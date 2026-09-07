# -*- coding: utf-8 -*-
"""
功能：英语模块深度自审，查 build_eng.py 的 validate() 之外的质量问题。
用法：python3 build/tests/audit_eng.py   （在专案根目录执行）
成功标准：末尾输出「✅ 全部通过」。信息项不需修。
"""
import sys, os, re, json, collections

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
sys.path.insert(0, 'build')
from eng_data import DATA

def norm(t):                       # 复刻前端 normalize
    return re.sub(r'\s+', '', str(t).strip()).replace('　', '').lower()

issues = collections.defaultdict(list)
info   = collections.defaultdict(list)      # 已判定可接受

allq = [(c['id'], s['id'], q) for c in DATA['chapters']
        for s in c['sections'] for q in s['quiz']]
allnotes = [(c['id'], s['id'], n) for c in DATA['chapters']
            for s in c['sections'] for n in s['notes']]

# A. fill 题的判分陷阱
for cid, sid, q in allq:
    if q['type'] != 'fill':
        continue
    if re.search(r'缩写', q['stem']):
        issues['A1-缩写题用了 fill（答案必含撇号）'].append((sid, q['id']))
    for a in q['answer']:
        if re.search(r"[,.，。、]", a):
            issues['A3-fill 答案含标点（判分不会忽略）'].append((sid, q['id'], a))

# B. 重复
stems = collections.Counter(norm(q['stem']) for _, _, q in allq)
for st, n in stems.items():
    if n > 1:
        where = [(s, q['id']) for _, s, q in allq if norm(q['stem']) == st]
        info['B1-题干模板重复'].append((n, where[:6], st[:50]))
keys = collections.Counter((q['point'], q['stem']) for _, _, q in allq)
for k, n in keys.items():
    if n > 1:
        issues['B2-错题本去重键碰撞'].append((k[0], n))

# C. 答案可猜性
judge = [q['answer'] for _, _, q in allq if q['type'] == 'judge']
jc = collections.Counter(judge)
print(f"判断题：对 {jc.get('对',0)} / 错 {jc.get('错',0)}  共 {len(judge)}")
if judge and not (0.3 <= jc.get('对', 0) / len(judge) <= 0.7):
    issues['C1-判断题答案整体偏斜'].append(dict(jc))
ch = [q['answer'] for _, _, q in allq if q['type'] == 'choice']
cc = collections.Counter(ch)
print(f"单选题字母分布：{dict(sorted(cc.items()))}  共 {len(ch)}")
for k, v in cc.items():
    if v / len(ch) > 0.40:
        issues['C2-单选答案集中'].append((k, v, len(ch)))
for c in DATA['chapters']:
    for s in c['sections']:
        js = [q['answer'] for q in s['quiz'] if q['type'] == 'judge']
        if len(js) >= 2 and len(set(js)) == 1:
            issues['C3-单节判断题答案全同'].append((s['id'], js))

# D. 选项结构
for cid, sid, q in allq:
    if q['type'] not in ('choice', 'multi'):
        continue
    letters = [o[0] for o in q['options']]
    if letters != [chr(65 + i) for i in range(len(letters))]:
        issues['D1-选项字母不从 A 连续'].append((sid, q['id'], letters))
    for o in q['options']:
        if len(o.strip()) <= 3:
            issues['D2-选项内容过短'].append((sid, q['id'], o))

# E. HTML 标签闭合
def tagcheck(txt, where):
    for tag in ('b', 'u', 'i'):
        if len(re.findall(rf'<{tag}>', txt)) != len(re.findall(rf'</{tag}>', txt)):
            issues['E1-标签未闭合'].append((where, tag))
for cid, sid, q in allq:
    tagcheck(q['stem'], f"{sid}/q{q['id']}/stem")
    tagcheck(q['explain'], f"{sid}/q{q['id']}/explain")
for cid, sid, n in allnotes:
    tagcheck(n['explain'], f"{sid}/{n['point'][:10]}")
    tagcheck(n['think'], f"{sid}/{n['point'][:10]}/think")
    for e in n['examples']:
        tagcheck(e['text'], f"{sid}/{n['point'][:10]}/例")

# F. 结构一致性
print("\n每章结构（题数 / 知识点数）：")
for c in DATA['chapters']:
    print(f"  {c['id']}: {[len(s['quiz']) for s in c['sections']]} / "
          f"{[len(s['notes']) for s in c['sections']]}")

# G. 需人工复核：以「不地道 / 语法没错」为由判错的题
#    铁律：题干问「正确的有」时，判错的理由必须是【语法错误】。
#    只是「不地道 / 语气不合适」的句子不能算错——否则孩子会把对的当错的背下来。
#    确实要考语用，题干必须写成「最合适的说法是」。
PRAGMATIC = re.compile(r'语法.{0,4}(没错|正确|成立|不算错)|不地道|一般不这么说|通常不这么')
for cid, sid, q in allq:
    if not PRAGMATIC.search(q.get('explain', '')):
        continue
    stem = q['stem']
    if re.search(r'最合适|最恰当|最自然|最地道', stem):
        continue                       # 题干已声明在比「合适度」，合规
    info['G1-用语用理由判错（需人工复核题干口径）'].append((sid, q['id'], stem[:34]))

print("\n" + "=" * 60)
print("信息项（已判定可接受，不需修）")
print("=" * 60)
for k in sorted(info):
    print(f"  ℹ️ {k}：{len(info[k])} 组")
    if k.startswith('G1'):
        for it in info[k]:
            print(f"     · {it[0]}/q{it[1]}  {it[2]}")
        print("     复核口径：判错的理由必须是【语法错误】；只是「不地道/语气不对」")
        print("     不能算错，否则孩子会把对的当错的背下来。要考语用就把题干")
        print("     写成「最合适的说法是」。")
    if k.startswith('B1'):
        print("     题干用统一模板（如「下列句子正确的有」）是刻意的：做题页每题上方")
        print("     有考点标签、错题本也显示 point + 章节，孩子能分清在考什么。")
        print("     真正会出事的是 point+stem 同时相同（错题本会合并），已由 G1 拦截。")

print("\n" + "=" * 60)
if not issues:
    print("✅ 全部通过")
    sys.exit(0)
total = 0
for k in sorted(issues):
    print(f"\n⚠️ {k}（{len(issues[k])} 项）")
    for it in issues[k][:10]:
        print("   -", it)
    total += len(issues[k])
print(f"\n合计 {total} 项待修")
sys.exit(1)
