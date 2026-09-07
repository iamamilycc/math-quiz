# -*- coding: utf-8 -*-
"""第七章 语法专题总复习：跨课次整合 · 综合辨析"""

s1 = {
    "id": "e-c7-s1",
    "title": "专题一 时态总表：六大时态一次辨清",
    "notes": [
        {
            "point": "六大时态形状对照表",
            "explain": "把第一册的六个时态放在一起对比，每个时态记住三件事：<b>长什么样、什么时候用、配什么标志词</b>。",
            "examples": [
                {"tag": "基础", "text": "一般现在时 <b>do/does</b>（习惯、真理｜every day, always）／ 现在进行时 <b>am/is/are doing</b>（此刻正在｜now, Look!）／ 一般过去时 <b>did</b>（过去发生｜yesterday, ago）"},
                {"tag": "进阶", "text": "过去进行时 <b>was/were doing</b>（过去某刻正在｜at 8 last night, when…）／ 现在完成时 <b>have/has done</b>（对现在有影响｜already, just, since, for）／ 一般将来时 <b>will do / be going to do</b>（将要发生｜tomorrow, next week）"},
                {"tag": "易错", "text": "六个时态里，只有<b>现在完成时</b>横跨过去和现在两个时间段，也只有它<b>不能配确切的过去时间</b>。这个特点是它最难也最常考的原因。"}
            ],
            "think": "六个时态里，有三个用到了 be 动词（进行时两个、被动语态），有两个用到了助动词 do/did，一个用 have —— 你能画一张“谁负责什么信息”的图吗？"
        },
        {
            "point": "最容易混的三组时态",
            "explain": "考试真正会考的，就是这三组的分界线。",
            "examples": [
                {"tag": "基础", "text": "<b>组一：一般现在 vs 现在进行</b>。分界是“经常”还是“此刻”：I <b>watch</b> TV every evening.（习惯）／ I <b>am watching</b> TV now.（此刻）"},
                {"tag": "进阶", "text": "<b>组二：一般过去 vs 现在完成</b>。分界是<b>有没有确切过去时间</b>：I <b>saw</b> him yesterday. ✓ / I <b>have seen</b> him.（没说时间）✓ / I have seen him yesterday. ✗<br><b>组三：一般过去 vs 过去进行</b>。分界是“瞬间”还是“背景”：When I <b>came</b> in（瞬间）, he <b>was reading</b>（背景）."},
                {"tag": "易错", "text": "组二是失分重灾区。记死一条：<b>看到 yesterday / last… / …ago / in + 过去年份，一律用过去时，不许用完成时</b>。这一条能解决大半的时态选择题。"}
            ],
            "think": "三组辨析里，两组的分界线都和“时间是不是明确”有关 —— 英语的时态系统似乎特别在意“说话人站在什么时间点看这件事”，你同意吗？"
        },
        {
            "point": "从句的时态规则（两条）",
            "explain": "从句不能随便选时态，有两条硬规则：<b>主将从现</b>和<b>时态呼应</b>。",
            "examples": [
                {"tag": "基础", "text": "<b>主将从现</b>：when / if / before / after / as soon as / until 引导的从句里，用一般现在时代替将来时：I will call you when he <b>comes</b>.（不是 will come）"},
                {"tag": "进阶", "text": "<b>时态呼应</b>：主句是过去时（said、told、asked），从句要退一格：He said he <b>was</b> busy. / He said he <b>would</b> come. 但如果从句说的是<b>客观真理</b>，可以不退：The teacher said the earth <b>is</b> round."},
                {"tag": "易错", "text": "两条规则容易串：<b>主将从现管的是将来</b>（if 从句不用 will），<b>时态呼应管的是过去</b>（said 后面退一格）。做题先看主句是将来还是过去，再决定用哪条。"}
            ],
            "think": "老师说“地球是圆的”，转述时可以不退格 —— 这个例外说明时态呼应背后的真正逻辑是什么？"
        },
        {
            "point": "时态选择五步流程（可直接照做）",
            "explain": "① 找<b>时间状语</b> → ② 找 <b>Look! / Listen!</b> → ③ 看是不是<b>从句</b>（用哪条从句规则）→ ④ 看<b>上下文其他动词</b>的时态 → ⑤ 看<b>动词本身</b>（状态动词不用进行时）。",
            "examples": [
                {"tag": "基础", "text": "例：He ______ (read) a book when I came in. → 有 when + came（过去），说的是背景动作 → <b>过去进行时</b> → was reading"},
                {"tag": "进阶", "text": "例：I ______ (know) him since 2016. → since 提示完成时，但 know 是<b>状态动词</b>不用进行时 → <b>have known</b>（不是 have been knowing）。第五步专门管这种情况。"},
                {"tag": "易错", "text": "五步里最容易跳过的是<b>第四步（看上下文）</b>。很多题根本没有时间状语，全靠前后句的动词时态推断：He opened the door. A man <b>was standing</b> outside."}
            ],
            "think": "这套五步流程，你觉得哪一步在实际考试中用得最多？如果只能记住一步，你会记哪一步？"
        },
        {
            "point": "各时态的疑问与否定速查",
            "explain": "变疑问否定时，永远先问一句：<b>句子里有没有 be 动词、情态动词或助动词</b>？有就动它；没有才请 do / does / did 出场。",
            "examples": [
                {"tag": "基础", "text": "<b>有 be</b>：He is here. → Is he here? / He isn’t here.<br><b>有情态</b>：He can swim. → Can he swim? / He can’t swim.<br><b>有 have（完成时）</b>：He has gone. → Has he gone? / He hasn’t gone."},
                {"tag": "进阶", "text": "<b>都没有</b>：He likes tea. → Does he <b>like</b> tea? / He doesn’t <b>like</b> tea.（现在时）／ He went. → Did he <b>go</b>? / He didn’t <b>go</b>.（过去时）—— 动词一律还原成原形。"},
                {"tag": "易错", "text": "两个高频错：① 句中已有 be 还请 do（He doesn’t <u>be</u> ✗）② 请了 do 却不还原动词（Does he <u>likes</u> ✗ / Did he <u>went</u> ✗）。这两个错各占一半失分。"}
            ],
            "think": "“有 be 用 be，无 be 才用 do”和“一个句子只能有一个时态标记”，其实是同一条原则的两面 —— 你能用一句话把它们合并起来吗？"
        }
    ],
    "quiz": [
        {"id": 1, "type": "multi", "point": "六大时态标志词（想一想·刁钻）",
         "stem": "下列配对<b>正确</b>的有（　）【多选】",
         "options": ["A. every day — 一般现在时", "B. at 8 last night — 过去进行时",
                     "C. since 2016 — 现在完成时", "D. next week — 一般将来时",
                     "E. two days ago — 现在完成时"],
         "answer": ["A", "B", "C", "D"],
         "explain": "只有 E 错：<b>…ago 是确切过去时间，配一般过去时</b>，绝不能配现在完成时。这是全册最高频的时态失分点。"},
        {"id": 2, "type": "multi", "point": "完成时与过去时的分界·总复习（想一想·刁钻）",
         "stem": "下列句子<b>正确</b>的有（　）【多选】",
         "options": ["A. I have finished my homework.", "B. I have finished my homework last night.",
                     "C. I finished my homework last night.", "D. He has lived here for ten years.",
                     "E. He has come here in 2016."],
         "answer": ["A", "C", "D"],
         "explain": "B、E 都把<b>确切过去时间</b>（last night、in 2016）配了完成时。记死：看到 yesterday / last… / …ago / in + 过去年份，一律用过去时。"},
        {"id": 3, "type": "multi", "point": "从句时态两条规则（想一想·刁钻）",
         "stem": "下列句子<b>正确</b>的有（　）【多选】",
         "options": ["A. I will call you when he comes.", "B. I will call you when he will come.",
                     "C. He said he was busy.", "D. He said he is busy.",
                     "E. The teacher said the earth is round."],
         "answer": ["A", "C", "E"],
         "explain": "A 用了<b>主将从现</b>（B 错）。C 用了<b>时态呼应</b>（D 错）。E 是时态呼应的<b>例外</b>：从句说的是客观真理，可以不退格。"},
        {"id": 4, "type": "multi", "point": "状态动词不用进行时（想一想·刁钻）",
         "stem": "下列句子<b>正确</b>的有（　）【多选】",
         "options": ["A. I have known him since 2016.", "B. I have been knowing him since 2016.",
                     "C. I like this book.", "D. I am liking this book.",
                     "E. I am having lunch."],
         "answer": ["A", "C", "E"],
         "explain": "know、like 是<b>状态动词，不用进行时</b>（B、D 错）。E 对：have 表示“吃”时是动作动词，可以用进行时。这是时态五步流程的第五步管的情况。"},
        {"id": 5, "type": "multi", "point": "疑问否定的变法（想一想·刁钻）",
         "stem": "下列句子<b>正确</b>的有（　）【多选】",
         "options": ["A. Does he like tea?", "B. Does he likes tea?", "C. Did he go home?",
                     "D. Did he went home?", "E. Has he gone?"],
         "answer": ["A", "C", "E"],
         "explain": "<b>助动词一出现，主要动词必须还原成原形</b>（B、D 都没还原）。E 对：完成时的 has 本身就是助动词，直接提到句首即可。"},
        {"id": 6, "type": "choice", "point": "上下文判断时态",
         "stem": "He opened the door. A man ______ outside in the rain.",
         "options": ["A. stands", "B. is standing", "C. was standing", "D. has stood"],
         "answer": "C",
         "explain": "句中<b>没有时间状语</b>，靠上下文判断：前句 opened 是过去时；“站着”是持续的背景状态，用<b>过去进行时</b>。这是五步流程第四步的典型题。"},
        {"id": 7, "type": "choice", "point": "主将从现",
         "stem": "We will go on a picnic if it ______ tomorrow.",
         "options": ["A. doesn’t rain", "B. won’t rain", "C. isn’t raining", "D. didn’t rain"],
         "answer": "A",
         "explain": "<b>if 引导的条件从句用一般现在时代替将来时</b>。虽然有 tomorrow，从句里也不能用 will，要用 doesn’t rain。"},
        {"id": 8, "type": "choice", "point": "过去进行时",
         "stem": "—What ______ you ______ at nine last night?　—I was watching TV.",
         "options": ["A. did, do", "B. are, doing", "C. were, doing", "D. have, done"],
         "answer": "C",
         "explain": "at nine last night 指<b>过去某个具体时刻</b>，问那时正在做什么，用<b>过去进行时</b>；答句 was watching 也印证了这一点。"},
        {"id": 9, "type": "fill", "point": "时态综合",
         "stem": "用 be 的正确形式填空：He ______ ill since last Monday.（填两个词）",
         "answer": ["has been"],
         "explain": "since 提示<b>现在完成时</b>；主语 He 三单用 has；be 的过去分词是 been。答案 has been。注意不能填 was（那样就和 since 冲突了）。"},
        {"id": 10, "type": "fill", "point": "主将从现",
         "stem": "用 arrive 的正确形式填空：I will tell him as soon as he ______.（填一个词）",
         "answer": ["arrives"],
         "explain": "as soon as 引导时间状语从句，<b>用一般现在时代替将来时</b>；主语 he 三单，所以是 arrives。"},
        {"id": 11, "type": "judge", "point": "完成时的时间限制",
         "stem": "现在完成时可以和 yesterday、last week 这类确切过去时间连用。",
         "answer": "错",
         "explain": "错。<b>现在完成时绝不能配确切的过去时间</b>，因为完成时关注“到现在为止”，而这些词把时间钉死在过去，两者视角冲突。有确切过去时间就用一般过去时。"},
        {"id": 12, "type": "judge", "point": "有 be 用 be",
         "stem": "变疑问句和否定句时，要先看句中有没有 be 动词、情态动词或助动词，有就动它们，没有才用 do/does/did。",
         "answer": "对",
         "explain": "对。这是英语句法最核心的规则之一。它和“<b>一个句子只能有一个时态标记</b>”是同一条原则的两面：谁承担了时态信息，就由谁负责变疑问和否定。"}
    ]
}

