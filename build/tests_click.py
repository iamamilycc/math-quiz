#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
功能：单词模块「真点击」端到端走查（不用 evaluate 调函数，模拟孩子实际操作）
用法：python3 build/tests_click.py
⭐ 为什么要真点击：evaluate 调函数能跑通，不代表按钮点得动
   （innerHTML 里拼的 onclick 若函数没挂 window 就会静默失效）。
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
        with sync_playwright() as pw:
            b = pw.chromium.launch(); pg = b.new_page(viewport={'width': 400, 'height': 900})
            errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.goto(f'http://127.0.0.1:{port}/words.html', wait_until='networkidle')
            pg.wait_for_timeout(400)
            T = lambda: pg.evaluate("document.body.innerText")
            card = lambda i: pg.locator('.big-card').nth(i)
            btn = lambda txt: pg.locator(f'button:has-text("{txt}")').first

            card(0).click(); pg.wait_for_timeout(250)
            ck('点单元卡进得去', 'Lesson 1-2' in T())
            card(0).click(); pg.wait_for_timeout(250)
            ck('点节卡进得去', '选一种练法' in T() and '本节单词表' in T())

            # ---- 记忆卡 ----
            card(0).click(); pg.wait_for_timeout(250)
            ck('点「记忆卡」进得去', 'excuse' in T() and '/ɪkˈskjuːz/' in T())
            btn('记住了，翻面').click(); pg.wait_for_timeout(250)
            ck('点「翻面」有反应', '____' in T())
            pg.fill('#cdIn', 'excuse'); btn('检查').click(); pg.wait_for_timeout(250)
            ck('拼对判对', '拼对了' in T())
            btn('下一个').click(); pg.wait_for_timeout(250)
            ck('点「下一个」前进', '第 2 / 21 个' in T())
            # 拼错要判错并进错题本
            btn('记住了，翻面').click(); pg.wait_for_timeout(200)
            pg.fill('#cdIn', 'zzz'); btn('检查').click(); pg.wait_for_timeout(250)
            ck('拼错判错并给正确拼写', '正确拼写是' in T())
            ck('拼错给音标', '/' in T())
            ck('拼错指出差在哪个字母', '差在这里' in T(), T()[-300:])
            ck('拼错给例句帮助记忆', '看一遍例句再记' in T(), T()[-300:])
            ck('拼错进错题本', pg.evaluate(
                "JSON.parse(localStorage.getItem('mathquiz_wrongbook_v1')||'[]').some(x=>x.subject==='engword')"))

            # ---- 背诵 ----
            btn('← 返回').click(); pg.wait_for_timeout(200)
            card(1).click(); pg.wait_for_timeout(250)
            ck('点「背诵」进得去', '只看中文' in T())
            import re
            ck('背诵页面不泄露英文答案', not re.search(r'[A-Za-z]{3,}', T().replace('Lesson', '')), T()[:120])
            btn('给点提示').click(); pg.wait_for_timeout(200)
            ck('点「给点提示」有反应', '开头是' in T())

            # ---- 造句 ----
            btn('← 返回').click(); pg.wait_for_timeout(200)
            card(2).click(); pg.wait_for_timeout(300)
            ck('点「造句」进得去', '先看看别人怎么用' in T())
            pg.fill('#mkIn', 'I like it.'); btn('检查我的句子').click(); pg.wait_for_timeout(250)
            ck('少于 5 词被挡', '至少 5 个单词' in T())
            pg.fill('#mkIn', 'He like this excuse very much.'); btn('检查我的句子').click(); pg.wait_for_timeout(300)
            ck('语法错被判错并列出问题', '个地方要改' in T() and '少了 s' in T(), T()[-200:])
            btn('改好了，再检查一次').click(); pg.wait_for_timeout(200)
            pg.fill('#mkIn', 'He likes this excuse very much.'); btn('检查我的句子').click(); pg.wait_for_timeout(300)
            ck('改对后判通过', '检查通过' in T(), T()[-160:])
            btn('收下这一句').click(); pg.wait_for_timeout(250)
            ck('点「收下」进到第 2 句', '第 2 / 3 句' in T())
            pg.fill('#mkIn', 'He likes this excuse very much.'); btn('检查我的句子').click(); pg.wait_for_timeout(250)
            ck('第 2 句重复被挡', '太像' in T())

            # ---- 错题本：三种练法都错同一个词 → 合并成一条，但各自写错的内容都要留下 ----
            # ⚠️ 进度也要清——三种练法现在都会「续做」，不清的话会停在各自上次的位置，
            #    三次错的就不是同一个词了，合并断言自然对不上。
            pg.evaluate("localStorage.removeItem('mathquiz_wrongbook_v1'); localStorage.removeItem('mathquiz_words_prog_v1'); renderHome(); openUnit(0); openSec(0); openMode('card'); cardFlip()")
            pg.wait_for_timeout(200)
            pg.fill('#cdIn', 'aaa'); btn('检查').click(); pg.wait_for_timeout(200)
            pg.evaluate("renderHome(); openUnit(0); openSec(0); openMode('recall')"); pg.wait_for_timeout(250)
            pg.fill('#rcIn', 'bbb'); btn('检查').click(); pg.wait_for_timeout(200)
            pg.evaluate("renderHome(); openUnit(0); openSec(0); openMode('make')"); pg.wait_for_timeout(250)
            # 用一句有语法错的：只有判错时才会出现「这句先跳过」，通过的句子本来就不该进错题本
            pg.fill('#mkIn', 'He like this excuse very much.')
            btn('检查我的句子').click(); pg.wait_for_timeout(350)
            fb = pg.inner_text('#mkFb')
            ck('写错时给了「改好应该是这样」', '改好应该是这样' in fb, fb[:120])
            ck('写错时也给了母语者说法（不用 AI Key）', '母语者会这样说' in fb, fb[:160])
            btn('这句先跳过').click(); pg.wait_for_timeout(250)
            book = pg.evaluate("JSON.parse(localStorage.getItem('mathquiz_wrongbook_v1')||'[]')")
            ck('同一个词合并成一条', len(book) == 1, len(book))
            if book:
                ua = book[0].get('userAnswer', '')
                ck('错误次数累计到 3', book[0].get('wrongCount') == 3, book[0].get('wrongCount'))
                ck('拼写写错的内容留下了', '记忆卡拼写写成「aaa」' in ua, ua)
                ck('背诵写错的内容留下了', '背诵写成「bbb」' in ua, ua)
                ck('造句写的内容留下了', '造句写成' in ua, ua)

            # ---- 回得去科目列表（不能只靠浏览器上一页）----
            pg.evaluate("renderHome()"); pg.wait_for_timeout(200)
            ck('首页有「返回科目选择」链接', pg.evaluate(
                "(()=>{const a=document.getElementById('homeLink');return !!a && a.getAttribute('href')==='index.html' && a.style.display!=='none';})()"))
            pg.evaluate("openUnit(0)"); pg.wait_for_timeout(200)
            ck('进到里层后换成「← 返回」不并排', pg.evaluate(
                "(()=>{const a=document.getElementById('homeLink'),b=document.getElementById('backBtn');return a.style.display==='none' && b.style.display!=='none';})()"))

            ck('全程无 JS 错误', not errs, errs[:2])
            b.close()
    finally:
        httpd.shutdown()

    print()
    if FAILS:
        print('❌ 失败 %d 项：%s' % (len(FAILS), '、'.join(FAILS)))
        sys.exit(1)
    print('✅ 真点击端到端全部通过')


if __name__ == '__main__':
    main()
