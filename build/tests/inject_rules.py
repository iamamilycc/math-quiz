# -*- coding: utf-8 -*-
"""
功能：对 build_eng.py 的全局规则 G1-G5 逐条注入故障，确认体检真的会变红。
用法：python3 build/tests/inject_rules.py   （在专案根目录执行）
成功标准：五条规则全部输出 ✅，且末尾「还原后 ✅ 体检通过」。
设计：只备份/还原数据文件本身，不整目录 rmtree —— 否则会连测试脚本自己一起删掉。
"""
import subprocess, sys, os, re, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
TARGETS = ['build/build_eng.py', 'build/eng_data.py'] + \
          [f'build/eng_c{i}.py' for i in range(2, 8)]

CASES = [
 ("G1 错题本去重键碰撞", 'build/eng_c3.py',
  '''"point": "y 结尾的处理",
         "stem": "所有以 y 结尾的动词，变第三人称单数时都要把 y 变成 i 再加 es。"''',
  '''"point": "并列主语的数",
         "stem": "Tom and Jane 作主语时是复数，动词不加 s，应该说 Tom and Jane like music。"'''),
 ("G2 单选答案集中", None, None, None),
 ("G3 单节判断题全同", 'build/eng_c7.py',
  '"stem": "news 以 s 结尾，所以它是复数名词，应该说 The news are good.",\n         "answer": "错"',
  '"stem": "news 以 s 结尾，所以它是复数名词，应该说 The news are good.",\n         "answer": "对"'),
 ("G4 缩写题用了 fill", 'build/eng_c2.py',
  '"stem": "写出 write 的现在分词形式：______"',
  '"stem": "写出 write is not 的缩写形式：______"'),
 ("G5 fill 冗余变体", 'build/eng_c2.py',
  '"answer": ["There"]', '"answer": ["There", "there"]'),
]

BACKUP = {p: open(p, encoding='utf-8').read() for p in TARGETS}

def restore():
    for p, s in BACKUP.items():
        open(p, 'w', encoding='utf-8').write(s)

def run():
    # ⚠️ 必须先清 __pycache__：注入若不改变文件大小（如 "A"→"B"、错→对），
    # 同秒覆写会让 Python 的 (mtime, size) 缓存校验失效，读到旧 .pyc，
    # 于是「注入了却看不到变红」，会被误判成规则失效。
    shutil.rmtree('build/__pycache__', ignore_errors=True)
    r = subprocess.run([sys.executable, 'build/build_eng.py'],
                       capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr

fails = 0
for name, f, old, new in CASES:
    restore()
    if f is None:                                  # G2：所有单选答案强改成 B
        for p in TARGETS:
            s = open(p, encoding='utf-8').read()
            open(p, 'w', encoding='utf-8').write(re.sub(r'"answer": "[ACD]"', '"answer": "B"', s))
    else:
        s = open(f, encoding='utf-8').read()
        if s.count(old) != 1:
            print(f"  ⚠️ {name}：注入定位 {s.count(old)} 处，无法注入")
            fails += 1
            continue
        open(f, 'w', encoding='utf-8').write(s.replace(old, new))
    code, out = run()
    if code != 0:
        print(f"  ✅ {name} → 体检变红")
        for l in [x for x in out.split('\n') if x.strip().startswith('-')][:1]:
            print(f"        {l.strip()[:96]}")
    else:
        print(f"  ❌ {name} → 注入后体检仍通过，规则失效！")
        fails += 1

restore()
code, _ = run()
print(f"\n还原后：{'✅ 体检通过' if code == 0 else '❌ 还原失败'}")
sys.exit(1 if fails or code else 0)
