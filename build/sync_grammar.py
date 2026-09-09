#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
功能：把共用的英语造句判分引擎同步到精读站（jingdu）
输入：build/grammar_en.js（单一事实源）+ build/words_data.py（词表）
输出：../jingdu/assets/grammar-en.js
用法：python3 build/sync_grammar.py
⭐ 为什么要有：两个站的造句关判分规则必须完全一致。
   孩子在测验站写「I very like it.」被判错，在精读站却被判对 —— 那他就不知道该信谁。
   所以引擎只有一份，精读站那份由本脚本生成，改动会被 tests_parity_grammar.py 挡下。
验证成功：印出「已同步」＋ python3 build/tests_parity_grammar.py 退出码 0
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
JINGDU = os.path.abspath(os.path.join(ROOT, '..', 'jingdu'))
SRC = os.path.join(HERE, 'grammar_en.js')
DST = os.path.join(JINGDU, 'assets', 'grammar-en.js')

BANNER = """/* ⚠️⚠️ 这个文件是**自动生成**的，不要手改 ⚠️⚠️
   单一事实源：math_quiz_deploy/build/grammar_en.js
   重新生成：  python3 build/sync_grammar.py（在 math_quiz_deploy 下跑）
   为什么：两个站的造句判分必须一模一样，孩子在这边被判错、在那边被判对，他就不知道该信谁。
   引擎正文 sha256：%s
*/
"""


def wrap(engine: str, words_js: str) -> str:
    """包成 IIFE 挂到 window.GrammarEN——精读站有自己的 normalize 等同名函数，不能直接摊在全局。"""
    digest = hashlib.sha256(engine.encode('utf-8')).hexdigest()
    return (BANNER % digest) + (
        "window.GRAMMAR_WORDS = %s;\n"
        "window.GrammarEN = (function () {\n"
        "var GRAMMAR_WORDS = window.GRAMMAR_WORDS;\n"
        "/* ==== 引擎正文开始（逐字复制，勿改）==== */\n"
        "%s\n"
        "/* ==== 引擎正文结束 ==== */\n"
        "return { checkGrammar: checkGrammar, autoFix: autoFix, collocHits: collocHits,\n"
        "         collocFix: collocFix, hitText: hitText, senseHits: senseHits,\n"
        "         hasWord: hasWord, tooSimilar: tooSimilar,\n"
        "         normalize: normalize, normSent: normSent, wordCount: wordCount,\n"
        "         COLLOC: COLLOC, MK_PER_WORD: MK_PER_WORD, MK_MIN_WORDS: MK_MIN_WORDS };\n"
        "})();\n" % (words_js, engine)
    )


def main():
    if not os.path.isdir(JINGDU):
        print('❌ 找不到精读站目录：%s' % JINGDU)
        sys.exit(1)
    sys.path.insert(0, HERE)
    from words_data import DATA
    words = [{'w': w['w'], 'pos': w['pos']}
             for u in DATA['units'] for s in u['sections'] for w in s['words']]
    engine = open(SRC, encoding='utf-8').read()
    out = wrap(engine, json.dumps(words, ensure_ascii=False))
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    open(DST, 'w', encoding='utf-8').write(out)
    print('✅ 已同步 → %s' % DST)
    print('   引擎 %d 行 / 词表 %d 词 / sha256 %s'
          % (engine.count('\n') + 1, len(words), hashlib.sha256(engine.encode('utf-8')).hexdigest()[:16]))


if __name__ == '__main__':
    main()
