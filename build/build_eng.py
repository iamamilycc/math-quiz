# -*- coding: utf-8 -*-
"""
功能：把 eng_data.py 的 DATA 注入 eng_template.html，产出 eng.html
输入：build/eng_data.py, build/eng_template.html
输出：eng.html（部署目录根下）
用法：python3 build/build_eng.py
校验：注入前先跑 validate()，任何一条不通过就中止，不写文件
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from eng_data import DATA

TAGS_OK = {"基础", "进阶", "易错"}


def validate(data):
    errs = []
    seen_cid, seen_sid = set(), set()
    for c in data["chapters"]:
        if c["id"] in seen_cid:
            errs.append("章 id 重复：%s" % c["id"])
        seen_cid.add(c["id"])
        if not c["sections"]:
            errs.append("%s 没有任何节" % c["id"])
        for s in c["sections"]:
            sid = s["id"]
            if sid in seen_sid:
                errs.append("节 id 重复：%s" % sid)
            seen_sid.add(sid)

            # --- 知识点深度标准 ---
            if len(s["notes"]) < 3:
                errs.append("%s 知识点少于 3 个（实际 %d）" % (sid, len(s["notes"])))
            for n in s["notes"]:
                where = "%s/%s" % (sid, n["point"])
                if len(n["examples"]) < 2:
                    errs.append("%s 例子少于 2 个" % where)
                tags = [e["tag"] for e in n["examples"]]
                for t in tags:
                    if t not in TAGS_OK:
                        errs.append("%s 例子标签非法：%s" % (where, t))
                if not any("易错" in t for t in tags):
                    errs.append("%s 缺少「易错」翻卡片例子" % where)
                if not n.get("think", "").strip():
                    errs.append("%s 缺少「想一想」" % where)
                if not n.get("explain", "").strip():
                    errs.append("%s 缺少 explain" % where)

            # --- 题目结构 ---
            qids = set()
            n_multi = 0
            for q in s["quiz"]:
                w = "%s/第%s题" % (sid, q["id"])
                if q["id"] in qids:
                    errs.append("%s id 重复" % w)
                qids.add(q["id"])
                for k in ("type", "point", "stem", "answer", "explain"):
                    if k not in q or q[k] in (None, "", []):
                        errs.append("%s 缺字段 %s" % (w, k))
                t = q["type"]
                if t in ("choice", "multi"):
                    if "options" not in q or len(q["options"]) < 3:
                        errs.append("%s 选项不足 3 个" % w)
                        continue
                    letters = [o[0] for o in q["options"]]
                    if letters != sorted(letters) or len(set(letters)) != len(letters):
                        errs.append("%s 选项字母不连续或重复：%s" % (w, letters))
                    for o in q["options"]:
                        if not re.match(r"^[A-Z]\. ", o):
                            errs.append("%s 选项未按「A. 内容」格式：%s" % (w, o[:20]))
                    if t == "choice":
                        if q["answer"] not in letters:
                            errs.append("%s 答案 %s 不在选项中" % (w, q["answer"]))
                    else:
                        n_multi += 1
                        if not isinstance(q["answer"], list):
                            errs.append("%s multi 的 answer 必须是数组" % w)
                        else:
                            if len(q["answer"]) < 2:
                                errs.append("%s 多选题答案少于 2 项，应改为单选" % w)
                            if len(q["answer"]) == len(letters):
                                errs.append("%s 多选题全选即对，缺少干扰项" % w)
                            for a in q["answer"]:
                                if a not in letters:
                                    errs.append("%s 答案 %s 不在选项中" % (w, a))
                elif t == "judge":
                    if q["answer"] not in ("对", "错"):
                        errs.append("%s judge 答案必须是「对」或「错」" % w)
                elif t == "fill":
                    if not isinstance(q["answer"], list) or not q["answer"]:
                        errs.append("%s fill 的 answer 必须是非空数组" % w)
                    else:
                        for a in q["answer"]:
                            # 判分会 strip 空白并转小写；含撇号的答案在 iPad 上易被智能引号替换
                            if "'" in a or "’" in a:
                                errs.append("%s fill 答案含撇号，iPad 智能引号会误判：%s" % (w, a))
                else:
                    errs.append("%s 未知题型：%s" % (w, t))

            # --- 深度标准：每个「想一想」配一道多选题 ---
            if n_multi < len(s["notes"]):
                errs.append("%s 多选题 %d 道，少于知识点数 %d（每个想一想应配一道）"
                            % (sid, n_multi, len(s["notes"])))
    return errs


def main():
    errs = validate(DATA)
    if errs:
        print("❌ 体检未通过，共 %d 项：" % len(errs))
        for e in errs:
            print("   -", e)
        sys.exit(1)

    tpl = open(os.path.join(HERE, "eng_template.html"), encoding="utf-8").read()
    assert tpl.count("/*__DATA__*/") == 1, "模板占位符缺失或重复"
    js = json.dumps(DATA, ensure_ascii=False)
    # </script> 出现在字符串里会提前闭合 script 标签
    js = js.replace("</", "<\\/")
    out = tpl.replace("/*__DATA__*/", js)

    path = os.path.join(ROOT, "eng.html")
    open(path, "w", encoding="utf-8").write(out)

    n_c = len(DATA["chapters"])
    n_s = sum(len(c["sections"]) for c in DATA["chapters"])
    n_n = sum(len(s["notes"]) for c in DATA["chapters"] for s in c["sections"])
    n_q = sum(len(s["quiz"]) for c in DATA["chapters"] for s in c["sections"])
    print("✅ 体检全部通过")
    print("   已生成 %s（%d 字符 / %d 字节）" % (path, len(out), len(out.encode("utf-8"))))
    print("   %d 章 / %d 节 / %d 个知识点 / %d 道题" % (n_c, n_s, n_n, n_q))


if __name__ == "__main__":
    main()