s2 = {
    "id": "e-c7-s2",
    "title": "专题二 名词 · 冠词 · 数量词",
    "notes": [
        {
            "point": "名词复数规则总表",
            "explain": "① 一般加 <b>s</b>；② s/x/sh/ch 结尾加 <b>es</b>；③ 辅音+y 变 i 加 <b>es</b>；④ f/fe 结尾变 <b>ves</b>；⑤ o 结尾：有生命加 es，无生命加 s；⑥ <b>不规则</b>单独记。",
            "examples": [
                {"tag": "基础", "text": "book→books ／ box→boxes、watch→watches ／ study→studies ／ knife→knives、leaf→leaves ／ potato→potatoes、photo→photos"},
                {"tag": "进阶", "text": "不规则四类：<b>元音变化</b>（man→men, foot→feet, tooth→teeth, mouse→mice）／ <b>加 ren</b>（child→children）／ <b>单复同形</b>（sheep, fish, deer, Chinese）／ <b>天生复数</b>（trousers, glasses, shoes）。"},
                {"tag": "易错", "text": "o 结尾的口诀是“<b>英雄爱吃西红柿土豆</b>”（hero, tomato, potato 加 es），其余无生命的加 s（photo, piano, radio, zoo）。这是唯一需要“分生命”的复数规则。"}
            ],
            "think": "英语的复数规则有六条，中文却几乎不区分单复数（“三本书”里“书”不变）—— 你觉得哪种方式更省事？各有什么代价？"
        },
        {
            "point": "可数与不可数名词",
            "explain": "<b>不可数名词</b>没有复数、不能直接加数字、配单数动词。要计数得用 <b>数词 + 单位 + of</b>。",
            "examples": [
                {"tag": "基础", "text": "常见不可数：water, milk, tea, coffee, bread, rice, meat, sugar, money, news, information, advice, furniture, luggage, homework, work, weather。"},
                {"tag": "进阶", "text": "计数方式：a <b>piece of</b> bread / paper / advice / news、a <b>cup of</b> tea、a <b>glass of</b> water、a <b>bottle of</b> milk、a <b>bowl of</b> rice。<b>变复数变的是单位</b>：two <b>pieces</b> of bread。"},
                {"tag": "易错", "text": "几个看起来像复数其实不可数的：<b>news</b>（新闻，The news is good.）、<b>clothes</b>（衣服，反过来永远是复数）、<b>hair</b>（整头头发不可数）、<b>fish</b>（鱼肉不可数，鱼可数）。这几个每次考试都出现。"}
            ],
            "think": "英语把 advice（建议）、information（信息）算作不可数，中文却说“三条建议、两个信息”—— 英语判断可数不可数的标准到底是什么？"
        },
        {
            "point": "冠词 a / an / the 与零冠词",
            "explain": "<b>a/an</b> 表示“一个（泛指）”，用于单数可数名词；<b>the</b> 表示“特指”（双方都知道是哪个）；<b>零冠词</b>（不加）用于复数泛指、不可数名词泛指、专有名词、三餐、球类、学科。",
            "examples": [
                {"tag": "基础", "text": "a book（一本书）／ an apple、an hour（看<b>读音</b>不看字母）／ the book（那本书）／ Books are useful.（泛指，零冠词）"},
                {"tag": "进阶", "text": "the 的四种用法：① 第二次提到（I saw a dog. <b>The</b> dog was black.）② 双方都知道（Open <b>the</b> door.）③ 世上独一无二（<b>the</b> sun, <b>the</b> moon）④ 最高级前（<b>the</b> tallest）。"},
                {"tag": "易错", "text": "a/an 的判断看<b>读音</b>不看字母：<b>an</b> hour（h 不发音）／ <b>a</b> university（读音以 /j/ 开头）／ <b>an</b> honest man ／ <b>a</b> useful book。光看首字母是元音字母就填 an，会错一半。"}
            ],
            "think": "中文完全没有冠词，说“我是老师”就够了，英语必须说 I’m <b>a</b> teacher —— 这个 a 到底提供了什么中文不需要的信息？"
        },
        {
            "point": "数量词对照表",
            "explain": "把所有表示数量的词按“配可数还是不可数”排成一张表，做题直接查。",
            "examples": [
                {"tag": "基础", "text": "<b>只配可数复数</b>：many, a few, few, several, a number of, How many<br><b>只配不可数</b>：much, a little, little, How much<br><b>都能配</b>：some, any, a lot of, lots of, plenty of, no"},
                {"tag": "进阶", "text": "语气差别：<b>a few / a little ＝ 有一些（肯定）</b>；<b>few / little ＝ 几乎没有（否定）</b>。记法：<b>有 a 是好消息，没 a 是坏消息</b>。"},
                {"tag": "易错", "text": "做这类题<b>两步走</b>：第一步看名词<b>可数不可数</b>（决定 many/much、few/little），第二步看句子<b>语气正负</b>（决定加不加 a）。两步都对才能选对。"}
            ],
            "think": "few 和 a few 只差一个字母，语气却完全相反 —— 如果你写作文时漏写这个 a，读者对你处境的理解会差多少？"
        },
        {
            "point": "名词所有格",
            "explain": "表示“谁的”：<b>单数加 ’s</b>（Tom’s book）；<b>复数以 s 结尾只加撇号</b>（the students’ books）；<b>复数不以 s 结尾仍加 ’s</b>（the children’s books）。无生命的东西通常用 <b>of</b>（the door of the room）。",
            "examples": [
                {"tag": "基础", "text": "Tom<b>’s</b> pen ／ my father<b>’s</b> car ／ the students<b>’</b> books ／ the children<b>’s</b> toys"},
                {"tag": "进阶", "text": "两人<b>共同拥有</b>只在最后一个名词后加 ’s：Tom and Jerry<b>’s</b> room（他俩合住一间）／ <b>各自拥有</b>各加各的：Tom<b>’s</b> and Jerry<b>’s</b> rooms（两间房）。一个撇号的位置改变了整句意思。"},
                {"tag": "易错", "text": "<b>代词所有格绝不加撇号</b>：its ✓ / it’s ✗（那是 it is）；yours ✓ / your’s ✗；theirs ✓ / their’s ✗。规则：名词所有格加撇号，代词所有格不加。"}
            ],
            "think": "Tom and Jerry’s room 是一间房，Tom’s and Jerry’s rooms 是两间 —— 一个撇号的位置就能表达“共有”还是“各有”，中文靠什么表达这个区别？"
        }
    ],
    "quiz": [
        {"id": 1, "type": "multi", "point": "名词复数规则（想一想·刁钻）",
         "stem": "下列复数形式<b>正确</b>的有（　）【多选】",
         "options": ["A. knives", "B. potatoes", "C. photoes", "D. children", "E. watches"],
         "answer": ["A", "B", "D", "E"],
         "explain": "只有 C 错：photo 是<b>无生命</b>的 o 结尾词，直接加 s → photos。口诀“<b>英雄爱吃西红柿土豆</b>”（hero/tomato/potato 加 es），其余加 s。"},
        {"id": 2, "type": "multi", "point": "不可数名词识别（想一想·刁钻）",
         "stem": "下列名词属于<b>不可数名词</b>的有（　）【多选】",
         "options": ["A. news", "B. advice", "C. suggestion", "D. information", "E. luggage"],
         "answer": ["A", "B", "D", "E"],
         "explain": "只有 C（suggestion 建议）可数，可以说 two suggestions。而 <b>advice</b> 表示同样的意思却不可数，要说 two <b>pieces of</b> advice。news 虽带 s 也是不可数。"},
        {"id": 3, "type": "multi", "point": "a 与 an 看读音（想一想·刁钻）",
         "stem": "下列冠词用得<b>正确</b>的有（　）【多选】",
         "options": ["A. an hour", "B. a hour", "C. a university", "D. an university", "E. an honest man"],
         "answer": ["A", "C", "E"],
         "explain": "<b>a/an 的判断看读音不看字母</b>：hour 的 h 不发音，读音以元音开头 → an；university 读音以 /j/ 开头（辅音）→ a；honest 的 h 也不发音 → an。"},
        {"id": 4, "type": "multi", "point": "数量词两步判断（想一想·刁钻）",
         "stem": "下列句子<b>正确</b>的有（　）【多选】",
         "options": ["A. I have a few friends here, so I’m not lonely.",
                     "B. I have few friends here, so I’m very lonely.",
                     "C. There is little water left, so we must save it.",
                     "D. There is a little water left, so we have nothing to drink.",
                     "E. How much money do you have?"],
         "answer": ["A", "B", "C", "E"],
         "explain": "只有 D 前后矛盾：a little ＝ 还有一点（肯定），和“没东西喝”冲突，应该用 little。<b>做题两步：先看可数不可数，再看语气正负</b>。"},
        {"id": 5, "type": "multi", "point": "所有格的撇号（想一想·刁钻）",
         "stem": "下列表达<b>正确</b>的有（　）【多选】",
         "options": ["A. Tom’s book", "B. the students’ books", "C. the children’s toys",
                     "D. its colour", "E. it’s colour"],
         "answer": ["A", "B", "C", "D"],
         "explain": "只有 E 错。规则：<b>名词所有格加撇号，代词所有格不加</b>。its ✓ / it’s ✗（那是 it is 的缩写）。同理 yours、theirs、hers 都不加撇号。"},
        {"id": 6, "type": "choice", "point": "不可数名词的量词",
         "stem": "The teacher gave me two ______ of advice.",
         "options": ["A. piece", "B. bags", "C. advices", "D. pieces"],
         "answer": "D",
         "explain": "advice 不可数，要用 <b>pieces of</b> 来数；two 是复数，所以 piece 加 s。注意 advice 本身永远不加 s。"},
        {"id": 7, "type": "choice", "point": "冠词的特指用法",
         "stem": "I saw a dog in the street. ______ dog was black and white.",
         "options": ["A. A", "B. An", "C. The", "D. 不填"],
         "answer": "C",
         "explain": "<b>第二次提到同一事物用 the</b>（特指）。第一次提到用 a（泛指），再提到时双方都知道说的是哪只狗了，改用 the。"},
        {"id": 8, "type": "choice", "point": "共有与各有",
         "stem": "This is ______ room. They live in it together.",
         "options": ["A. Tom’s and Jerry’s", "B. Tom and Jerry’s",
                     "C. Tom and Jerry", "D. Toms and Jerrys"],
         "answer": "B",
         "explain": "“他们一起住”说明是<b>共同拥有</b>，只在<b>最后一个名词后加 ’s</b>：Tom and Jerry’s room。如果各有一间要写 Tom’s and Jerry’s rooms。"},
        {"id": 9, "type": "fill", "point": "名词复数",
         "stem": "写出 leaf 的复数形式：______",
         "answer": ["leaves"],
         "explain": "以 f / fe 结尾的名词，复数要<b>变成 ves</b>：leaf→leaves、knife→knives、wife→wives、life→lives、half→halves。"},
        {"id": 10, "type": "fill", "point": "冠词",
         "stem": "填空：My uncle is ______ honest man.（填 a 或 an）",
         "answer": ["an"],
         "explain": "honest 的 <b>h 不发音</b>，读音以元音开头，所以用 <b>an</b>。判断 a/an 永远看读音，不看首字母是不是元音字母。"},
        {"id": 11, "type": "judge", "point": "news 的可数性",
         "stem": "news 以 s 结尾，所以它是复数名词，应该说 The news are good.",
         "answer": "错",
         "explain": "错。<b>news 是不可数名词</b>，永远配单数动词：The news <b>is</b> good. 同类“看着像复数其实不是”的还有 maths、physics、politics。反过来 clothes、trousers、glasses 才是真复数。"},
        {"id": 12, "type": "judge", "point": "代词所有格无撇号",
         "stem": "yours、theirs、its 这些代词所有格都不加撇号。",
         "answer": "对",
         "explain": "对。<b>名词所有格加撇号</b>（Tom’s、the dog’s），<b>代词所有格不加</b>（mine, yours, his, hers, its, ours, theirs）。凡是代词里带撇号的（it’s、you’re、they’re、who’s）都是<b>缩写</b>。"}
    ]
}

