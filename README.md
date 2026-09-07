# 七年级学习测验站

> **完成的定义**：跑过（真实命令输出）＋ 有证据（测试全绿）＋ 文档同步 ＋ 同类位置都改了 ＋ push 后验过线上 URL。
> 本机绿 ≠ 孩子能用 —— 每次改动必须 curl 线上地址断言到新内容才算完成。

线上： https://iamamilycc.github.io/math-quiz/

## 科目

| 页面 | 内容 | 数据源 |
|---|---|---|
| `math.html` | 数学 北师大版七上 | 手写 |
| `geo.html` | 地理 湘教版七上 | 手写 |
| `bio.html` | 生物 人教版七上 | 手写 |
| `eng.html` | 新概念第一册 · 考点测验（7 章 506 题） | `build/eng_data.py` + `build/eng_c2..c7.py` |
| `words.html` | 新概念第一册 · 单词（记忆 / 背诵 / 造句） | `build/words_data.py` + `build/words_u*.py` |
| `wrongbook.html` | 各科错题本（localStorage） | — |

## 改内容怎么改

**只改数据文件，不要手改生成的 html。**

```bash
# 英语考点测验
vi build/eng_c3.py            # 改哪一章就改哪个文件
python3 build/build_eng.py    # 体检 + 生成 eng.html（体检不过不生成）
node   build/test_eng.js      # 闭环测试

# 英语单词
vi build/words_u1.py          # 改哪个单元就改哪个文件
python3 build/build_words.py  # 体检 + 生成 words.html
node   build/tests_words.js   # 数据与页面断言
node   build/tests_grammar.js # 造句语法检查器（错句必抓 / 正确句零误报）
python3 build/tests_click.py  # 真点击端到端走查（需要 playwright）
```

## 一次改完要跑的全套

```bash
python3 build/build_eng.py   && node build/test_eng.js
python3 build/build_words.py && node build/tests_words.js && node build/tests_grammar.js
python3 build/tests/audit_eng.py        # 英语题库深度自审
node    build/tests/walkthrough_eng.js  # 使用者视角走查
python3 build/tests/inject_rules.py     # 故障注入：确认建置规则真的会变红
python3 build/tests_click.py            # 单词模块真点击走查
```

## 内容规则（已焊成建置断言，不过就不生成文件）

**为什么这么严：孩子没有判断能力。给他的内容错了，他会照着学下去。**

- 每个单词必须配 **3 个例句**，每句 **≥5 个单词**、必须真的用上该词、句首大写句尾标点、三句互不重复
- 中文释义里 **不得出现该英文原词**（背诵模式只给中文，写进去等于白送答案）
- 测验题：单选答案不得集中在某个字母（>40% 就挡）、同一节判断题不得答案全同
- 错题本去重键 `subject|point|stem` 必须全局唯一（否则两道题会被合并成一题）
- 判正误的题，判错理由必须是**语法错误**；只是「不地道」不能算错，要考语用就把题干写成「最合适的说法是」

## 造句怎么判分

`words.html` 内建**规则式英语语法检查器**（不依赖任何 AI Key）。孩子写完按「检查」，系统直接给结论：
通过，或者列出**哪几处错、错在哪、怎么改**。

覆盖：主谓一致（三单加 s / be 动词匹配）、时态标记冲突（do/does/did 后要原形）、情态动词后原形、
冠词 a/an、双重否定、very 修饰动词、although+but、because+so、物主代词误用、重复词、大小写、句尾标点、有没有动词。

设计原则：**宁可漏报，不可误报** —— 把对的句子判成错，比漏掉一个错更伤（孩子会把对的当错的记）。
`tests_grammar.js` 两半都测：错句必须被抓到，正确句必须零误报，且全册例句一条都不能被判错。

## 依赖

- Python 3（只用标准库）
- Node.js（跑 `.js` 测试）
- `playwright`（只有 `tests_click.py` 需要；没装就跳过这一支）

## 备份

代码即备份：全部内容在 git 里，远端 `github.com/iamamilycc/math-quiz`。
数据源都是纯文本（`build/*.py`），生成物 `*.html` 随时可重建。
