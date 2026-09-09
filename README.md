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
| `words.html` | 新概念第一册 · 单词 6 单元 32 节 601 词（记忆 / 背诵 / 造句） | `build/words_data.py` + `build/words_u1..u6.py` |
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
node   build/tests_native.js  # 中式英语搭配表 + 课本例句推荐（零误报）
python3 build/tests_click.py  # 真点击端到端走查（需要 playwright）
```

## 一次改完要跑的全套

```bash
python3 build/build_eng.py   && node build/test_eng.js
python3 build/build_words.py && node build/tests_words.js && node build/tests_grammar.js
node    build/tests_autofix.js          # 写错时的自动改正
node    build/tests_native.js           # 写错时的地道说法（不依赖 AI Key）
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

### 写错时：直接给出改好的句子

规则查到的错会**自动应用**，把改好的完整句子摆在孩子面前（`autoFix`）——
他看不懂「三单要加 s」也能照着抄一遍，边抄边记。
覆盖：三单加 s（含 have→has）、动词还原（含 went→go）、a/an、物主代词、be 动词匹配、
不规则过去式、There is→are、双重否定、very 位置、重复词、连词重复、大小写、句尾标点。
`tests_autofix.js` 两半都测：17 条错句要改对，7 条正确句一个字都不能被改动。

### 写错时：同一时间给「欧美人平常会怎么说」

⭐ **不能让孩子「改对了才配看母语者怎么说」** —— 他最想知道地道说法的时刻，就是刚写错那一刻。
所以写错的反馈是三段：**错在哪 → 改好长这样 → 同样的意思欧美人会这样说**。

## ⭐ 判分分层：能百分之百确定的，一律不调 AI

孩子没有判断能力，所以结论必须尽量来自**测过的确定性规则**，而不是概率模型。
`makeCheck()` 按这个顺序判，**前三层任何一层有话说，就地给结论并 return，根本不调 AI**：

| 层 | 判什么 | 怎么保证对 | 调 AI？ |
|---|---|---|---|
| ① 语法 | 主谓一致 / 时态 / 冠词 / 双重否定 / 大小写标点… | `checkGrammar` + `autoFix`，错句 33/33 抓到、正确句零误报、全册 1803 例句零误判 | ❌ |
| ② 意思说不通 | 吃书、喝桌子这类（`senseHits`） | 查表：只放明确无生命非食物的名词，动物植物一律不放 | ❌ |
| ③ 说法不地道 | 23 条中式英语搭配（`COLLOC`） | 每条自带 `fix()`＋`exp`，测试断言「改出来 = exp、改完不再命中、改好的句子自己过语法检查」 | ❌ |
| ④ 语义 / 地道度 | 前三层都没话说时剩下的那一小块 | 规则做不到，只能靠 AI；且 AI 输出仍要过本层 ① 的语法检查才显示 | ✅（可选） |

所以**不填 Key 也是完整可用的**：①②③ 全部照跑，页面会明说
「系统能确定的都查过了：语法、常见中式说法、意思说不通的搭配，全都没问题」。
没查的只有 ④ 那一小块（`I fly this excuse to school.` 这种语法对、搭配也不在表里的语义怪句）。

地道说法这一层的三个确定性来源：

| 来源 | 内容 | 一定给得出？ |
|---|---|---|
| `COLLOC` 中式英语搭配表（23 条） | `open the light→turn on`、`very like→really like`、`eat medicine→take medicine`、`arrive to→arrive at`、`I am boring→I am bored`、`everyday→every day`… 22 条能**自动改好整句** | 命中才给 |
| `w.native` 常用句型 | 部分词额外配的「母语者习惯句型 + 例句 + 提示」，比课本原句更有针对性 | 优先给 |
| `closestEg` 课本原句 | 没配 `native` 的词退回这里：从该词 3 个例句里挑**和孩子那句共同词最多**的一句 —— 课本例句是母语者写的，且建置时全过检查器 | ✅ 兜底，两者必有其一 |

⭐ 回显的必须是**孩子自己句子里命中的那一段**（`hitText`）。他写的是 excuse，
你却拿规则表里的 `I very like this book.` 给他看，他只会更糊涂 —— 这条也焊进了测试。

`COLLOC` / `senseHits` 的铁律和语法检查器一样：**宁可漏报，不可误报**。每条都把词限死 ——
`open` 只在 light / TV / radio 这类电器上报，`open the door`、`open the book` 绝不能被判；
`I am boring` 只在主语是人称代词时报，`The film is boring.` 不报。

`tests_native.js` 七段都测：23 条规则各抓自己的反例、22 条 `fix()` 自证（改出来 = `exp`、
改完不再命中、改好的句子过语法检查）、38 条正常说法零误报、**全册 1803 个例句零误报**、
语义表 4 类反例全抓到、接线断言、**「规则已确定就不调 AI」的分支顺序断言**。

### 第 ④ 层：AI 检查（可选，只补规则做不到的那一小块）

前三层都没话说时才轮到它，做两件规则做不到的事：
① 判断**意思通不通、搭配对不对**（`I fly this excuse to school.` 这种语法对、也不在搭配表里的怪句；
   `I eat a book.` 这类已经被第 ② 层查表拦下，不用 AI）
② ⭐ **照着孩子那一句改写成母语者的说法** —— 同样的意思、同样的场合、仍用这个单词，
   并用一句话说清楚差在哪（哪个词换了／语序变了／换了更常用的搭配）。

- 首页 →「⚙️ 家长设置 · AI 检查」填智谱 API Key
  模型默认 **`glm-4.7-flash`**（智谱当前免费的主力模型，30B / 200K 上下文，2026-01 上线）；
  想更稳可换按量计费的 `glm-4-plus`
- ⭐ **AI 给的句子会先过一遍本地语法检查器，没通过就不显示** ——
  AI 会犯错、孩子看不出来，与其让他学到一句错的，不如这次少给一句。
  拦下时会明说原因，不会悄悄少一块。规则层是确定性的、测过的，用它给 AI 把关比信任 AI 可靠。
- **不填也能正常用** —— ①②③ 三层照跑（见上面的判分分层表），只有 ④ 那一小块查不出
- **只有前三层规则都没话说时才调 AI**；语法写错但规则没命中搭配表时也会调（拿 `autoFix` **改好的句子**去问，
  不拿错句去问，免得 AI 被语法错带偏）。AI 挂了/超时/Key 无效都不挡路，规则的结论照样完整
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
| `TEST003` 模块没有同名测试 | **不适用**。测试按功能命名（tests_grammar / tests_resume / tests_ai…），不按模块名，12 支覆盖到位。 |
| `DOC002` 找不到教程档 | **本文件就是**。体检只认特定文件名。 |

## 自查清单（每次改完照着走）

1. `python3 build/build_words.py` —— 体检不过就不生成文件
2. 12 支测试全绿（见上面「一次改完要跑的全套」）
3. `python3 scripts/project_audit.py .` —— **P0 必须为 0**
4. 真点击走查一遍（`tests_click.py` 已覆盖，改了 UI 要人工再点一次）
5. `git push` 之后 **curl 线上地址断言到新内容** —— 本机绿 ≠ 孩子能用
