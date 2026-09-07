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
python3 build/tests_ai.py               # AI 第二层（mock 拦 fetch，不需要真 Key）
python3 build/tests_parity.py           # 建置端与造句端的用词规则必须一致
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

### 第二层：AI 检查（可选，补规则做不到的部分）

规则查语法，AI 查**意思通不通、搭配对不对**（例如 `I eat a book every day.` 语法没错但意思荒谬）。

- 首页 →「⚙️ 家长设置 · AI 检查」填智谱 API Key（模型默认免费的 `glm-4-flash`）
- **不填也能正常用** —— 规则层的结论照样有效，只是查不出语义问题
- **语法层没过就不调 AI**（省额度），AI 挂了/超时/Key 无效都不挡路，语法结论仍然有效
- AI 可能误判，所以留了「我觉得这句没问题，收下」的人工出口
- 🔒 **Key 只存在设备的 localStorage**，不进代码、不进仓库、只发给智谱本身。
  同一台设备上任何人都能在设置里看到它 —— 孩子的设备请用额度有限的 Key。
- `tests_ai.py` 用 mock 拦 fetch 验证全部路径（通过 / 判错 / 500 / 401 / 无 Key / 不浪费调用）

## 依赖

- Python 3（只用标准库）
- Node.js（跑 `.js` 测试）
- `playwright`（只有 `tests_click.py` 需要；没装就跳过这一支）

## 备份

代码即备份：全部内容在 git 里，远端 `github.com/iamamilycc/math-quiz`。
数据源都是纯文本（`build/*.py`），生成物 `*.html` 随时可重建。


## 体检 P1 的判定（已逐条确认，不是漏掉）

| 项目 | 判定 |
|---|---|
| `ARCH001` words.html 916 行超过 800 | **接受**。自包含单页应用，分了「基础／语法检查器／AI 层／路由／三种练法」五区，改哪块很清楚。语法检查器（约 280 行）将来若要给别的项目复用，再抽成 `assets/grammar-en.js`。 |
| `BAK001` 找不到备份脚本 | **不适用**。内容全是纯文本 `build/*.py`，git + GitHub 就是备份，生成物随时可重建。 |
| `SET001` 有上传缺导出 | **误报**。错题本有「📋 复制错题清单」导出。 |
| `TEST003` 模块没有同名测试 | **不适用**。测试按功能命名（tests_grammar / tests_resume / tests_ai…），不按模块名，10 支覆盖到位。 |
| `DOC002` 找不到教程档 | **本文件就是**。体检只认特定文件名。 |

## 自查清单（每次改完照着走）

1. `python3 build/build_words.py` —— 体检不过就不生成文件
2. 10 支测试全绿（见上面「一次改完要跑的全套」）
3. `python3 scripts/project_audit.py .` —— **P0 必须为 0**
4. 真点击走查一遍（`tests_click.py` 已覆盖，改了 UI 要人工再点一次）
5. `git push` 之后 **curl 线上地址断言到新内容** —— 本机绿 ≠ 孩子能用
