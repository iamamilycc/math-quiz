#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
功能：单词模块「做一半退出，回来接着做」的闭环测试
用法：python3 build/tests_resume.py
⭐ 为什么必须测：进度存档是「只增不减」(Math.max)。如果重进页面时不回填 session 状态，
   孩子会从第 1 个重做，而且重做前面几个不会让进度前进——看起来就像进度卡死了。
   （这个坑在别的项目上踩过，这里焊成测试防止重犯。）
"""
import os, sys, socket, http.server, threading, functools

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
FAILS = []


def ck(name, cond, detail=''):
    print(('  ✅ ' if cond else '  ❌ ') + name + ('' if cond else '   << ' + str(detail)[:160]))
    if not cond:
        FAILS.append(name)


def main():
    from playwright.sync_api import sync_playwright
    s = socket.socket(); s.bind(('127.0.0.1', 0)); port = s.getsockname()[1]; s.close()
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
    httpd = http.server.ThreadingHTTPServer(('127.0.0.1', port), h)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    try:
        from playwright.sync_api import sync_playwright as _sp
        with _sp() as pw:
            b = pw.chromium.launch(); pg = b.new_page()
            errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
            url = f'http://127.0.0.1:{port}/words.html'
            pg.goto(url, wait_until='networkidle'); pg.wait_for_timeout(300)
            pg.evaluate("localStorage.clear()")

            prog = lambda k: pg.evaluate(
                "k => (JSON.parse(localStorage.getItem('mathquiz_words_prog_v1')||'{}')['w-u1-s1']||{})[k]", k)

            # ---- 记忆卡：做 3 个 → 退出 → 回来 ----
            pg.evaluate("openUnit(0); openSec(0); openMode('card')"); pg.wait_for_timeout(200)
            for _ in range(3):
                pg.evaluate("cardFlip()"); pg.wait_for_timeout(60)
                pg.evaluate("document.getElementById('cdIn').value = cur.sec.words[cd.i].w; cardCheck()")
                pg.wait_for_timeout(60)
                pg.evaluate("cardNext()"); pg.wait_for_timeout(60)
            ck('记忆卡做 3 个后进度 = 3', prog('card') == 3, prog('card'))
            ck('记忆卡答对数也记下了 = 3', prog('card_s') == 3, prog('card_s'))

            pg.reload(wait_until='networkidle'); pg.wait_for_timeout(350)
            pg.evaluate("openUnit(0); openSec(0); openMode('card')"); pg.wait_for_timeout(250)
            ck('重进后从第 4 个接着做', pg.evaluate("cd.i") == 3, '从第 %s 个' % (pg.evaluate("cd.i") + 1))
            ck('重进后答对数回填了', pg.evaluate("cd.ok") == 3, pg.evaluate("cd.ok"))
            pg.evaluate("cardFlip()"); pg.wait_for_timeout(60)
            pg.evaluate("document.getElementById('cdIn').value = cur.sec.words[cd.i].w; cardCheck()")
            pg.wait_for_timeout(120)
            ck('再做 1 个进度前进到 4（不再卡住）', prog('card') == 4, prog('card'))

            # ---- 背诵：同样的续做行为 ----
            pg.evaluate("renderHome(); openUnit(0); openSec(0); openMode('recall')"); pg.wait_for_timeout(200)
            for _ in range(2):
                pg.evaluate("document.getElementById('rcIn').value = cur.sec.words[rc.i].w; recallCheck()")
                pg.wait_for_timeout(60)
                pg.evaluate("recallNext()"); pg.wait_for_timeout(60)
            pg.reload(wait_until='networkidle'); pg.wait_for_timeout(350)
            pg.evaluate("openUnit(0); openSec(0); openMode('recall')"); pg.wait_for_timeout(250)
            ck('背诵重进后从第 3 个接着做', pg.evaluate("rc.i") == 2, '从第 %s 个' % (pg.evaluate("rc.i") + 1))

            # ---- 造句：进度以「句」计，续做要定位到 (第几个词, 第几句) ----
            pg.evaluate("renderHome(); openUnit(0); openSec(0); openMode('make')"); pg.wait_for_timeout(250)
            for _ in range(4):        # 4 句 = 第 1 个词 3 句 + 第 2 个词 1 句
                w = pg.evaluate("cur.sec.words[mk.i].w")
                pg.evaluate("v => { document.getElementById('mkIn').value = v; }",
                            'I really like this %s in my school bag today.' % w)
                pg.evaluate("makeCheck()"); pg.wait_for_timeout(200)
                pg.evaluate("makeAccept()"); pg.wait_for_timeout(120)
            ck('造句做 4 句后进度 = 4', prog('make') == 4, prog('make'))
            pg.reload(wait_until='networkidle'); pg.wait_for_timeout(350)
            pg.evaluate("openUnit(0); openSec(0); openMode('make')"); pg.wait_for_timeout(250)
            ck('造句重进后定位到第 2 个词的第 2 句',
               pg.evaluate("mk.i") == 1 and pg.evaluate("mk.j") == 1,
               '第 %s 个词第 %s 句' % (pg.evaluate("mk.i") + 1, pg.evaluate("mk.j") + 1))

            # ---- 全做完之后「再来一轮」要能从头练 ----
            pg.evaluate("""(() => { const p = JSON.parse(localStorage.getItem('mathquiz_words_prog_v1'));
                p['w-u1-s1'].card = 21; localStorage.setItem('mathquiz_words_prog_v1', JSON.stringify(p)); })()""")
            pg.evaluate("renderHome(); openUnit(0); openSec(0); openMode('card')"); pg.wait_for_timeout(250)
            ck('已全做完时重进 → 从头开新一轮', pg.evaluate("cd.i") == 0, pg.evaluate("cd.i"))
            ck('开新一轮不会让进度倒退', prog('card') == 21, prog('card'))

            ck('全程无 JS 错误', not errs, errs[:2])
            b.close()
    finally:
        httpd.shutdown()

    print()
    if FAILS:
        print('❌ 失败 %d 项：%s' % (len(FAILS), '、'.join(FAILS)))
        sys.exit(1)
    print('✅ 续做行为全部正确')


if __name__ == '__main__':
    main()
