#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
功能：造句 AI 第二层的闭环测试（用 mock 拦截 fetch，不需要真的 API Key）
用法：python3 build/tests_ai.py
⭐ 要验证的核心：AI 是「加分项」，绝不能变成「减分项」——
   没 Key 照常用、AI 挂了不挡路、AI 判错能人工否决。
"""
import os, sys, socket, http.server, threading, functools

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
FAILS = []


def ck(name, cond, detail=''):
    print(('  ✅ ' if cond else '  ❌ ') + name + ('' if cond else '   << ' + str(detail)[:200]))
    if not cond:
        FAILS.append(name)


# ⚠️ Playwright 的 evaluate 只传一个参数——写成 (reply, status) 会让 status 永远是
#    undefined，测试就会「因为错误的原因通过」。必须收成一个参数再解构。
MOCK = """(args) => {
  const reply = args[0], status = args[1];
  window.__aiCalls = 0;
  window.fetch = async (url, opt) => {
    window.__aiCalls++;
    window.__aiUrl = url;
    window.__aiAuth = (opt.headers || {})['Authorization'] || '';
    window.__aiBody = opt.body;
    if (status === 'timeout') { await new Promise(r => setTimeout(r, 20000)); }
    if (status && status !== 200 && status !== 'timeout')
      return { ok: false, status: status, text: async () => 'err' };
    return { ok: true, status: 200, json: async () => ({ choices: [{ message: { content: JSON.stringify(reply) } }] }) };
  };
}"""


def main():
    from playwright.sync_api import sync_playwright
    s = socket.socket(); s.bind(('127.0.0.1', 0)); port = s.getsockname()[1]; s.close()
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
    httpd = http.server.ThreadingHTTPServer(('127.0.0.1', port), h)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    try:
        with sync_playwright() as pw:
            b = pw.chromium.launch(); pg = b.new_page(viewport={'width': 400, 'height': 900})
            errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.goto(f'http://127.0.0.1:{port}/words.html', wait_until='networkidle')
            pg.wait_for_timeout(300)
            T = lambda: pg.evaluate("document.body.innerText")
            btn = lambda t: pg.locator(f'button:has-text("{t}")').first

            # ---- 设置面板 ----
            btn('家长设置').click(); pg.wait_for_timeout(200)
            ck('设置面板打得开', 'AI 检查' in T() and '智谱 API Key' in T())
            ck('说明写清楚了不填也能用', '不填照样能用' in T(), T()[:300])
            ck('说明写清楚了规则能确定的不调 AI', '一律不调 AI' in T(), T()[:400])
            ck('说明写清楚了 Key 存哪里', '只存在' in T() and '这台设备' in T(), T()[:300])
            pg.fill('#aiKeyIn', 'test-key-123')
            btn('保存').click(); pg.wait_for_timeout(200)
            ck('保存后有回馈', '已保存' in T())
            ck('Key 存进 localStorage', pg.evaluate("localStorage.getItem('mathquiz_zhipu_key')") == 'test-key-123')
            ck('Key 输入框是密码类型（不明文显示）',
               pg.evaluate("(()=>{openSettings();const e=document.getElementById('aiKeyIn');return e&&e.type;})()") == 'password')

            def go_make():
                pg.evaluate("renderHome(); openUnit(0); openSec(0); openMode('make')")
                pg.wait_for_timeout(250)

            def try_sent(v):
                pg.fill('#mkIn', v)
                btn('检查我的句子').click()
                pg.wait_for_timeout(700)
                return T()

            # ---- ① AI 说通过 ----
            go_make()
            pg.evaluate(MOCK, [{"ok": True, "tip": "意思很清楚", "better": "Excuse me, could you give me a hand?",
                                "betterZh": "打扰一下，能帮我个忙吗？", "diff": "把 help me 换成更常用的 give me a hand"}, 200])
            t = try_sent('Excuse me, can you help me now?')
            ck('语法层先给出通过', '语法检查通过' in t, t[-300:])
            ck('AI 说通过 → 显示意思也没问题', '意思也没问题' in t, t[-300:])
            ck('显示欧美人的说法', '欧美人平常会这样说' in t, t[-400:])
            ck('说清楚差在哪', '差在哪' in t and 'give me a hand' in t, t[-400:])
            ck('请求发到智谱端点', 'open.bigmodel.cn' in pg.evaluate("window.__aiUrl || ''"))
            ck('带上了 Key', 'test-key-123' in pg.evaluate("window.__aiAuth || ''"))

            # ---- ② AI 说意思不通 ----
            go_make()
            pg.evaluate(MOCK, [{"ok": False, "tip": "书不能吃", "fix": "I read a book every day.",
                                "better": "Please excuse my late reply.", "betterZh": "请原谅我回复得晚。"}, 200])
            # 句子必须用上当前生词（excuse），否则被硬检查提前挡下、走不到 AI
            t = try_sent('I eat this excuse every day.')
            ck('语法层仍判通过（这句语法确实没错）', '语法检查通过' in t, t[-300:])
            ck('AI 的话降级成「另外提了一句」', 'AI 老师另外提了一句' in t and '书不能吃' in t, t[-400:])
            # ⭐ 儿童向产品不准把校验推给孩子：不能出现「你自己判断 AI 说得对不对」
            ck('不要孩子裁决 AI', '我觉得这句没问题' not in t, t[-300:])
            ck('明确告诉孩子系统判他通过', '你这句是通过的' in t, t[-400:])
            ck('主按钮仍是「收下」，不卡住', '收下这一句' in t, t[-200:])
            # ⭐ 聚焦二次核对：AI 的建议句跑题了（没用上 excuse）→ 直接丢弃，不给孩子看
            ck('跑题的 AI 建议被丢弃', 'I read a book every day.' not in t, t[-300:])

            # 同样的场景，AI 这次给的建议句用上了这个词 → 才显示
            go_make()
            pg.evaluate(MOCK, [{"ok": False, "tip": "借口不能吃", "fix": "I make this excuse every day.",
                                "better": "I always use this excuse.", "betterZh": "我总是用这个借口。"}, 200])
            t = try_sent('I eat this excuse every day.')
            ck('用上了这个词的建议句才显示', 'I make this excuse every day.' in t, t[-400:])

            # ---- ③ AI 挂了不能挡路 ----
            go_make()
            pg.evaluate(MOCK, [{}, 500])
            t = try_sent('Excuse me, can you help me now?')
            ck('AI 报错时语法结论仍然有效', '语法检查通过' in t and '仍然有效' in t, t[-300:])
            ck('AI 报错时仍能继续', '收下这一句' in t, t[-200:])

            # ---- ④ Key 无效 ----
            go_make()
            pg.evaluate(MOCK, [{}, 401])
            t = try_sent('Excuse me, can you help me now?')
            ck('401 提示 Key 无效', 'Key 无效' in t, t[-300:])
            ck('401 时仍能继续', '收下这一句' in t, t[-200:])

            # ---- ⑤ 语法写错时也要给母语者的说法（孩子最需要的就是这一刻）----
            go_make()
            pg.evaluate(MOCK, [{"ok": True, "better": "He really likes this excuse.",
                                "betterZh": "他很喜欢这个借口。", "diff": "very like 改成 really like"}, 200])
            t = try_sent('He like this excuse very much.')
            ck('语法错照常给出改法', '少了 s' in t, t[-250:])
            # excuse 配了「常用句型」，就给句型块；没配的词才退回课本原句 —— 两者必有其一
            ck('语法错也不用 AI 就有母语者说法',
               ('母语者会这样说' in t) or ('欧美人常这样用' in t), t[-400:])
            ck('语法错时也请了 AI', pg.evaluate("window.__aiCalls") == 1,
               'aiCalls=' + str(pg.evaluate("window.__aiCalls")))
            ck('拿「改好的句子」去问 AI，不拿错句', 'He likes this excuse very much.' in
               (pg.evaluate("window.__aiBody") or ''), (pg.evaluate("window.__aiBody") or '')[-200:])
            ck('AI 的母语者说法也显示出来', 'He really likes this excuse.' in t, t[-400:])

            # ---- ⑤b ⭐ 规则已经能百分之百确定时，绝不调 AI ----
            # 语法错 + 命中中式搭配表：改法和地道说法规则都给得出，AI 没有插嘴的余地
            go_make()
            pg.evaluate(MOCK, [{"ok": True, "better": "AI SHOULD NOT BE CALLED"}, 200])
            t = try_sent('I very like this excuse.')
            ck('中式说法命中 → 一次都不调 AI', pg.evaluate("window.__aiCalls") == 0,
               'aiCalls=' + str(pg.evaluate("window.__aiCalls")))
            ck('规则自己给出了地道说法', 'really like' in t, t[-400:])
            ck('页面上没有出现 AI 的内容', 'AI SHOULD NOT BE CALLED' not in t)
            # 语法全对、但说法不地道：同样由规则收口，不走 AI
            go_make()
            pg.evaluate(MOCK, [{"ok": True, "better": "AI SHOULD NOT BE CALLED"}, 200])
            t = try_sent('Excuse me, I read a book everyday.')
            ck('语法对但中式 → 也不调 AI', pg.evaluate("window.__aiCalls") == 0,
               'aiCalls=' + str(pg.evaluate("window.__aiCalls")))
            ck('直接给出改好的整句', 'every day' in t, t[-400:])

            # ---- ⑥ 清除 Key 后回到纯规则 ----
            pg.evaluate("aiSetKey('')")
            go_make()
            pg.evaluate(MOCK, [{"ok": True}, 200])
            t = try_sent('Excuse me, can you help me now?')
            ck('清除 Key 后不再调 AI', pg.evaluate("window.__aiCalls") == 0)
            ck('清除 Key 后照常通过', '语法检查通过' in t and '收下这一句' in t, t[-200:])

            # ---- ⑦ AI 给出语法有错的句子 → 必须拦下，不能给孩子看 ----
            pg.evaluate("aiSetKey('k'); renderHome(); openUnit(0); openSec(0); openMode('make')")
            pg.wait_for_timeout(250)
            pg.evaluate(MOCK, [{"ok": True, "tip": "很好",
                                "better": "He like this excuse very much.",   # 三单漏 s，故意写错
                                "betterZh": "他很喜欢这个借口。", "diff": "换了说法"}, 200])
            t = try_sent('Excuse me, can you help me now?')
            ck('AI 给的错句被拦下不显示', 'He like this excuse' not in t, t[-400:])
            ck('拦下时告诉用户原因', '没通过语法检查' in t, t[-300:])
            ck('语法结论仍然有效', '语法检查通过' in t, t[-400:])

            # ---- ⑧ AI 给出正确的句子 → 正常显示 ----
            pg.evaluate("renderHome(); openUnit(0); openSec(0); openMode('make')"); pg.wait_for_timeout(250)
            pg.evaluate(MOCK, [{"ok": True, "tip": "很好",
                                "better": "Excuse me, could you give me a hand?",
                                "betterZh": "打扰一下，能帮我个忙吗？", "diff": "换成更常用的说法"}, 200])
            t = try_sent('Excuse me, can you help me now?')
            ck('AI 给的正确句正常显示', 'give me a hand' in t, t[-300:])
            ck('正确时不出现拦截提示', '没通过语法检查' not in t, t[-300:])

            ck('默认模型是当前免费的 glm-4.7-flash',
               pg.evaluate("(()=>{localStorage.removeItem('mathquiz_zhipu_model');return aiGetModel();})()") == 'glm-4.7-flash')

            ck('全程无 JS 错误', not errs, errs[:2])
            b.close()
    finally:
        httpd.shutdown()

    print()
    if FAILS:
        print('❌ 失败 %d 项：%s' % (len(FAILS), '、'.join(FAILS)))
        sys.exit(1)
    print('✅ AI 第二层全部通过')


if __name__ == '__main__':
    main()