s3 = {
    "id": "e-c7-s3",
    "title": "专题三 代词全系统",
    "notes": [
        {
            "point": "人称代词与物主代词五列表",
            "explain": "英语的代词有五种形式，必须整行整行地背，做题时才能一眼对上。",
            "examples": [
                {"tag": "基础", "text": "<b>主格 / 宾格 / 形容词性物主 / 名词性物主 / 反身</b>：<br>I / me / my / mine / myself<br>you / you / your / yours / yourself<br>he / him / his / his / himself<br>she / her / her / hers / herself"},
                {"tag": "进阶", "text": "it / it / its / its / itself<br>we / us / our / ours / ourselves<br>you / you / your / yours / yourselves<br>they / them / their / theirs / themselves"},
                {"tag": "易错", "text": "三个陷阱：① <b>his 的四五列相同</b>（his book / This is his）② <b>her 的三四列不同</b>（her book / This is hers）③ <b>its 的三四列相同且不加撇号</b>。这三处每次考试都考。"}
            ],
            "think": "这张表里 you 一个词占了主格和宾格两列，he 却分成 he/him —— 英语在哪些人称上“偷懒”了？为什么偏偏是 you？"
        },
        {
            "point": "主格与宾格怎么选",
            "explain": "<b>主格</b>（I, he, she, we, they）作<b>主语</b>，放动词前面；<b>宾格</b>（me, him, her, us, them）作<b>宾语</b>，放动词或介词后面。",
            "examples": [
                {"tag": "基础", "text": "<b>He</b> gave <b>me</b> a book.（He 是主语用主格，me 是宾语用宾格）／ Give it to <b>him</b>.（介词 to 后面用宾格）"},
                {"tag": "进阶", "text": "并列时最容易错：<b>Tom and I</b> are friends.（作主语用 I）／ He gave the book to <b>Tom and me</b>.（作宾语用 me）。<b>检验方法：把另一个人去掉，只留代词读一遍</b>——“He gave the book to I” 明显别扭，就知道该用 me。"},
                {"tag": "易错", "text": "“<u>Me and Tom</u> are friends.” ✗ → <b>Tom and I</b> are friends. ✓ 而且英语习惯把自己放<b>后面</b>（Tom and I，不是 I and Tom），这是礼貌习惯。"}
            ],
            "think": "把并列的另一个人去掉再读一遍，就能判断该用 I 还是 me —— 你能想出还有哪些语法问题也可以用“删掉干扰项”的方法解决？"
        },
        {
            "point": "两类物主代词的分界",
            "explain": "判断只有一步：<b>看后面有没有名词</b>。有名词用<b>形容词性</b>（my, your, his, her），没名词用<b>名词性</b>（mine, yours, his, hers）。",
            "examples": [
                {"tag": "基础", "text": "This is <b>my</b> book.（后面有 book）／ This book is <b>mine</b>.（后面没名词）／ —Whose is it? —It’s <b>hers</b>."},
                {"tag": "进阶", "text": "名词性物主代词 ＝ 形容词性 + 名词：mine ＝ my book，yours ＝ your pen。所以 “This is <u>mine book</u>” 展开就是 “This is my book book”，明显重复了。"},
                {"tag": "易错", "text": "<b>物主代词和冠词不能同时出现</b>：“<u>a my</u> friend” ✗ → <b>a friend of mine</b> ✓（我的一个朋友）。这个 of mine 的结构专门用来解决“既要说一个又要说我的”的矛盾。"}
            ],
            "think": "a friend of mine 直译是“我的朋友中的一个”—— 英语用这么绕的方式，就是为了避免 a 和 my 打架。你觉得值得吗？"
        },
        {
            "point": "指示代词与不定代词",
            "explain": "<b>指示代词</b>：this/these（近）、that/those（远）。<b>不定代词</b>：some/any、something/anything/nothing/everything、somebody/anybody/nobody/everybody。",
            "examples": [
                {"tag": "基础", "text": "<b>this</b> book（这本）／ <b>these</b> books（这些）／ <b>that</b> book（那本）／ <b>those</b> books（那些）"},
                {"tag": "进阶", "text": "<b>复合不定代词永远当单数</b>：Someone <b>is</b> at the door. / Everybody <b>likes</b> him. / Nothing <b>is</b> difficult. 而且<b>形容词要放在它们后面</b>：something <b>new</b>（新东西）、nothing <b>important</b>（没什么重要的）。"},
                {"tag": "易错", "text": "“<u>new something</u>” ✗ → <b>something new</b> ✓ —— 这是英语里少数“形容词放名词后面”的情况，因为 something 本身是不定代词，不是普通名词。"}
            ],
            "think": "英语的形容词几乎总放名词前面（a new book），唯独修饰 something 时要放后面 —— 你觉得这个例外是怎么形成的？"
        },
        {
            "point": "it 的三种特殊用法",
            "explain": "it 除了指“它”，还有三个特殊身份：① <b>非人称主语</b>（说天气时间距离）② <b>形式主语</b>（代替后面的真主语）③ <b>指代前文提到的同一事物</b>。",
            "examples": [
                {"tag": "基础", "text": "① <b>It’s</b> cold today. / <b>It’s</b> eight o’clock. / <b>It’s</b> five kilometres from here.（it 不指任何东西）"},
                {"tag": "进阶", "text": "② <b>It’s</b> important <b>to learn English</b>.（真正的主语是 to learn English，it 只是占位）③ I lost my pen. I must find <b>it</b>.（指同一支笔，对比 one ＝ 另一支）"},
                {"tag": "易错", "text": "it / one / that 三者分工：<b>it ＝ 同一个</b>、<b>one ＝ 同类另一个</b>、<b>that ＝ 比较句中代不可数名词</b>。“I lost my pen, I must find <u>one</u>” 意思变成“随便找一支”，不是想说的。"}
            ],
            "think": "It’s cold today. 里的 it 什么都不指，却不能省略 —— 英语为什么坚持每个句子都要有主语？中文为什么可以不要？"
        }
    ],
    "quiz": [
        {"id": 1, "type": "multi", "point": "代词五列表（想一想·刁钻）",
         "stem": "下列配对<b>正确</b>的有（　）【多选】",
         "options": ["A. her 的名词性物主代词是 hers", "B. his 的名词性物主代词还是 his",
                     "C. its 的名词性物主代词是 it’s", "D. their 的名词性物主代词是 theirs",
                     "E. my 的名词性物主代词是 mine"],
         "answer": ["A", "B", "D", "E"],
         "explain": "只有 C 错：its 的名词性形式<b>还是 its，不加撇号</b>。it’s 是 it is 的缩写。<b>his 和 its 是仅有的两个形容词性和名词性相同的物主代词</b>。"},
        {"id": 2, "type": "multi", "point": "主格与宾格（想一想·刁钻）",
         "stem": "下列句子<b>正确</b>的有（　）【多选】",
         "options": ["A. Tom and I are friends.", "B. Me and Tom are friends.",
                     "C. He gave the book to Tom and me.", "D. He gave the book to Tom and I.",
                     "E. Give it to him."],
         "answer": ["A", "C", "E"],
         "explain": "作<b>主语用主格 I</b>（B 错），作<b>宾语用宾格 me</b>（D 错）。<b>检验方法：把另一个人去掉只留代词读一遍</b>——“He gave the book to I”明显别扭。"},
        {"id": 3, "type": "multi", "point": "两类物主代词·总复习（想一想·刁钻）",
         "stem": "下列句子<b>正确</b>的有（　）【多选】",
         "options": ["A. This is my book.", "B. This is mine book.", "C. This book is mine.",
                     "D. a friend of mine", "E. a my friend"],
         "answer": ["A", "C", "D"],
         "explain": "判断只有一步：<b>后面有名词用 my，没名词用 mine</b>（B 错）。E 错：<b>冠词和物主代词不能同时出现</b>，要说 a friend <b>of mine</b>（D 对）。"},
        {"id": 4, "type": "multi", "point": "复合不定代词（想一想·刁钻）",
         "stem": "下列句子<b>正确</b>的有（　）【多选】",
         "options": ["A. Someone is at the door.", "B. Someone are at the door.",
                     "C. Everybody likes him.", "D. I want something new.",
                     "E. I want new something."],
         "answer": ["A", "C", "D"],
         "explain": "<b>复合不定代词永远当单数</b>（B 错），<b>形容词要放在它们后面</b>（E 错）。这是英语里少数“形容词后置”的情况。"},
        {"id": 5, "type": "multi", "point": "it / one / that（想一想·刁钻）",
         "stem": "下列句子<b>正确</b>的有（　）【多选】",
         "options": ["A. I lost my pen. I must find it.", "B. I lost my pen. I need to buy one.",
                     "C. I lost my pen. I must find one.（想找回原来那支）",
                     "D. The weather here is better than that in Beijing.",
                     "E. It’s important to learn English."],
         "answer": ["A", "B", "D", "E"],
         "explain": "只有 C 错：要找回<b>同一支</b>笔用 it，one 是“同类另一个”。D 用 that 代替不可数名词 weather。E 是 it 作<b>形式主语</b>的典型用法。"},
        {"id": 6, "type": "choice", "point": "宾格",
         "stem": "This present is for you and ______.",
         "options": ["A. me", "B. I", "C. my", "D. mine"],
         "answer": "A",
         "explain": "介词 for 后面要用<b>宾格</b> me。检验方法：去掉 you and 只留代词——“This present is for me” ✓，“for I” ✗。"},
        {"id": 7, "type": "choice", "point": "名词性物主代词",
         "stem": "My bike is broken. May I use ______?",
         "options": ["A. you", "B. your", "C. yours", "D. yourself"],
         "answer": "C",
         "explain": "use 后面<b>没有名词</b>，要用名词性物主代词 <b>yours</b>（＝ your bike）。your 后面必须跟名词。"},
        {"id": 8, "type": "choice", "point": "复合不定代词的语序",
         "stem": "Is there ______ in today’s newspaper?",
         "options": ["A. anything interesting", "B. interesting anything",
                     "C. anything interested", "D. something interesting"],
         "answer": "A",
         "explain": "两个考点：① <b>形容词放在复合不定代词后面</b>（排除 B）② <b>疑问句用 anything 不用 something</b>（排除 D）③ 形容事物用 <b>ing</b> 形式 interesting（排除 C）。"},
        {"id": 9, "type": "fill", "point": "反身代词",
         "stem": "填空：The little boy can dress ______ now.（他自己，填一个词）",
         "answer": ["himself"],
         "explain": "主语是 The little boy（男性单数），反身代词用 <b>himself</b>（不是 hisself）。第三人称用宾格 + self。"},
        {"id": 10, "type": "fill", "point": "名词性物主代词",
         "stem": "同义句改写：This is her bag. → This bag is ______.（填一个词）",
         "answer": ["hers"],
         "explain": "改写后 is 的后面<b>没有名词</b>，要用名词性物主代词 <b>hers</b>（＝ her bag）。注意 her 和 hers 形式不同（而 his 两种形式相同）。"},
        {"id": 11, "type": "judge", "point": "his 与 its 的特殊性",
         "stem": "This is his book. 和 This book is his. 里的两个 his 长得一样，说明所有物主代词的两种形式都相同。",
         "answer": "错",
         "explain": "错。<b>只有 his 和 its 两组形式相同</b>，其余全都要变形：my→mine、your→yours、her→hers、our→ours、their→theirs。所以看到 her 和 hers 不一样是正常的，看到 his 和 his 一样才是特例。"},
        {"id": 12, "type": "judge", "point": "形容词修饰不定代词的位置",
         "stem": "修饰 something、anything 这类不定代词时，形容词要放在它们后面。",
         "answer": "对",
         "explain": "对。<b>something new、anything important、nothing special</b> —— 这是英语里少数“形容词后置”的情况。普通名词前面才是常规位置（a new book）。"}
    ]
}

