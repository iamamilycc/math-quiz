# -*- coding: utf-8 -*-
"""
功能：把 words_data.py 的 DATA 注入 words_template.html，产出 words.html
输入：build/words_data.py, build/words_template.html
输出：words.html（部署目录根下）
用法：python3 build/build_words.py
校验：注入前先跑 validate()，任何一条不通过就中止，不写文件

⭐ 为什么校验这么严：例句是给孩子看的范例，他没有判断能力，例句错了会照着学。
   所以「3 句 / 每句 ≥5 词 / 必须用上该词 / 句首大写句尾标点 / 三句不重复」全部焊成硬规则。
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from words_data import DATA

EGS_REQUIRED = 3
EGS_MIN_WORDS = 5


def _norm(t):
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9\s]', ' ', str(t).lower())).strip()


# 常见不规则变形：孩子写 caught 来练 catch 是对的，不能判成「没用上这个词」
IRREGULAR = {
    'catch': ['caught'], 'buy': ['bought'], 'bring': ['brought'], 'think': ['thought'],
    'teach': ['taught'], 'go': ['went', 'gone'], 'see': ['saw', 'seen'], 'do': ['did', 'done'],
    'have': ['had'], 'make': ['made'], 'take': ['took', 'taken'], 'give': ['gave', 'given'],
    'come': ['came'], 'get': ['got'], 'eat': ['ate', 'eaten'], 'drink': ['drank', 'drunk'],
    'write': ['wrote', 'written'], 'read': ['read'], 'run': ['ran'], 'sit': ['sat'],
    'stand': ['stood'], 'meet': ['met'], 'leave': ['left'], 'lose': ['lost'], 'find': ['found'],
    'feel': ['felt'], 'keep': ['kept'], 'sleep': ['slept'], 'speak': ['spoke', 'spoken'],
    'wear': ['wore', 'worn'], 'sing': ['sang', 'sung'], 'swim': ['swam', 'swum'],
    'be': ['am', 'is', 'are', 'was', 'were', 'been'], 'say': ['said'], 'tell': ['told'],
    'pay': ['paid'], 'send': ['sent'], 'spend': ['spent'], 'hear': ['heard'], 'hold': ['held'],
    'fly': ['flew', 'flown'], 'drive': ['drove', 'driven'], 'fall': ['fell', 'fallen'],
    'ring': ['rang', 'rung'], 'win': ['won'], 'cut': ['cut'], 'put': ['put'], 'let': ['let'],
    'learn': ['learnt', 'learned'], 'lend': ['lent'], 'understand': ['understood'],
    # 不规则名词复数：写 teeth 来练 tooth 也算用上了
    'tooth': ['teeth'], 'foot': ['feet'], 'child': ['children'], 'man': ['men'],
    'woman': ['women'], 'mouse': ['mice'], 'person': ['people'], 'knife': ['knives'],
    'leaf': ['leaves'], 'shelf': ['shelves'], 'wife': ['wives'], 'life': ['lives'],
    'sweep': ['swept'],
    'sleep': ['slept'],
    'keep': ['kept'],
    'feel': ['felt'],
    'meet': ['met'],
    'leave': ['left'],
    'lose': ['lost'],
    'build': ['built'],
    'burn': ['burnt', 'burned'],
    'dream': ['dreamt', 'dreamed'],
    'smell': ['smelt', 'smelled'],
    'hang': ['hung'],
    'shine': ['shone'],
    'shoot': ['shot'],
    'sit': ['sat'],
    'stand': ['stood'],
    'wake': ['woke'],
    'wear': ['wore', 'worn'],
    'win': ['won'],
    'hide': ['hid', 'hidden'],
    'draw': ['drew', 'drawn'],
    'blow': ['blew', 'blown'],
    'know': ['knew', 'known'],
    'throw': ['threw', 'thrown'],
    'grow': ['grew', 'grown'],
    'fly': ['flew', 'flown'],
    'begin': ['began', 'begun'],
    'break': ['broke', 'broken'],
    'choose': ['chose', 'chosen'],
    'forget': ['forgot', 'forgotten'],
    'freeze': ['froze', 'frozen'],
    'steal': ['stole', 'stolen'],
    'swim': ['swam', 'swum'],
    'ride': ['rode', 'ridden'],
    'rise': ['rose', 'risen'],
    'drive': ['drove', 'driven'],
    'sell': ['sold'],
    'tell': ['told'],
    'feed': ['fed'],
    'lead': ['led'],
    'mean': ['meant'],
    'cost': ['cost'],
    'hurt': ['hurt'],
    'shut': ['shut'],
    'let': ['let'],
    'set': ['set'],
}


def _has_word(sent, w):
    """例句/造句里有没有真的用上这个词——容许常见变形：
       复数、三单、过去式、ing、比较级最高级（tall→taller/tallest）、不规则动词（catch→caught）"""
    base = _norm(w)
    if not base:
        return True
    S = ' ' + _norm(sent) + ' '
    if ' ' in base:
        # 词组：第一个词可以变形（turn on → turned on / turns on / turning on）
        head, tail = base.split(' ', 1)
        hs = re.sub(r'[ey]$', '', head)
        heads = {head, head + 's', head + 'es', head + 'ed', head + 'ing',
                 hs + 'ing', hs + 'ed', hs + 'ies', hs + 'ied'} | set(IRREGULAR.get(head, []))
        return any((' ' + h + ' ' + tail + ' ') in S for h in heads)
    stem_e = re.sub(r'e$', '', base)          # like → lik(ing)
    stem_y = re.sub(r'y$', '', base)          # happy → happ(ier)
    forms = {base, base+'s', base+'es', base+'d', base+'ed', base+'ing',
             base+'er', base+'est',                       # 比较级/最高级
             stem_e+'ing', stem_e+'ed', stem_e+'er', stem_e+'est',
             stem_y+'ies', stem_y+'ied', stem_y+'ier', stem_y+'iest',
             base+base[-1]+'er', base+base[-1]+'est',      # big → bigger/biggest
             base+base[-1]+'ing', base+base[-1]+'ed'}      # stop → stopping/stopped
    forms.update(IRREGULAR.get(base, []))
    return any((' ' + f + ' ') in S for f in forms)


def _too_similar(a, b):
    A, B = _norm(a), _norm(b)
    if not A or not B:
        return False
    if A == B:
        return True
    ta, tb = A.split(' '), B.split(' ')
    inter, uni = len(set(ta) & set(tb)), len(set(ta) | set(tb))
    return uni > 0 and inter / uni >= 0.8


def validate(data):
    errs = []
    seen_uid, seen_sid = set(), set()
    seen_word = {}
    for u in data['units']:
        if u['id'] in seen_uid:
            errs.append('单元 id 重复：%s' % u['id'])
        seen_uid.add(u['id'])
        if not u['sections']:
            errs.append('%s 没有任何节' % u['id'])
        for s in u['sections']:
            sid = s['id']
            if sid in seen_sid:
                errs.append('节 id 重复：%s' % sid)
            seen_sid.add(sid)
            if not s['words']:
                errs.append('%s 没有任何单词' % sid)
            for i, w in enumerate(s['words']):
                where = '%s/%s' % (sid, w.get('w', '#%d' % i))
                for k in ('w', 'ipa', 'pos', 'zh', 'lesson', 'egs'):
                    if k not in w or w[k] in (None, '', []):
                        errs.append('%s 缺字段 %s' % (where, k))
                if 'w' not in w:
                    continue
                # 同一个词不要在两节里重复收（孩子会觉得在做重复功课）
                key = _norm(w['w'])
                if key in seen_word:
                    errs.append('单词「%s」重复收录：%s 与 %s' % (w['w'], seen_word[key], where))
                seen_word[key] = where
                # ⭐ 背诵模式只给中文让孩子写英文——释义里若混着英文原词，答案就直接白送了
                if _norm(w['w']) and (' ' + _norm(w['w']) + ' ') in (' ' + _norm(w['zh']) + ' '):
                    errs.append('%s：中文释义里出现了英文原词「%s」，背诵时会直接泄露答案（%s）'
                                % (where, w['w'], w['zh']))
                if not isinstance(w.get('lesson'), int) or not (1 <= w['lesson'] <= 144):
                    errs.append('%s 的 lesson 要是 1..144 的整数' % where)
                egs = w.get('egs')
                if not isinstance(egs, list) or len(egs) != EGS_REQUIRED:
                    errs.append('%s：egs 要正好 %d 句' % (where, EGS_REQUIRED))
                    continue
                for k, e in enumerate(egs):
                    nw = len(str(e).strip().split())
                    if nw < EGS_MIN_WORDS:
                        errs.append('%s 例句%d：只有 %d 个单词，要 ≥%d（%s）' % (where, k+1, nw, EGS_MIN_WORDS, e))
                    if not _has_word(e, w['w']):
                        errs.append('%s 例句%d：没有用上这个词（%s）' % (where, k+1, e))
                    if not str(e).strip()[:1].isupper():
                        errs.append('%s 例句%d：句首要大写（%s）' % (where, k+1, e))
                    if str(e).strip()[-1:] not in '.!?':
                        errs.append('%s 例句%d：句尾要有标点（%s）' % (where, k+1, e))
                for a in range(len(egs)):
                    for b in range(a + 1, len(egs)):
                        if _too_similar(egs[a], egs[b]):
                            errs.append('%s：例句%d 和 例句%d 太像，要三个不同的句子' % (where, a+1, b+1))
    return errs


def main():
    errs = validate(DATA)
    if errs:
        print('❌ 体检未通过，共 %d 项：' % len(errs))
        for e in errs:
            print('   -', e)
        sys.exit(1)

    tpl = open(os.path.join(HERE, 'words_template.html'), encoding='utf-8').read()
    assert tpl.count('/*__DATA__*/') == 1, '模板占位符缺失或重复'
    js = json.dumps(DATA, ensure_ascii=False).replace('</', '<\\/')
    out = tpl.replace('/*__DATA__*/', js)
    path = os.path.join(ROOT, 'words.html')
    open(path, 'w', encoding='utf-8').write(out)

    n_u = len(DATA['units'])
    n_s = sum(len(u['sections']) for u in DATA['units'])
    n_w = sum(len(s['words']) for u in DATA['units'] for s in u['sections'])
    lessons = sorted({w['lesson'] for u in DATA['units'] for s in u['sections'] for w in s['words']})
    print('✅ 体检全部通过')
    print('   已生成 %s（%d 字符 / %d 字节）' % (path, len(out), len(out.encode('utf-8'))))
    print('   %d 单元 / %d 节 / %d 个单词 / %d 个例句' % (n_u, n_s, n_w, n_w * EGS_REQUIRED))
    print('   覆盖课次：Lesson %d–%d（共 %d 课有收词）' % (lessons[0], lessons[-1], len(lessons)))


if __name__ == '__main__':
    main()
