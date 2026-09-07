#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
功能：build_words.py 的 _has_word（建置端）与 words.html 的 hasWord（孩子造句端）必须判得一样。
用法：python3 build/tests_parity.py
⭐ 为什么必须测：同一条规则写了两份实现。两边不一致会出现最难查的问题——
   建置说这个例句合格，孩子写同样的形式却被判「没用上这个词」。
"""
import os, sys, re, json, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, 'build')
from build_words import _has_word

CASES = [
    ('catch', 'The cat caught a mouse last night.'),
    ('catch', 'Try to catch the ball with both hands.'),
    ('tall',  'He is the tallest boy in our class.'),
    ('tall',  'My father is taller than my uncle.'),
    ('young', 'She looks younger than her sister.'),
    ('big',   'This is the biggest house in town.'),
    ('happy', 'She is happier than she was before.'),
    ('study', 'My sister studies music at university.'),
    ('stop',  'The bus stopped in front of us.'),
    ('like',  'He liked that film very much.'),
    ('go',    'He went to school by bike yesterday.'),
    ('see',   'I saw my teacher at the station.'),
    ('write', 'She has written three letters today.'),
    ('handbag', 'She put her keys into the handbag.'),
    ('excuse me', 'Excuse me, where is the station?'),
    ('excuse me', 'Sorry, where is the station?'),      # 没用上 → 两边都该 False
    ('book',  'I go to school every single day.'),       # 没用上 → 两边都该 False
    ('very much', 'I like this story book very much.'),
    ('very much', 'I like this story book a lot.'),      # 没用上
    ('thank you', 'Thank you for helping me today.'),
]

# 用 node 跑页面里的 hasWord
src = open('words.html', encoding='utf-8').read()
m = re.search(r'function hasWord\(s, w\) \{[\s\S]*?\n\}', src)
mv = re.search(r'const VERB_FORMS = \{[\s\S]*?\n\};', src)
mn = re.search(r'function normSent\(s\) \{[\s\S]*?\n\}', src)
if not (m and mv and mn):
    print('❌ 抽不出前端 hasWord / VERB_FORMS / normSent'); sys.exit(1)
js = mv.group(0) + '\n' + mn.group(0) + '\n' + m.group(0) + '\n' + \
     'const cases=' + json.dumps(CASES, ensure_ascii=False) + ';\n' + \
     'console.log(JSON.stringify(cases.map(c=>hasWord(c[1],c[0]))));'
open('/tmp/parity.js', 'w', encoding='utf-8').write(js)
out = subprocess.run(['node', '/tmp/parity.js'], capture_output=True, text=True)
if out.returncode != 0:
    print('❌ node 执行失败：', out.stderr[:300]); sys.exit(1)
js_res = json.loads(out.stdout.strip())
py_res = [_has_word(sent, w) for w, sent in CASES]

bad = 0
for (w, sent), a, b in zip(CASES, py_res, js_res):
    if a != b:
        print('  ❌ 判不一致  词=%-11s 建置端=%-5s 造句端=%-5s  %s' % (w, a, b, sent)); bad += 1
print('  %d/%d 两端判定一致' % (len(CASES) - bad, len(CASES)))

# 全册例句：两端都必须认为「用上了这个词」
sys.path.insert(0, 'build')
from words_data import DATA
n = 0
for u in DATA['units']:
    for s in u['sections']:
        for w in s['words']:
            for e in w['egs']:
                if not _has_word(e, w['w']):
                    print('  ❌ 建置端认为没用上：', w['w'], '|', e); bad += 1
                n += 1
print('  %d 个例句在建置端全部通过' % n)

print('\n❌ 失败 %d 项' % bad if bad else '\n✅ 两端规则完全一致')
sys.exit(1 if bad else 0)