s4 = {
    "id": "e-c7-s4",
    "title": "专题四 动词形式与助动词",
    "notes": [
        {
            "point": "动词的五种形式",
            "explain": "每个动词最多有五种形式：<b>原形 / 三单 / 现在分词 / 过去式 / 过去分词</b>。知道一个动词在句子里该用哪种形式，是英语语法的核心能力。",
            "examples": [
                {"tag": "基础", "text": "work / works / working / worked / worked（规则）<br>go / goes / going / went / gone（不规则）<br>be / is / being / was / been（最特殊）"},
                {"tag": "进阶", "text": "各自的岗位：<b>原形</b>跟在情态动词和 do/does/did 后面；<b>三单</b>用于一般现在时三单主语；<b>现在分词</b>跟在 be 后面（进行时）；<b>过去式</b>独立作谓语；<b>过去分词</b>跟在 have（完成时）或 be（被动）后面。"},
                {"tag": "易错", "text": "<b>过去式和过去分词绝不能互换</b>：I <b>saw</b> him. ✓ / I have <b>seen</b> him. ✓ / I <u>seen</u> him ✗ / I have <u>saw</u> him ✗。规则动词两者同形，所以这个错在不规则动词上才暴露。"}
            ],
            "think": "五种形式各有各的岗位，从来不越界 —— 你能只看一个动词的形式，就反推出它前面应该有什么词吗？试试 seen、going、goes。"
        },
        {
            "point": "三种拼写调整规则（通用）",
            "explain": "加 s、加 ing、加 ed、加 er/est 时，用的是同一套拼写调整逻辑：① <b>变 y 为 i</b>（辅音+y）② <b>双写</b>（重读闭音节）③ <b>去 e</b>（e 结尾）。",
            "examples": [
                {"tag": "基础", "text": "study：studies / studying / studied<br>stop：stops / stopping / stopped<br>like：likes / liking / liked"},
                {"tag": "进阶", "text": "注意<b>加 ing 时 y 不变</b>：study→study<b>ing</b>（不是 studiing）。因为 i 和 i 不能连着写。所以“变 y 为 i”只适用于加 s、ed、er、est，<b>不适用于加 ing</b>。"},
                {"tag": "易错", "text": "双写的前提是<b>重读闭音节</b>（辅音+元音+辅音）：stop ✓、run ✓、big ✓，但 rain ✗（ai 是两个元音字母）、open ✗（重音在前）、long ✗（ng 是两个辅音字母）。判断错了就会多写或少写一个字母。"}
            ],
            "think": "study 加 ed 变 studied（y 变 i），加 ing 却是 studying（y 不变）—— 这个例外的原因是什么？（提示：试着写 studiing，看看像不像英语单词。）"
        },
        {
            "point": "助动词大盘点",
            "explain": "助动词自己没有实际意义，只负责承担<b>时态、人称、否定、疑问</b>这些语法信息。第一册出现的助动词有：be、do/does/did、have/has、will、情态动词。",
            "examples": [
                {"tag": "基础", "text": "<b>be</b>：进行时（is doing）、被动（is done）<br><b>do/does/did</b>：一般时态的疑问否定<br><b>have/has</b>：完成时（has done）<br><b>will</b>：将来时"},
                {"tag": "进阶", "text": "<b>核心规则：谁承担了时态信息，谁就负责变疑问和否定，同时主要动词还原成原形。</b>He <b>likes</b> tea → <b>Does</b> he <b>like</b> tea?（s 从 like 搬到了 does 上）"},
                {"tag": "易错", "text": "have 有两个身份：<b>实义动词</b>“有”（I have a book → Do you have a book?）和<b>助动词</b>（完成时 I have finished → Have you finished?）。同一个词，变疑问的方式完全不同，要看它在句中干什么活。"}
            ],
            "think": "“谁承担时态信息，谁就负责变疑问否定”—— 用这一条规则，你能解释清楚 Does he like / Is he reading / Has he gone / Can he swim 这四个疑问句为什么长得都不一样吗？"
        },
        {
            "point": "非谓语动词入门：to do 与 doing",
            "explain": "一个句子只能有一个谓语动词，其他动词要变成<b>非谓语形式</b>：<b>to do</b>（不定式）或 <b>doing</b>（动名词/分词）。",
            "examples": [
                {"tag": "基础", "text": "<b>跟 to do</b>：want to do、would like to do、ask sb to do、tell sb to do、decide to do、hope to do。<br><b>跟 doing</b>：enjoy doing、like doing、finish doing、be good at doing、go on doing。"},
                {"tag": "进阶", "text": "介词后面<b>只能跟 doing</b>：be good <b>at swimming</b>、thank you <b>for helping</b>、instead <b>of going</b>。因为介词后面要跟名词性成分，动名词就是动词的名词形式。"},
                {"tag": "易错", "text": "“I want <u>go</u> home.” ✗ —— want 后面要跟不定式：I want <b>to go</b> home. ✓ 而 “I enjoy <u>to read</u>.” ✗ —— enjoy 后面只能跟动名词：I enjoy <b>reading</b>. ✓ 哪个词配哪种形式，只能记。"}
            ],
            "think": "一个句子只能有一个谓语动词，其他动词必须“变形”—— 中文可以说“我想去买书”连用三个动词，英语为什么不行？"
        },
        {
            "point": "情态动词全表",
            "explain": "第一册的情态动词：<b>can/could</b>（能、可以）、<b>may/might</b>（可以、可能）、<b>must</b>（必须）、<b>should</b>（应该）、<b>will/would</b>（将、愿意）。共同特点：<b>自己不变形、后面跟原形、不用 do 变疑问否定</b>。",
            "examples": [
                {"tag": "基础", "text": "He <b>can</b> swim. → <b>Can</b> he swim? / He <b>can’t</b> swim.（不用 does）"},
                {"tag": "进阶", "text": "语气强弱：<b>must</b>（必须）> <b>should</b>（应该）> <b>may</b>（可以）／ 礼貌程度：<b>could/would</b> > <b>can/will</b>（过去式形式表示委婉，不表示过去）。"},
                {"tag": "易错", "text": "<b>mustn’t ≠ 不必</b>：mustn’t ＝ <b>绝对不可以</b>（禁止）；“不必”是 <b>don’t have to</b>。这两个的意思差得极远，实际交流中用错会造成严重误会。"}
            ],
            "think": "情态动词的过去式（could、would、might）经常不表示过去，而表示“更客气”—— 英语为什么把“距离感”和“礼貌”联系在一起？"
        }
    ],
    "quiz": [
        {"id": 1, "type": "multi", "point": "五种动词形式的岗位（想一想·刁钻）",
         "stem": "下列句子<b>正确</b>的有（　）【多选】",
         "options": ["A. I saw him yesterday.", "B. I seen him yesterday.",
                     "C. I have seen him.", "D. I have saw him.", "E. He is seeing a doctor."],
         "answer": ["A", "C", "E"],
         "explain": "<b>过去式独立作谓语</b>（A），<b>过去分词跟在 have 后面</b>（C），<b>现在分词跟在 be 后面</b>（E）。B 和 D 把过去式和过去分词用反了。"},
        {"id": 2, "type": "multi", "point": "拼写调整规则（想一想·刁钻）",
         "stem": "下列拼写<b>正确</b>的有（　）【多选】",
         "options": ["A. studied", "B. studying", "C. studiing", "D. stopping", "E. raining"],
         "answer": ["A", "B", "D", "E"],
         "explain": "只有 C 错。<b>“变 y 为 i”不适用于加 ing</b>（因为 i 和 i 不能连写），所以是 studying。E 对：rain 的 ai 是两个元音字母，不属于重读闭音节，不双写。"},
        {"id": 3, "type": "multi", "point": "助动词的核心规则（想一想·刁钻）",
         "stem": "下列句子<b>正确</b>的有（　）【多选】",
         "options": ["A. Does he like tea?", "B. Is he reading?", "C. Has he gone?",
                     "D. Can he swim?", "E. Does he can swim?"],
         "answer": ["A", "B", "C", "D"],
         "explain": "只有 E 错：句中已有情态动词 can，<b>不需要再请 do 出场</b>。前四句展示了四种不同的助动词各自负责变疑问：do / be / have / 情态动词。"},
        {"id": 4, "type": "multi", "point": "to do 与 doing 的搭配（想一想·刁钻）",
         "stem": "下列搭配<b>正确</b>的有（　）【多选】",
         "options": ["A. want to go", "B. want go", "C. enjoy reading",
                     "D. enjoy to read", "E. be good at swimming"],
         "answer": ["A", "C", "E"],
         "explain": "want 后跟<b>不定式</b>（B 漏了 to），enjoy 后只能跟<b>动名词</b>（D 错），<b>介词后面只能跟 doing</b>（E 对）。哪个词配哪种形式只能记。"},
        {"id": 5, "type": "multi", "point": "情态动词的共同特点（想一想·刁钻）",
         "stem": "关于情态动词，说法<b>正确</b>的有（　）【多选】",
         "options": ["A. 自己没有第三人称单数形式。", "B. 后面跟动词原形。",
                     "C. 变疑问否定不用 do。", "D. mustn’t 的意思是“不必”。",
                     "E. could 在请求句里表示委婉，不表示过去。"],
         "answer": ["A", "B", "C", "E"],
         "explain": "只有 D 错：<b>mustn’t ＝ 绝对不可以（禁止）</b>，“不必”是 don’t have to。这两个意思差得极远，实际交流中用错会造成严重误会。"},
        {"id": 6, "type": "choice", "point": "过去分词的岗位",
         "stem": "The window was ______ by the boy yesterday.",
         "options": ["A. break", "B. broke", "C. broken", "D. breaking"],
         "answer": "C",
         "explain": "was + ______ 是<b>被动语态</b>，要用<b>过去分词</b> broken。凡是跟在 be 或 have 后面的动词，一律用过去分词。"},
        {"id": 7, "type": "choice", "point": "介词后跟动名词",
         "stem": "Thank you for ______ me with my homework.",
         "options": ["A. help", "B. to help", "C. helping", "D. helps"],
         "answer": "C",
         "explain": "for 是<b>介词</b>，后面只能跟<b>动名词</b>（doing）。介词后面需要名词性成分，动名词就是动词的名词形式。"},
        {"id": 8, "type": "choice", "point": "have 的两个身份",
         "stem": "—______ you finished your homework?　—Yes, I have.",
         "options": ["A. Do", "B. Have", "C. Are", "D. Did"],
         "answer": "B",
         "explain": "finished 是<b>过去分词</b>，说明这是现在完成时，have 在这里是<b>助动词</b>，直接提到句首变疑问。如果是实义动词“有”才用 Do you have…?"},
        {"id": 9, "type": "fill", "point": "动词形式",
         "stem": "写出 lie（躺）的现在分词形式：______",
         "answer": ["lying"],
         "explain": "以 <b>ie 结尾的动词，加 ing 时要 ie 变 y</b> → lying。同类：die→dying、tie→tying。这是加 ing 的第四条规则。"},
        {"id": 10, "type": "fill", "point": "非谓语搭配",
         "stem": "用 swim 的正确形式填空：My brother is good at ______.（填一个词）",
         "answer": ["swimming"],
         "explain": "at 是<b>介词</b>，后面跟<b>动名词</b>；swim 是重读闭音节，加 ing 要双写 m → swimming。"},
        {"id": 11, "type": "judge", "point": "y 变 i 的适用范围",
         "stem": "study 加 ed 变成 studied，加 ing 变成 studiing。",
         "answer": "错",
         "explain": "错。<b>“变 y 为 i”不适用于加 ing</b>，因为 i 和 i 不能连着写。正确是 study<b>ing</b>（y 保留）。这条规则只管加 s、ed、er、est。"},
        {"id": 12, "type": "judge", "point": "助动词核心规则",
         "stem": "助动词一旦承担了时态和人称信息，主要动词就要还原成原形。",
         "answer": "对",
         "explain": "对。这是贯穿全册的核心规则：He like<b>s</b> → <b>Does</b> he <b>like</b>?（s 搬家到 does 上）／ He <b>went</b> → <b>Did</b> he <b>go</b>?（时态搬家到 did 上）。理解了这一条，Does he likes、Did he went 这类错误就永远不会再犯。"}
    ]
}

