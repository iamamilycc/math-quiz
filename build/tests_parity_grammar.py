#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
功能：两个站的造句判分引擎必须逐字一致（parity）
用法：python3 build/tests_parity_grammar.py
⭐ 为什么：同一句话在测验站被判错、在精读站被判对，孩子就不知道该信谁。
   引擎只有一份单一事实源，精读站那份由 sync_grammar.py 生成——手改就会被这支测试挡下。
"""
import hashlib
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(HERE, 'grammar_en.js')
DST = os.path.abspath(os.path.join(ROOT, '..', 'jingdu', 'assets', 'grammar-en.js'))
FAILS = []


def ck(name, cond, detail=''):
    print(('  ✅ ' if cond else '  ❌ ') + name + ('' if cond else '   << ' + str(detail)[:200]))
    if not cond:
        FAILS.append(name)


def body_of(text):
    m = re.search(r'/\* ==== 引擎正文开始（逐字复制，勿改）==== \*/\n([\s\S]*?)\n/\* ==== 引擎正文结束 ==== \*/', text)
    return m.group(1) if m else None


def main():
    src = open(SRC, encoding='utf-8').read()
    ck('单一事实源存在', bool(src.strip()))
    if not os.path.exists(DST):
        ck('精读站那份存在', False, DST + ' 不存在，先跑 python3 build/sync_grammar.py')
    else:
        dst = open(DST, encoding='utf-8').read()
        body = body_of(dst)
        ck('精读站那份抽得出引擎正文', body is not None)
        if body is not None:
            ck('两边引擎逐字一致',
               hashlib.sha256(body.encode()).hexdigest() == hashlib.sha256(src.encode()).hexdigest(),
               '不一致 —— 别手改精读站那份，改 build/grammar_en.js 后重跑 sync_grammar.py')
        ck('精读站那份写了「不要手改」', '不要手改' in dst)
        ck('精读站那份挂上了 window.GrammarEN', 'window.GrammarEN' in dst)
        for fn in ['checkGrammar', 'autoFix', 'collocHits', 'senseHits', 'hasWord',
                   'usSpellingOf', 'confusableNote']:
            ck('导出了 ' + fn, re.search(r'\b%s:\s*%s\b' % (fn, fn), dst) is not None)

        # ⭐ 零孤儿：精读站用到的每个 GrammarEN.xxx 都必须真的被导出。
        #    手写导出列表一定会漏（这条就是漏掉 confusableNote / usSpellingOf 之后加的），
        #    grep「有没有调用」抓不到，只有把两边对起来才抓得到。
        jd_dir = os.path.abspath(os.path.join(ROOT, '..', 'jingdu', 'assets'))
        used = set()
        if os.path.isdir(jd_dir):
            for fn in os.listdir(jd_dir):
                if not fn.endswith('.js') or fn == 'grammar-en.js':
                    continue
                txt = open(os.path.join(jd_dir, fn), encoding='utf-8').read()
                used |= set(re.findall(r'GrammarEN\s*&&\s*GrammarEN\.(\w+)', txt))
                used |= set(re.findall(r'\bG\.(\w+)\s*\(', txt))
                used |= set(re.findall(r'window\.GrammarEN\.(\w+)', txt))
        exported = set(re.findall(r'(\w+):\s*\1\b', dst)) | set(re.findall(r'(\w+):\s*\w+\b', dst))
        missing = sorted(u for u in used if u not in exported)
        ck('精读站用到的每个引擎函数都被导出了', not missing,
           '这些被调用却没导出（调用时会 undefined，页面静默失效）：' + ', '.join(missing))

    # 引擎必须真的被两个站用上
    words_html = os.path.join(ROOT, 'words.html')
    if os.path.exists(words_html):
        w = open(words_html, encoding='utf-8').read()
        ck('测验站已内联引擎', '英语句子语法检查器' in w and 'function checkGrammar' in w)
    jd_lesson = os.path.abspath(os.path.join(ROOT, '..', 'jingdu', 'assets', 'lesson.js'))
    if os.path.exists(jd_lesson):
        j = open(jd_lesson, encoding='utf-8').read()
        ck('精读站造句真的调用了引擎', 'GrammarEN' in j,
           '精读站还在把对错交给 AI／自评 —— 儿童向产品不准把校验推给人')

    print()
    if FAILS:
        print('❌ 失败 %d 项：%s' % (len(FAILS), '、'.join(FAILS)))
        sys.exit(1)
    print('✅ 两站引擎 parity 全部通过')


if __name__ == '__main__':
    main()