s5 = {
    "id": "e-c7-s5",
    "title": "专题五 形容词 · 副词 · 比较结构",
    "notes": [
        {
            "point": "形容词与副词的分工",
            "explain": "<b>形容词</b>修饰名词或作表语（放 be 后面）；<b>副词</b>修饰动词、形容词或其他副词。判断只有一步：<b>看它修饰的是什么词</b>。",
            "examples": [
                {"tag": "基础", "text": "He is a <b>careful</b> driver.（形容词修饰名词 driver）／ He drives <b>carefully</b>.（副词修饰动词 drives）—— 同一个意思，两种说法。"},
                {"tag": "进阶", "text": "副词构成：<b>形容词 + ly</b>（quick→quickly）／ <b>辅音+y 变 i 加 ly</b>（happy→happily）／ <b>le 结尾去 e 加 y</b>（simple→simply）／ <b>形副同形</b>（fast, hard, late, early, high）。"},
                {"tag": "易错", "text": "两组陷阱：① <b>friendly、lovely、lonely 以 ly 结尾却是形容词</b>；② <b>hardly、lately 虽然是 hard、late 加 ly，意思却完全不同</b>（几乎不 / 最近）。不能只看词尾判断词性。"}
            ],
            "think": "He is a careful driver. 和 He drives carefully. 说的完全是一回事 —— 英语为什么要保留两种表达同一个意思的结构？"
        },
        {
            "point": "三级变化总规则",
            "explain": "<b>单音节和部分双音节</b>加 er / est；<b>三音节及以上</b>用 more / most。拼写调整和加 ed 一样（去 e、变 y 为 i、双写）。",
            "examples": [
                {"tag": "基础", "text": "tall-taller-tallest ／ nice-nicer-nicest ／ easy-easier-easiest ／ big-bigger-biggest ／ beautiful-more beautiful-most beautiful"},
                {"tag": "进阶", "text": "五组不规则必背：good/well-<b>better-best</b>／ bad/ill-<b>worse-worst</b>／ many/much-<b>more-most</b>／ little-<b>less-least</b>／ far-<b>farther/further-farthest/furthest</b>。"},
                {"tag": "易错", "text": "<b>er/est 和 more/most 绝不能同时用</b>：more taller ✗、most tallest ✗。要加强语气用 <b>much</b>（much taller）或 <b>by far</b>（by far the tallest），不是叠加两种比较级形式。"}
            ],
            "think": "比较级、过去式、进行时的拼写调整用的是同一套规则（去 e、变 y、双写）—— 你能把这套规则写成一段话，让别人一次记住吗？"
        },
        {
            "point": "三种比较结构",
            "explain": "① <b>A + 比较级 + than + B</b>（A 比 B 更…）② <b>A + as + 原级 + as + B</b>（A 和 B 一样…）③ <b>A + the + 最高级 + in/of…</b>（A 是…中最…的）。",
            "examples": [
                {"tag": "基础", "text": "He is <b>taller than</b> me.／ He is <b>as tall as</b> me.／ He is <b>the tallest in</b> our class."},
                {"tag": "进阶", "text": "同义句改写三件套：<b>A is not as tall as B</b> ＝ <b>A is shorter than B</b> ＝ <b>B is taller than A</b>。三句话说的是同一件事，考试常考互相改写。"},
                {"tag": "易错", "text": "结构里的形容词形式各不相同：than 前用<b>比较级</b>、as…as 中间用<b>原级</b>、最高级前加 <b>the</b>。三个结构配三种形式，配错就全错。"}
            ],
            "think": "A is not as tall as B / A is shorter than B / B is taller than A —— 同一个事实三种说法，你觉得在什么场合会选择哪一种？"
        },
        {
            "point": "最高级的搭配与例外",
            "explain": "<b>the + 最高级 + in + 范围（地方/团体）</b>；<b>the + 最高级 + of + 同类事物</b>。前面已有物主代词时<b>不加 the</b>。",
            "examples": [
                {"tag": "基础", "text": "the tallest <b>in</b> our class（团体）／ the tallest <b>of</b> the three（同类）／ <b>my</b> best friend（有 my 就不加 the）"},
                {"tag": "进阶", "text": "<b>“最……之一”</b>用复数：He is <b>one of the tallest students</b> in our class.（students 要复数，因为“最高的学生们”有好几个，他是其中之一）。"},
                {"tag": "易错", "text": "“one of the tallest <u>student</u>” ✗ —— one of 后面必须跟<b>复数名词</b>：one of the tallest <b>students</b> ✓。这是最高级里最容易漏的一个 s。"}
            ],
            "think": "one of the tallest students 里 students 是复数，但整个短语作主语时动词却用单数（One of the students <b>is</b>…）—— 为什么？"
        },
        {
            "point": "too / enough / so / very 的位置与含义",
            "explain": "<b>too</b>（太…，含贬义，放形容词前）／ <b>very</b>（很，中性，放形容词前）／ <b>so</b>（如此，放形容词前）／ <b>enough</b>（足够，<b>形容词后、名词前</b>）。",
            "examples": [
                {"tag": "基础", "text": "It’s <b>too</b> small.（太小了，穿不下）／ It’s <b>very</b> small.（很小，但可能刚好）／ It’s big <b>enough</b>.（够大了）／ I have <b>enough</b> money."},
                {"tag": "进阶", "text": "两个固定句型：<b>too + 形容词 + to do</b>（太…而不能…，含否定意义）／ <b>so + 形容词 + that + 句子</b>（如此…以至于…）。He is <b>too young to</b> go. ＝ He is <b>so young that</b> he can’t go."},
                {"tag": "易错", "text": "enough 的位置随词性变：<b>形容词后</b>（big enough ✓ / enough big ✗）、<b>名词前</b>（enough money ✓ / money enough ✗）。这是英语里少见的“位置不固定”的词。"}
            ],
            "think": "too young to go 整句没有否定词，意思却是“不能去”—— 英语用这种方式表达否定，比直接说 can’t 有什么好处？"
        }
    ],
    "quiz": [
        {"id": 1, "type": "multi", "point": "形容词与副词的判断（想一想·刁钻）",
         "stem": "下列句子<b>正确</b>的有（　）【多选】",
         "options": ["A. He is a careful driver.", "B. He drives carefully.",
                     "C. He drives careful.", "D. He sings well.", "E. He sings good."],
         "answer": ["A", "B", "D"],
         "explain": "<b>修饰名词用形容词，修饰动词用副词</b>。C 用形容词修饰了动词 drives，E 用形容词修饰了动词 sings，都应改成副词（carefully / well）。"},
        {"id": 2, "type": "multi", "point": "ly 结尾不等于副词（想一想·刁钻）",
         "stem": "下列说法<b>正确</b>的有（　）【多选】",
         "options": ["A. friendly 是形容词。", "B. lovely 是形容词。",
                     "C. hardly 和 hard 意思相同。", "D. lately 意思是“最近”。",
                     "E. fast 的副词形式还是 fast。"],
         "answer": ["A", "B", "D", "E"],
         "explain": "只有 C 错：<b>hardly ＝ 几乎不（否定词）</b>，和 hard（努力地）意思相反。不能只看词尾判断词性和意思。"},
        {"id": 3, "type": "multi", "point": "三种比较结构（想一想·刁钻）",
         "stem": "下列句子<b>正确</b>的有（　）【多选】",
         "options": ["A. He is taller than me.", "B. He is as tall as me.",
                     "C. He is as taller as me.", "D. He is the tallest in our class.",
                     "E. He is tallest in our class."],
         "answer": ["A", "B", "D"],
         "explain": "三个结构配三种形式：<b>than 前用比较级、as…as 中间用原级、最高级前加 the</b>。C 在 as…as 中用了比较级，E 漏了 the。"},
        {"id": 4, "type": "multi", "point": "最高级的搭配（想一想·刁钻）",
         "stem": "下列表达<b>正确</b>的有（　）【多选】",
         "options": ["A. the tallest in our class", "B. the tallest of the three",
                     "C. my best friend", "D. one of the tallest students",
                     "E. one of the tallest student"],
         "answer": ["A", "B", "C", "D"],
         "explain": "只有 E 错：<b>one of 后面必须跟复数名词</b> → students。C 对：前面有物主代词 my 就不再加 the。<b>in 跟范围，of 跟同类</b>。"},
        {"id": 5, "type": "multi", "point": "too / enough 的位置·总复习（想一想·刁钻）",
         "stem": "下列表达<b>正确</b>的有（　）【多选】",
         "options": ["A. too small", "B. big enough", "C. enough big",
                     "D. enough money", "E. money enough"],
         "answer": ["A", "B", "D"],
         "explain": "<b>enough 修饰形容词放后面（big enough），修饰名词放前面（enough money）</b>。C、E 都放反了。这是英语里少见的“位置随词性变”的词。"},
        {"id": 6, "type": "choice", "point": "比较级的修饰",
         "stem": "This room is ______ bigger than that one.",
         "options": ["A. very", "B. much", "C. so", "D. too"],
         "answer": "B",
         "explain": "修饰<b>比较级</b>要用 much（…得多），不能用 very（very 只修饰原级）。同类可用的还有 a little、even、far。"},
        {"id": 7, "type": "choice", "point": "one of 的搭配",
         "stem": "Beijing is one of the biggest ______ in China.",
         "options": ["A. city", "B. cities", "C. citys", "D. a city"],
         "answer": "B",
         "explain": "<b>one of 后面必须跟复数名词</b>；city 的复数是 <b>cities</b>（辅音+y 变 i 加 es）。这题同时考 one of 的搭配和复数拼写。"},
        {"id": 8, "type": "choice", "point": "too...to 句型",
         "stem": "The box is ______ heavy ______ I can’t carry it.",
         "options": ["A. too, to", "B. enough, to", "C. very, that", "D. so, that"],
         "answer": "D",
         "explain": "后半句是<b>完整的句子</b>（I can’t carry it），要用 <b>so … that + 句子</b>。如果用 too…to，句子应该是 The box is too heavy <b>to carry</b>.（后面跟动词不定式）。"},
        {"id": 9, "type": "fill", "point": "副词形式",
         "stem": "写出 careful 对应的副词形式：______",
         "answer": ["carefully"],
         "explain": "careful 以 l 结尾，直接<b>加 ly</b> → carefully（两个 l）。注意不要漏掉一个 l。"},
        {"id": 10, "type": "fill", "point": "同义句改写",
         "stem": "同义句：Tom is not as tall as Jack. → Tom is ______ than Jack.（填一个词）",
         "answer": ["shorter"],
         "explain": "not as tall as ＝ 不如……高 ＝ 比……<b>矮</b>，所以填 shorter。这组三句互换（not as…as / shorter than / taller than 反过来）是高频改写题。"},
        {"id": 11, "type": "judge", "point": "比较级不能叠加",
         "stem": "为了加强语气，可以说 more taller 或 most tallest。",
         "answer": "错",
         "explain": "错。<b>er/est 和 more/most 是两套并列的方式，绝不能同时用</b>。要加强语气用 <b>much taller</b>（比较级）或 <b>by far the tallest</b>（最高级）。"},
        {"id": 12, "type": "judge", "point": "one of 的单复数",
         "stem": "one of the tallest students 中的 students 要用复数，但如果这个短语作主语，动词要用单数。",
         "answer": "对",
         "explain": "对。<b>one of + 复数名词</b>（他是“那些最高的学生”中的一个），但整个短语的<b>中心词是 one</b>，所以作主语时动词用单数：One of the students <b>is</b> from Japan."}
    ]
}

s6 = {
    "id": "e-c7-s6",
    "title": "专题六 句型转换 · 中式英语纠错终检",
    "notes": [
        {
            "point": "六种基本句型转换",
            "explain": "考试最常考的六种改写，每种都有固定步骤。",
            "examples": [
                {"tag": "基础", "text": "① <b>变一般疑问句</b>：有 be/情态/助动词就提前，没有就加 do/does/did（动词还原）<br>② <b>变否定句</b>：在 be/情态/助动词后加 not，没有就加 don’t/doesn’t/didn’t（动词还原）"},
                {"tag": "进阶", "text": "③ <b>对划线部分提问</b>：先定<b>疑问词</b>（问人 who、问物 what、问地点 where、问时间 when、问原因 why、问方式 how、问数量 how many/much），再<b>倒装</b>，划线部分删掉<br>④ <b>陈述句变间接引语</b>：改人称、时态、时间地点词<br>⑤ <b>主动变被动</b>：宾语提前 + be + 过去分词 + by<br>⑥ <b>同义句改写</b>：not as…as ＝ 比较级、too…to ＝ so…that"},
                {"tag": "易错", "text": "第 ③ 种最容易错在<b>忘了删掉划线部分</b>：He went to <u>Beijing</u>. → Where did he go? ✓（不是 Where did he go to Beijing? ✗）。提问就是把那部分挖掉，用疑问词顶上。"}
            ],
            "think": "六种转换里，有四种都用到了“助动词提前/加入”这个动作 —— 这是不是说明助动词才是英语句型变化的“开关”？"
        },
        {
            "point": "中式英语高频错误（一）：多余与缺失",
            "explain": "中文有而英语没有的东西要<b>删掉</b>，英语有而中文没有的东西要<b>补上</b>。",
            "examples": [
                {"tag": "基础", "text": "<b>要删的</b>：虽然…但是…（Although… but… ✗）／ 因为…所以…（Because… so… ✗）／ 双重否定（don’t never ✗）"},
                {"tag": "进阶", "text": "<b>要补的</b>：① <b>冠词</b>（I’m a teacher，中文没有）② <b>be 动词</b>（He is tall，中文说“他高”不用“是”）③ <b>主语</b>（It’s raining，中文说“下雨了”不用主语）④ <b>单复数标记</b>（three books 要加 s）"},
                {"tag": "易错", "text": "最高频的两个：<b>漏 be 动词</b>（“He very tall.” ✗ → He <b>is</b> very tall. ✓）和<b>漏冠词</b>（“He is teacher.” ✗ → He is <b>a</b> teacher. ✓）。这两个错都源于中文里根本没有这两样东西。"}
            ],
            "think": "中文说“他很高”三个字就够了，英语必须说 He is very tall 四个词 —— 那个 is 到底提供了什么信息？"
        },
        {
            "point": "中式英语高频错误（二）：搭配直译",
            "explain": "中文的搭配习惯不能直接搬到英语上，这类错误最难自查，因为“读起来很顺”。",
            "examples": [
                {"tag": "基础", "text": "“价格贵” → The price is <b>high</b>（不是 expensive）／ “看电视” → <b>watch</b> TV（不是 look at）／ “学习知识” → <b>learn</b> knowledge（不是 study knowledge）"},
                {"tag": "进阶", "text": "“我很喜欢” → I like it <b>very much</b>（不是 I very like it）／ “我们班有50人” → <b>There are</b> fifty students in our class（不是 Our class have）／ “开灯” → <b>turn on</b> the light（不是 open the light）"},
                {"tag": "易错", "text": "判断方法：写完一句话后，<b>凡是感觉“和中文一个字一个字对得上”的地方，都要停下来检查</b>。真正地道的英语句子，往往和中文的字面结构对不上。"}
            ],
            "think": "“开灯”用 turn on 不用 open，“开门”却真的用 open —— 同一个“开”字，英语为什么要分两个词？"
        },
        {
            "point": "全册易错点终检清单（十条）",
            "explain": "写完任何英语句子，按这十条扫一遍，能消掉九成以上的错误。",
            "examples": [
                {"tag": "基础", "text": "① 三单加 s 了吗　② be 动词对吗　③ 时态和时间状语匹配吗　④ 名词单复数对吗　⑤ 冠词漏了吗"},
                {"tag": "进阶", "text": "⑥ 助动词出现后动词还原了吗　⑦ 介词搭配对吗（listen to、good at）　⑧ 从句用陈述语序了吗　⑨ 比较级/最高级形式对吗　⑩ 有没有中文式的“虽然但是”“因为所以”"},
                {"tag": "易错", "text": "十条里，<b>第 ⑤ 条（冠词）和第 ⑩ 条（连词重复）</b>最容易漏，因为中文里完全没有对应概念。养成习惯：写完先找这两样。"}
            ],
            "think": "这十条自查清单里，有几条是“中文里没有的东西”？这是不是说明学英语最难的部分，恰恰是母语没教过你注意的地方？"
        }
    ],
    "quiz": [
        {"id": 1, "type": "multi", "point": "对划线部分提问（想一想·刁钻）",
         "stem": "对 He went to <u>Beijing</u> last week. 划线部分提问，<b>正确</b>的有（　）【多选】",
         "options": ["A. Where did he go last week?", "B. Where did he go to Beijing last week?",
                     "C. Where he went last week?", "D. Where did he went last week?",
                     "E. 提问时要把划线部分删掉。"],
         "answer": ["A", "E"],
         "explain": "B <b>忘了删掉划线部分</b>（最常见的错）；C 没倒装；D 的 did 后面动词没还原。<b>提问就是把那部分挖掉，用疑问词顶上，再倒装</b>。"},
        {"id": 2, "type": "multi", "point": "中文有英语没有的东西（想一想·刁钻）",
         "stem": "下列句子<b>正确</b>的有（　）【多选】",
         "options": ["A. Although he is old, he is strong.", "B. Although he is old, but he is strong.",
                     "C. Because it rained, we stayed home.", "D. Because it rained, so we stayed home.",
                     "E. I never go there."],
         "answer": ["A", "C", "E"],
         "explain": "<b>英语里 although 和 but、because 和 so 都不能同时出现</b>（B、D 错）。中文“虽然…但是…”“因为…所以…”要两个词，英语只能用一个。"},
        {"id": 3, "type": "multi", "point": "英语有中文没有的东西（想一想·刁钻）",
         "stem": "下列句子<b>正确</b>的有（　）【多选】",
         "options": ["A. He is very tall.", "B. He very tall.", "C. He is a teacher.",
                     "D. He is teacher.", "E. It’s raining."],
         "answer": ["A", "C", "E"],
         "explain": "B <b>漏了 be 动词</b>（中文说“他高”不用“是”），D <b>漏了冠词</b>（中文说“他是老师”不用“一个”）。这两个是最高频的中式英语错误，都源于中文里没有这两样东西。"},
        {"id": 4, "type": "multi", "point": "搭配不能直译（想一想·刁钻）",
         "stem": "下列表达<b>正确</b>的有（　）【多选】",
         "options": ["A. The price is high.", "B. The price is expensive.", "C. watch TV",
                     "D. I like it very much.", "E. I very like it."],
         "answer": ["A", "C", "D"],
         "explain": "B 错（<b>价格配 high 不配 expensive</b>）；E 错（<b>very 不能修饰动词</b>，要说 very much）。判断方法：凡是感觉“和中文一字一对”的地方都要停下来检查。"},
        {"id": 5, "type": "multi", "point": "自查清单（想一想·刁钻）",
         "stem": "下列<b>属于</b>英语自查项目的有（　）【多选】",
         "options": ["A. 三单有没有加 s", "B. 单数可数名词前有没有冠词",
                     "C. 助动词出现后动词有没有还原", "D. 从句有没有用陈述语序",
                     "E. 句子是不是超过了十五个词"],
         "answer": ["A", "B", "C", "D"],
         "explain": "只有 E 不是语法检查项。前四条中，<b>B（冠词）</b>最容易漏——因为中文完全没有冠词这个概念，写的时候根本想不起来。"},
        {"id": 6, "type": "choice", "point": "主动变被动",
         "stem": "They built this bridge in 2010. → This bridge ______ in 2010.",
         "options": ["A. was built", "B. builds", "C. is built", "D. was build"],
         "answer": "A",
         "explain": "被动语态是 <b>be + 过去分词</b>；原句是过去时（in 2010），新主语 This bridge 是单数，所以 be 用 was；build 的过去分词是 built。"},
        {"id": 7, "type": "choice", "point": "同义句改写",
         "stem": "He is too young to go to school. ＝ He is ______ young ______ he can’t go to school.",
         "options": ["A. too, that", "B. so, to", "C. very, that", "D. so, that"],
         "answer": "D",
         "explain": "<b>too…to do ＝ so…that + 句子</b>（否定）。后半句是完整的句子，所以要用 so…that 结构。"},
        {"id": 8, "type": "choice", "point": "中式英语纠错",
         "stem": "下列句子中，表达<b>最地道</b>的是：",
         "options": ["A. Our class have fifty students.", "B. There are fifty students in our class.",
                     "C. Our class has fifty student.", "D. In our class have fifty students."],
         "answer": "B",
         "explain": "“某地有某物”用 <b>There be</b>，不用 have。A、D 都是中文“我们班有…”的直译。C 除了 have/has 的问题，student 还漏了复数 s。"},
        {"id": 9, "type": "fill", "point": "对划线部分提问",
         "stem": "对 He goes to school <u>by bike</u>. 划线部分提问：______ does he go to school?（填一个词）",
         "answer": ["How"],
         "explain": "by bike 是<b>交通方式</b>，问方式用 <b>How</b>。同时注意提问后要把 by bike 删掉，并保持倒装语序。"},
        {"id": 10, "type": "fill", "point": "中式英语纠错",
         "stem": "改错：He is teacher. 这句话漏了一个词，应该在 is 后面加上：______",
         "answer": ["a"],
         "explain": "<b>职业名词前必须加冠词</b>：He is <b>a</b> teacher. 中文说“他是老师”不需要“一个”，所以这是中国学生最容易漏的一处。"},
        {"id": 11, "type": "judge", "point": "提问要删划线部分",
         "stem": "对划线部分提问时，要保留原句的全部内容，只在句首加上疑问词。",
         "answer": "错",
         "explain": "错。<b>提问就是把划线部分挖掉，用疑问词顶上，再倒装</b>：He went to <u>Beijing</u>. → <b>Where did he go?</b> ✓ 写成 Where did he go <u>to Beijing</u>? ✗ 就是保留了不该保留的内容——这是本类题最高频的失分点。"},
        {"id": 12, "type": "judge", "point": "中英差异的根源",
         "stem": "英语自查清单里最容易漏的项目（如冠词、连词不重复），恰恰是中文里没有对应概念的部分。",
         "answer": "对",
         "explain": "对。<b>母语没教过你注意的东西，你就想不起来检查</b>。中文没有冠词，所以漏 a/an/the；中文“虽然…但是…”成对出现，所以会写出 Although…but…。<b>知道自己会在哪里犯错，比记住规则更重要。</b>"}
    ]
}

CHAPTER = {
    "id": "e-c7",
    "title": "第七章 语法专题总复习：跨课次整合辨析",
    "sections": [s1, s2, s3, s4, s5, s6]
}
