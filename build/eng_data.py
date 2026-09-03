# -*- coding: utf-8 -*-
"""
新概念英语第一册 · 考点数据（单一事实源）
功能：以 Python dict 保存全部考点讲解与测验题，供 build_eng.py 注入 eng.html
约定：绝不手写 JS 对象字面量，一律 json.dumps(ensure_ascii=False) 注入
题型：choice(单选) / multi(多选,answer为字母数组) / judge(对错) / fill(填空,answer为可接受答案数组)
"""

CHAPTERS = []

# ==================== 第一章 Lesson 1-24 ====================

c1s1 = {
    "id": "e-c1-s1",
    "title": "第一节 Lesson 1-6：be 动词 · 一般疑问句 · 物主代词 · 国籍",
    "notes": [
        {
            "point": "be 动词三兄弟 am / is / are 怎么选",
            "explain": "be 动词跟着主语走：主语是 I 用 am；主语是 he / she / it 或单数名词用 is；主语是 you / we / they 或复数名词用 are。口诀：“我用 am，你用 are，is 连着他她它，单数 is，复数 are。”",
            "examples": [
                {"tag": "基础", "text": "I <b>am</b> a student. / This <b>is</b> my pen. / These <b>are</b> my books. —— 三种人称各对应一个 be 动词，一一对上就不会错。"},
                {"tag": "进阶", "text": "两个人并列作主语算复数：Tom and I <b>are</b> late.（不是 am）。但不可数名词算单数：The water <b>is</b> cold. / The news <b>is</b> good.（news 看着像复数，其实是不可数名词）"},
                {"tag": "易错", "text": "“My trousers <u>is</u> blue.” ✗ —— trousers（裤子）、glasses（眼镜）、shoes（鞋）这类成对出现的东西天生是复数，必须用 are：My trousers <b>are</b> blue. ✓ 判断 be 动词要看主语的“数”，不要被中文的“一条裤子”带偏。"}
            ],
            "think": "课本第一课是 “Excuse me, is this your handbag?” —— 如果把 handbag 换成 shoes，整句话有几个地方要改？为什么改一个词会牵动这么多地方？"
        },
        {
            "point": "一般疑问句：把 be 动词提到句首",
            "explain": "含 be 动词的陈述句变一般疑问句，只要把 be 动词提到主语前面，句末改问号，首字母大写。回答用 Yes, 主语 + be. / No, 主语 + be + not.",
            "examples": [
                {"tag": "基础", "text": "This is your book. → <b>Is</b> this your book? ／ You are Chinese. → <b>Are</b> you Chinese?"},
                {"tag": "进阶", "text": "简答时主语要换成代词：Is this your coat? → Yes, <b>it</b> is.（不说 Yes, this is.）；Are you a teacher? → Yes, <b>I</b> am.（不说 Yes, you are.）—— 对方问“你”，你要答“我”。"},
                {"tag": "易错", "text": "肯定简答里的 be 动词<b>不能缩写</b>：Yes, it is. ✓ ／ Yes, it’s. ✗ ／ Yes, I am. ✓ ／ Yes, I’m. ✗ 但否定简答两种缩写都行：No, it isn’t. ＝ No, it’s not."}
            ],
            "think": "为什么 “Yes, I’m.” 是错的，“Yes, I am.” 就对？（提示：想想这句话说出来时，重音落在哪个词上，缩写以后那个词还能重读吗？）"
        },
        {
            "point": "形容词性物主代词 my / your —— 名词前的“谁的”",
            "explain": "my / your / his / her / its / our / their 叫形容词性物主代词，作用相当于形容词，后面<b>必须跟名词</b>，不能单独站着。",
            "examples": [
                {"tag": "基础", "text": "my book（我的书）、your pen（你的笔）、her bag（她的包）—— 后面都拖着一个名词。"},
                {"tag": "进阶", "text": "物主代词和冠词 a / an / the 不能同时出现在一个名词前面：“<u>a my</u> book” ✗ → my book ✓，如果一定要表达“我的一本书”，要说 <b>a book of mine</b>。"},
                {"tag": "易错", "text": "your（你的）和 you’re（you are）读音一模一样，写的时候最容易混。“<u>Your</u> late again!” ✗ 这里要表达“你迟到了”，是 you are 的缩写 → <b>You’re</b> late again! ✓ 判断方法：能还原成 you are 的就写 you’re。"}
            ],
            "think": "中文里“我的书”和“书是我的”用的都是“我的”这两个字，英语却要分成 my book 和 It’s mine，你觉得英语这样分有什么好处？"
        },
        {
            "point": "国籍形容词与国名不是一回事",
            "explain": "国名是名词（China），国籍形容词表示“……国的 / ……国人”（Chinese）。说国籍用 I’m + 国籍形容词；说来自哪里用 I’m from + 国名。两者不能混用。",
            "examples": [
                {"tag": "基础", "text": "China→Chinese，France→French，Germany→German，Japan→Japanese，Italy→Italian，America→American，England→English，Korea→Korean，Russia→Russian，Sweden→Swedish。"},
                {"tag": "进阶", "text": "国名和国籍形容词的首字母<b>永远大写</b>，哪怕它出现在句子中间：He is a <b>Japanese</b> student.（不能写成 japanese）"},
                {"tag": "易错", "text": "两个方向都会错：“I’m from <u>Chinese</u>.” ✗（from 后面要跟国名 China）；“I’m <u>China</u>.” ✗（是“我是中国”的意思，要跟国籍形容词 Chinese）。记法：<b>from 后面跟地方，be 后面跟身份</b>。"}
            ],
            "think": "Lesson 5 里 Robert 说 “I’m Italian.”，Sophie 说 “I’m French.” —— 如果要把 Robert 那句改成“我来自意大利”，句子里有几个词要变？"
        },
        {
            "point": "This is... 介绍句型与 Nice to meet you",
            "explain": "把第三个人介绍给别人时，英语的固定说法是 <b>This is + 姓名</b>，不用 He is / She is。对方回应 Nice to meet you.，你答 Nice to meet you, too.",
            "examples": [
                {"tag": "基础", "text": "在班上介绍新同学：<b>This is</b> Lucy. — Nice to meet you, Lucy. — Nice to meet you, too."},
                {"tag": "进阶", "text": "打电话报自己名字，英语也用 This is，不用 I am：“Hello, <b>this is</b> Tom speaking.” 问对方是谁则用 “Who’s <b>that</b>?”（近处的自己用 this，远处的对方用 that）"},
                {"tag": "易错", "text": "“He is my friend Tom.” 这句<b>语法完全正确</b>，但作为“当面介绍”不地道 —— 当着 Tom 的面用 he 指他，听起来像在背后谈论他。正式介绍固定用 This is Tom. 这是习惯问题，不是对错问题，别把它当成语法错误。"}
            ],
            "think": "打电话时中文说“我是小明”，英语却说 “This is Xiaoming.” —— 你觉得英语在这里为什么不用 I am？（提示：想想对方此刻看不见你，他需要先确认的是“哪个人在说话”还是“你是谁”？）"
        }
    ],
    "quiz": [
        {"id": 1, "type": "multi", "point": "be 动词与主语的数（想一想·刁钻）",
         "stem": "下列句子中，be 动词用得<b>正确</b>的有（　）【多选】",
         "options": ["A. My trousers are new.", "B. Tom and I am students.", "C. The news are good.", "D. These shoes are yours.", "E. My family is big."],
         "answer": ["A", "D", "E"],
         "explain": "A 对：trousers 天生复数用 are。B 错：Tom and I 是两个人，是复数，要用 are。C 错：news 看起来带 s，其实是<b>不可数名词</b>，当单数用 is。D 对：shoes 是复数。E 对：family 作为“一个整体”时当单数，用 is。这题专门测“看起来像复数”和“真的是复数”的区别。"},
        {"id": 2, "type": "choice", "point": "一般疑问句的简答",
         "stem": "—Is this your umbrella?　—____",
         "options": ["A. Yes, this is.", "B. Yes, it is.", "C. Yes, it’s.", "D. Yes, that is."],
         "answer": "B",
         "explain": "简答时主语要换成代词 it，不能重复 this / that，所以 A、D 排除；肯定简答的 be 动词不能缩写，所以 C 错。正确答案是 Yes, it is."},
        {"id": 3, "type": "multi", "point": "简答的缩写规则（想一想·辨析）",
         "stem": "关于 be 动词的简略回答，下列说法<b>正确</b>的有（　）【多选】",
         "options": ["A. 肯定简答里的 be 动词不能缩写", "B. No, it isn’t. 和 No, it’s not. 都是正确的", "C. Is this your book? 应答 Yes, this is.", "D. Are you students? 应答 Yes, we are.", "E. 肯定简答不能缩写，是因为句末的 be 动词要重读"],
         "answer": ["A", "B", "D", "E"],
         "explain": "C 错：简答要用代词 it，不能用 this。其余都对 —— 特别是 E，这正是不能缩写的真正原因：缩写形式（’m / ’s / ’re）读音很轻，没法承担句末的重音。"},
        {"id": 4, "type": "fill", "point": "陈述句变一般疑问句",
         "stem": "把 These are my books. 改成一般疑问句：______ these your books?（填一个词）",
         "answer": ["Are"],
         "explain": "含 be 动词的句子变疑问句，把 be 动词提到句首即可。主语 these 是复数，所以用 Are。"},
        {"id": 5, "type": "choice", "point": "your 与 you’re 辨析（易错）",
         "stem": "____ late again! ____ homework is still on my desk.",
         "options": ["A. You’re; Your", "B. Your; You’re", "C. You’re; You’re", "D. Your; Your"],
         "answer": "A",
         "explain": "第一空要表达“你迟到了”，能还原成 You are，所以用 You’re；第二空后面跟着名词 homework，要用形容词性物主代词 Your。判断诀窍：<b>能还原成 you are 的写 you’re，后面跟名词的写 your</b>。"},
        {"id": 6, "type": "multi", "point": "my 与 mine 的分工（想一想·辨析）",
         "stem": "关于 my 和 mine，下列说法<b>正确</b>的有（　）【多选】",
         "options": ["A. my 后面必须跟名词", "B. mine 后面不能再跟名词", "C. “a my book”是错误的说法", "D. This book is mine. 和 This is my book. 意思相同", "E. mine 可以放在名词前面作定语"],
         "answer": ["A", "B", "C", "D"],
         "explain": "E 错：mine 是名词性物主代词，本身已经等于“我的+名词”，不能再放到名词前面（mine book ✗）。A、B、C、D 都对，其中 C 是因为冠词和物主代词不能同时修饰一个名词，要说 a book of mine。"},
        {"id": 7, "type": "choice", "point": "国名与国籍形容词",
         "stem": "—Where are you from?　—I’m from ____ . I’m ____ .",
         "options": ["A. Japanese; Japan", "B. Japan; Japanese", "C. Japan; Japan", "D. Japanese; Japanese"],
         "answer": "B",
         "explain": "from 后面跟<b>国名</b>（Japan），be 后面跟<b>国籍形容词</b>（Japanese）。记法：from 后面跟地方，be 后面跟身份。"},
        {"id": 8, "type": "judge", "point": "国籍形容词大小写",
         "stem": "国籍形容词（如 chinese、french）只要不在句首，首字母就可以小写。",
         "answer": "错",
         "explain": "错。国名和国籍形容词属于专有名词，<b>无论出现在句子什么位置，首字母都必须大写</b>：He is a Chinese student. 这是英语里少数“位置不影响大小写”的词类之一。"},
        {"id": 9, "type": "fill", "point": "国籍形容词拼写",
         "stem": "France 对应的国籍形容词是 ______",
         "answer": ["French"],
         "explain": "France（法国，国名）→ French（法国的／法国人）。注意它不是在国名后面加后缀，而是整个换了一个词，属于要单独记的一类。"},
        {"id": 10, "type": "multi", "point": "自我介绍的正误（想一想·刁钻）",
         "stem": "下列自我介绍中，<b>没有语病</b>的有（　）【多选】",
         "options": ["A. I’m China.", "B. I’m Chinese.", "C. I come from China.", "D. I’m from Chinese.", "E. I’m a Chinese student."],
         "answer": ["B", "C", "E"],
         "explain": "A 错：意思变成“我是中国（这个国家）”。D 错：from 后面要跟国名 China。B、C 都对，是最常见的两种说法；E 对，Chinese 在这里作定语修饰 student。这题的陷阱在于 A 和 D 分别踩了“该用形容词却用国名”和“该用国名却用形容词”两个相反的坑。"},
        {"id": 11, "type": "choice", "point": "This is 介绍句型",
         "stem": "在班上把新同学 Lucy 介绍给大家，最合适的说法是（　）",
         "options": ["A. She is Lucy.", "B. This is Lucy.", "C. That is Lucy.", "D. It is Lucy."],
         "answer": "B",
         "explain": "当面介绍第三个人，英语的固定说法是 This is + 姓名。A 语法没错但当着本人的面用 she 不礼貌；C 的 that 指远处，介绍身边的人不合适；D 的 it 不能指人。"},
        {"id": 12, "type": "multi", "point": "This is 的用法边界（想一想·刁钻）",
         "stem": "关于 This is... 这个句型，下列说法<b>正确</b>的有（　）【多选】",
         "options": ["A. 当面介绍别人时用 This is + 姓名", "B. 打电话报自己的名字用 This is..., 不用 I am...", "C. This is 只能指物，不能指人", "D. 接电话问对方是谁可以说 Who’s that?", "E. 介绍别人时说 He is my friend Tom. 是语法错误"],
         "answer": ["A", "B", "D"],
         "explain": "C 错：This is 完全可以指人，介绍句型正是最典型的用法。E 是这题最容易上当的选项 —— He is my friend Tom. <b>语法上完全正确</b>，只是当面介绍时不够礼貌、不地道，属于“习惯用法”问题，不能说成“语法错误”。要能分清<b>语法错误</b>和<b>不地道</b>是两回事。"}
    ]
}

c1s2 = {
    "id": "e-c1-s2",
    "title": "第二节 Lesson 7-12：冠词 a/an · 职业 · Whose 与名词所有格",
    "notes": [
        {
            "point": "不定冠词 a / an —— 看读音，不看字母",
            "explain": "a 用在<b>辅音音素</b>开头的单词前，an 用在<b>元音音素</b>开头的单词前。判断标准是这个词<b>读起来</b>的第一个音，不是拼写的第一个字母。",
            "examples": [
                {"tag": "基础", "text": "a book / a pen / a car（辅音开头）　an apple / an egg / an orange / an umbrella（元音开头）"},
                {"tag": "进阶", "text": "两类“表里不一”的词要单独记：<b>an</b> hour、<b>an</b> honest man（h 不发音，实际以元音开头）；<b>a</b> university、<b>a</b> useful book、<b>a</b> European country（拼写是 u，但读音是 /j/，是辅音）。"},
                {"tag": "易错", "text": "“<u>an</u> useful tool” ✗ —— useful 读作 /ˈjuːsfl/，开头的 /j/ 是辅音，要用 a useful tool ✓。反过来 “<u>a</u> hour” ✗ —— hour 读 /ˈaʊə/，h 完全不发音，要用 an hour ✓。<b>凡是 u 和 h 开头的词，都要多想一秒读音。</b>"}
            ],
            "think": "a 和 an 的区别到底是为了什么？试着连着快读 “a apple” 和 “an apple”，哪个更顺口？这能不能解释英语为什么要多造一个 an 出来？"
        },
        {
            "point": "说职业，单数名词前必须加冠词",
            "explain": "表示某人的职业，单数可数名词前一定要加 a / an：I’m <b>a</b> teacher.（不能说 I’m teacher.）主语是复数时不加冠词：We are teachers.",
            "examples": [
                {"tag": "基础", "text": "He is <b>an</b> engineer. ／ She is <b>a</b> nurse. ／ They are <b>students</b>.（复数不加）"},
                {"tag": "进阶", "text": "问职业的固定说法有两个：<b>What’s your job?</b> 和 <b>What do you do?</b>，回答都用 I’m a + 职业。"},
                {"tag": "易错", "text": "“I am <u>teacher</u>.” ✗ 是最典型的中式英语 —— 中文说“我是老师”不用量词，直译过来就漏了冠词。英语规定：<b>单数可数名词前面不能光秃秃</b>，必须有 a / an / the / my 之类的限定词。"}
            ],
            "think": "为什么英语非要说 “a teacher”（一个老师），中文却不用说“一个老师”？如果英语允许说 I’m teacher，会不会产生歧义？"
        },
        {
            "point": "Whose 提问“谁的” + 名词所有格 ’s",
            "explain": "Whose 用来问东西属于谁，有两种语序：<b>Whose is this shirt?</b> ＝ <b>Whose shirt is this?</b> 回答用名词所有格：It’s Tim’s. 单数名词加 ’s；以 s 结尾的复数名词只加一个撇号。",
            "examples": [
                {"tag": "基础", "text": "Tim’s coat（蒂姆的外套）、my mother’s bag（我妈妈的包）、the dog’s tail（那条狗的尾巴）"},
                {"tag": "进阶", "text": "复数所有格看结尾：the students<b>’</b> books（学生们的书，本来就有 s，只加撇号）；不规则复数没有 s，还是加 ’s：the children<b>’s</b> toys、the men<b>’s</b> room。"},
                {"tag": "易错", "text": "whose（谁的）和 who’s（who is 的缩写）读音<b>完全相同</b>，是英语里最经典的同音陷阱。“<u>Who’s</u> book is this?” ✗ → <b>Whose</b> book is this? ✓ 判断方法：能还原成 who is 的才写 who’s。"}
            ],
            "think": "the teacher’s books（一个老师的书）和 the teachers’ books（多个老师的书）读音一模一样，那么说话的时候，英语母语者要怎么让别人听懂到底是几个老师？"
        },
        {
            "point": "形容词性 vs 名词性物主代词",
            "explain": "形容词性（my / your / his / her / its / our / their）后面<b>必须跟名词</b>；名词性（mine / yours / his / hers / ours / theirs）<b>单独使用</b>，本身等于“物主代词 + 名词”。",
            "examples": [
                {"tag": "基础", "text": "This is <b>my</b> pen. ＝ This pen is <b>mine</b>. 两句意思相同，但 my 后面拖着名词，mine 后面什么都不跟。"},
                {"tag": "进阶", "text": "his 是个特例，<b>两种词性长得一样</b>：his book（形容词性）／ It’s his.（名词性）。而 its 几乎从不单独使用，实际上没有常用的名词性形式。"},
                {"tag": "易错", "text": "her 和 hers 最容易混：“This bag is <u>her</u>.” ✗ —— 后面没有名词了，要用名词性的 <b>hers</b>：This bag is hers. ✓ 或者改写成 This is <b>her</b> bag. ✓ 两种都对，但不能混着用。"}
            ],
            "think": "英语里 he 变成 his、she 变成 hers，那为什么 his 不用再变成 “hiss”？这会不会造成理解上的麻烦？"
        },
        {
            "point": "职业词汇与它们的复数",
            "explain": "新概念第一册的核心职业词：engineer（工程师）、nurse（护士）、mechanic（机械师）、keyboard operator（键盘操作员）、policeman / policewoman（警察）、taxi driver（出租车司机）、air hostess（空姐）、hairdresser（理发师）、housewife（家庭主妇）、milkman（送奶工）、postman（邮递员）、shop assistant（店员）。",
            "examples": [
                {"tag": "基础", "text": "—What’s your job?　—I’m <b>a nurse</b>.　—What’s his job?　—He’s <b>a mechanic</b>."},
                {"tag": "进阶", "text": "复数变化要注意：policeman→police<b>men</b>、postman→post<b>men</b>（man 变 men）；housewife→housewi<b>ves</b>（fe 变 ves）；air hostess→air hostess<b>es</b>（ss 结尾加 es）。"},
                {"tag": "易错", "text": "由 man / woman 构成的复合职业名词，变复数时<b>前后两个词都要变</b>：woman doctor → <b>women doctors</b>（不是 woman doctors）；man teacher → <b>men teachers</b>。这是英语里唯一“一个名词变两处”的情况。"}
            ],
            "think": "课本里的 air hostess（空姐）现在更常说成 flight attendant（乘务员）。你能想到这个变化是为了解决什么问题吗？policeman 是不是也有同样的处境？"
        }
    ],
    "quiz": [
        {"id": 1, "type": "choice", "point": "a / an 看读音（易错）",
         "stem": "____ hour later, ____ honest man came in with ____ umbrella.",
         "options": ["A. An; a; an", "B. A; an; a", "C. An; an; an", "D. A; a; an"],
         "answer": "C",
         "explain": "三个词都以元音音素开头，所以全部用 an：hour 的 h 不发音（/ˈaʊə/）、honest 的 h 也不发音（/ˈɒnɪst/）、umbrella 本身就是元音开头。这题专门测“不看字母看读音”。"},
        {"id": 2, "type": "multi", "point": "a / an 的判断标准（想一想·刁钻）",
         "stem": "下列 a / an 的用法<b>正确</b>的有（　）【多选】",
         "options": ["A. an hour", "B. a university", "C. an useful tool", "D. a European country", "E. an honest boy"],
         "answer": ["A", "B", "D", "E"],
         "explain": "C 错：useful 读作 /ˈjuːsfl/，开头的 /j/ 是<b>辅音</b>，要用 a useful tool。B、D 同理，university 和 European 都读 /j/ 开头，用 a。A、E 的 h 都不发音，实际是元音开头，用 an。记住：<b>u 开头常常是辅音，h 开头有时是元音</b>，正好都跟直觉相反。"},
        {"id": 3, "type": "fill", "point": "冠词选择",
         "stem": "填 a 或 an：She is ______ engineer.",
         "answer": ["an"],
         "explain": "engineer 读作 /ˌendʒɪˈnɪə/，以元音音素 /e/ 开头，所以用 an。"},
        {"id": 4, "type": "choice", "point": "职业前的冠词（中式英语陷阱）",
         "stem": "—What’s your job?　—____",
         "options": ["A. I’m teacher.", "B. I’m a teacher.", "C. I teacher.", "D. My job is teacher."],
         "answer": "B",
         "explain": "单数可数名词前不能光秃秃，必须加冠词，所以 A、D 都缺 a；C 连 be 动词都漏了。正确说法是 I’m a teacher."},
        {"id": 5, "type": "multi", "point": "职业表达（想一想·辨析）",
         "stem": "关于用英语说职业，下列说法<b>正确</b>的有（　）【多选】",
         "options": ["A. 单数职业名词前要加 a / an", "B. 复数职业名词前不加 a / an", "C. “I’m teacher.” 是正确的英语", "D. What’s your job? 可以换成 What do you do?", "E. “我们是学生”应该说 We are students."],
         "answer": ["A", "B", "D", "E"],
         "explain": "C 错：漏了冠词，是最典型的中式英语。其余都对。特别注意 B 和 E 的呼应：单数要加冠词，复数反而不能加。"},
        {"id": 6, "type": "choice", "point": "Whose 与 who’s 辨析（同音陷阱）",
         "stem": "____ bag is this? — It’s ____.",
         "options": ["A. Who’s; Tom", "B. Whose; Tom’s", "C. Who’s; Tom’s", "D. Whose; Tom"],
         "answer": "B",
         "explain": "第一空问“谁的包”，用 Whose（who’s 是 who is，代进去变成 “Who is bag is this?”，明显不通）；第二空回答“是汤姆的”，要用名词所有格 Tom’s，光说 Tom 意思变成“它是汤姆”。两个空一个测同音陷阱，一个测所有格。"},
        {"id": 7, "type": "fill", "point": "形容词性变名词性物主代词",
         "stem": "把 It is her bag. 改成同义句：The bag is ______.",
         "answer": ["hers"],
         "explain": "改写后 bag 已经作主语，物主代词后面没有名词了，必须用名词性物主代词 hers。写成 her 是最常见的错误。"},
        {"id": 8, "type": "judge", "point": "同音词的书面区分",
         "stem": "whose 和 who’s 读音相同，所以在书面语里可以互相替换。",
         "answer": "错",
         "explain": "错。读音相同不等于意思相同：whose 是“谁的”（疑问词／限定词），who’s 是 who is 的缩写。书面语中<b>绝对不能互换</b>。检验方法：能还原成 who is 就写 who’s，否则写 whose。"},
        {"id": 9, "type": "multi", "point": "名词所有格规则（想一想·刁钻）",
         "stem": "关于名词所有格，下列说法<b>正确</b>的有（　）【多选】",
         "options": ["A. 单数名词加 ’s", "B. 以 s 结尾的复数名词只加一个撇号", "C. children 是不规则复数，所有格写成 children’s", "D. the teacher’s book 和 the teachers’ book 读音不同", "E. Whose book is this? 和 Whose is this book? 都正确"],
         "answer": ["A", "B", "C", "E"],
         "explain": "D 错，而且这正是这一节最值得注意的地方：the teacher’s 和 the teachers’ <b>读音完全相同</b>，只能靠上下文或改说 the book of the teachers 来区分。C 对：不规则复数没有 s 结尾，所以照常加 ’s。"},
        {"id": 10, "type": "choice", "point": "her 与 hers",
         "stem": "This coat isn’t ____. ____ coat is blue.",
         "options": ["A. her; Hers", "B. hers; Her", "C. hers; Hers", "D. her; Her"],
         "answer": "B",
         "explain": "第一空后面没有名词（句子已经结束），用名词性的 hers；第二空后面跟着名词 coat，用形容词性的 Her。<b>看后面有没有名词</b>是唯一的判断依据。"},
        {"id": 11, "type": "multi", "point": "物主代词两种词性（想一想·辨析）",
         "stem": "关于物主代词，下列说法<b>正确</b>的有（　）【多选】",
         "options": ["A. his 既可以放在名词前，也可以单独使用", "B. its 一般不单独使用", "C. “This is hers book.” 是正确的", "D. mine 相当于 my + 名词", "E. 形容词性物主代词后面必须跟名词"],
         "answer": ["A", "B", "D", "E"],
         "explain": "C 错：hers 已经含有名词的意思，后面不能再跟 book，应说 her book 或 It’s hers。A 对，his 是唯一两种词性同形的物主代词，这也是它容易被忽略的原因。"},
        {"id": 12, "type": "multi", "point": "职业名词的复数（想一想·刁钻）",
         "stem": "下列职业名词的复数形式<b>正确</b>的有（　）【多选】",
         "options": ["A. policeman → policemen", "B. housewife → housewives", "C. woman doctor → woman doctors", "D. woman doctor → women doctors", "E. air hostess → air hostesses"],
         "answer": ["A", "B", "D", "E"],
         "explain": "C 错、D 对：由 man / woman 构成的复合名词变复数时，<b>前后两个词都要变</b>，所以是 women doctors。这是英语里独一份的规则，C 和 D 摆在一起就是为了让你必须想清楚才能选。"}
    ]
}

c1s3 = {
    "id": "e-c1-s3",
    "title": "第三节 Lesson 13-18：What colour · 名词单复数 · 复数句与形容词",
    "notes": [
        {
            "point": "What colour 问颜色",
            "explain": "问颜色的固定句型是 <b>What colour + be + 主语?</b> 主语单数用 is，复数用 are。回答 It’s blue. / They’re blue. colour 是英式拼写，美式写作 color，新概念用英式。",
            "examples": [
                {"tag": "基础", "text": "What colour <b>is</b> your car? — It’s red. ／ What colour <b>are</b> your shoes? — They’re black."},
                {"tag": "进阶", "text": "同义说法：What’s <b>the colour of</b> your bag? 意思一样，但语序完全不同 —— 这时 colour 前面要加 the，后面用 of 连接。"},
                {"tag": "易错", "text": "“What colour <u>your dress is</u>?” ✗ —— 特殊疑问句里，be 动词必须提到主语<b>前面</b>：What colour <b>is your dress</b>? ✓ 中文“你的裙子什么颜色”是“主语在前”，英语是“be 在前”，这个语序差别是所有特殊疑问句的通病。"}
            ],
            "think": "中文问“你的裙子什么颜色？”，疑问词“什么颜色”跑到了句子中间；英语 What colour is your dress? 疑问词却一定在句首。你能总结出英语疑问词位置的规律吗？这条规律对 Whose、Which 也成立吗？"
        },
        {
            "point": "名词复数的变化规则",
            "explain": "① 一般加 -s；② 以 s / x / ch / sh 结尾加 -es；③ 辅音字母 + y 结尾，变 y 为 i 再加 -es；④ 以 f / fe 结尾，多数变 f / fe 为 v 再加 -es；⑤ 一批不规则变化要单独记。",
            "examples": [
                {"tag": "基础", "text": "book→books、bus→bus<b>es</b>、box→box<b>es</b>、watch→watch<b>es</b>、dish→dish<b>es</b>"},
                {"tag": "进阶", "text": "看 y 前面是什么：bab<b>y</b>→bab<b>ies</b>（辅音 b + y）但 bo<b>y</b>→bo<b>ys</b>（元音 o + y）。f/fe 类：knife→kni<b>ves</b>、wife→wi<b>ves</b>、leaf→lea<b>ves</b>。不规则：man→men、woman→women、child→children、foot→feet、tooth→teeth、mouse→mice。"},
                {"tag": "易错", "text": "以 o 结尾的名词<b>不是一律加 es</b>：photo→photo<b>s</b>、piano→piano<b>s</b>、radio→radio<b>s</b>（加 s），但 tomato→tomato<b>es</b>、potato→potato<b>es</b>、hero→hero<b>es</b>（加 es）。口诀：“<b>英雄爱吃土豆西红柿</b>”（hero、potato、tomato 加 es），剩下的多半加 s。"}
            ],
            "think": "sheep（绵羊）、fish（鱼）、Chinese（中国人）的单数和复数长得一模一样。你能想到这类词还有哪些？它们有什么共同点？（提示：想想它们在句子里靠什么来表示“几个”）"
        },
        {
            "point": "复数句的 be 动词与简答",
            "explain": "主语是复数，be 动词用 are，简答用 <b>Yes, they are. / No, they aren’t.</b> 如果对方问的是 you（你们），要用 <b>we</b> 来回答。",
            "examples": [
                {"tag": "基础", "text": "Are these your books? — Yes, <b>they</b> are. ／ Are those your keys? — No, <b>they</b> aren’t."},
                {"tag": "进阶", "text": "英语的 you 既是“你”也是“你们”，全靠上下文判断：Are you a student?（你）→ Yes, <b>I</b> am. ／ Are you students?（你们）→ Yes, <b>we</b> are. <b>看名词的单复数，就能反推 you 指几个人。</b>"},
                {"tag": "易错", "text": "“Are these your keys? — Yes, <u>these</u> are.” ✗ —— 简答一律用人称代词，不能重复 this / that / these / those，要说 Yes, <b>they</b> are. ✓ 这跟单数时不能说 Yes, this is. 是同一条规则。"}
            ],
            "think": "英语的 you 既是“你”又是“你们”，那么当有人对你说 “Are you ready?” 时，你怎么判断他是在问你一个人，还是在问你们全组？"
        },
        {
            "point": "形容词的位置：定语在名词前，表语在 be 后",
            "explain": "形容词有两个位置：修饰名词时放在名词<b>前面</b>（作定语），描述主语状态时放在 be 动词<b>后面</b>（作表语）。英语的形容词<b>永远不变复数</b>。",
            "examples": [
                {"tag": "基础", "text": "a <b>red</b> car（定语，在名词前）／ The car is <b>red</b>.（表语，在 be 后）—— 同一个形容词，两个位置，意思相通。"},
                {"tag": "进阶", "text": "有冠词时的固定语序是 <b>冠词 + 形容词 + 名词</b>：a beautiful girl ✓（不是 beautiful a girl）。变复数时冠词要去掉：a new dress → new dress<b>es</b>。"},
                {"tag": "易错", "text": "“The dresses are <u>news</u>.” ✗ —— 形容词不跟着名词变复数，也不加 s：The dresses are <b>new</b>. ✓（顺便一提，news 是另一个词，意思是“新闻”，加了 s 意思就变了。）"}
            ],
            "think": "英语的形容词不随名词变复数，但法语、西班牙语的形容词要跟着名词变。对学英语的人来说，这算是省事还是麻烦？如果英语也要变，你觉得会多出多少要背的东西？"
        },
        {
            "point": "表示状态的形容词：tired / thirsty / hungry / hot / cold",
            "explain": "表达“我累了 / 渴了 / 饿了”，英语用 <b>be + 形容词</b>，不用动词。中文的“了”在英语里没有对应的词，状态本身就由 be + 形容词表示。",
            "examples": [
                {"tag": "基础", "text": "I’m <b>tired</b>.（我累了）／ I’m <b>thirsty</b>.（我渴了）／ She’s <b>cold</b>.（她冷）"},
                {"tag": "进阶", "text": "加强语气用 very / so 放在形容词前：I’m <b>very</b> tired. ／ I’m <b>so</b> hungry. 注意 very 修饰的是形容词，不能修饰动词。"},
                {"tag": "易错", "text": "两个方向都会错：“I <u>very</u> tired.” ✗ 漏了 be 动词 → I’m very tired. ✓；“I <u>have</u> hungry.” ✗ 用错了动词 → I’m hungry. ✓ 只要形容词作表语，前面就一定要有 be。"}
            ],
            "think": "中文说“我热”和“天气热”都用同一个“热”字，英语却是 I’m hot. 和 It’s hot. —— 这两句在英语里的含义差别有多大？如果想说“天气很热”却说成 I’m hot.，别人会理解成什么？"
        }
    ],
    "quiz": [
        {"id": 1, "type": "choice", "point": "What colour 的语序",
         "stem": "____ your new shoes? — They’re white.",
         "options": ["A. What colour is", "B. What colour are", "C. What is colour", "D. What are colour"],
         "answer": "B",
         "explain": "主语 shoes 是复数，be 动词用 are；疑问词 What colour 作为一个整体放句首，后面紧跟 be。C、D 把 colour 拆开了，语序错误。"},
        {"id": 2, "type": "multi", "point": "特殊疑问句语序（想一想·刁钻）",
         "stem": "下列问句中<b>正确</b>的有（　）【多选】",
         "options": ["A. What colour is your bag?", "B. What colour your bag is?", "C. What colour are these socks?", "D. What’s the colour of your bag?", "E. What colour do your bag?"],
         "answer": ["A", "C", "D"],
         "explain": "B 错：特殊疑问句里 be 动词必须提到主语前面。E 错：句中有 be 动词就不能再用助动词 do。D 是另一种正确说法，注意它的结构完全不同：What’s <b>the colour of</b> + 名词，colour 前面要加 the。"},
        {"id": 3, "type": "fill", "point": "以 o 结尾的名词复数",
         "stem": "photo 的复数形式是 ______",
         "answer": ["photos"],
         "explain": "photo 属于“加 s”的那一类（photos、pianos、radios）。只有 hero、potato、tomato 这几个常用词加 es，口诀是“英雄爱吃土豆西红柿”。"},
        {"id": 4, "type": "choice", "point": "复数拼写综合（刁钻）",
         "stem": "下列复数形式<b>全部正确</b>的一组是（　）",
         "options": ["A. tomatos, knifes, childs", "B. tomatoes, knives, children", "C. tomatoes, knifes, childrens", "D. tomatos, knives, children"],
         "answer": "B",
         "explain": "tomato→tomato<b>es</b>（英雄爱吃土豆西红柿）；knife→kni<b>ves</b>（fe 变 ves）；child→child<b>ren</b>（不规则，且 children 本身已是复数，不能再加 s）。这题三个词各考一条规则，错一个就全错。"},
        {"id": 5, "type": "multi", "point": "单复数同形的名词（想一想·辨析）",
         "stem": "关于名词的单复数，下列说法<b>正确</b>的有（　）【多选】",
         "options": ["A. sheep 单复数同形", "B. fish 表示“鱼的种类”时可以用 fishes", "C. Chinese 单复数同形", "D. baby 的复数是 babys", "E. Japanese 单复数同形"],
         "answer": ["A", "B", "C", "E"],
         "explain": "D 错：baby 是“辅音字母 b + y”结尾，要变 y 为 i 再加 es，写成 bab<b>ies</b>；boy 是“元音 o + y”，才直接加 s 写成 boys。B 是个容易被误判的知识点：fish 一般单复数同形，但强调“不同种类的鱼”时确实可以说 fishes。"},
        {"id": 6, "type": "judge", "point": "以 o 结尾的复数规则",
         "stem": "以字母 o 结尾的名词，变复数时一律加 -es。",
         "answer": "错",
         "explain": "错。photo→photos、piano→pianos、radio→radios 都只加 s。只有 hero、potato、tomato 这一小批加 es。“一律”“都”“永远”这类绝对化的说法，在语法题里往往是错的信号。"},
        {"id": 7, "type": "choice", "point": "you 的单复数与简答",
         "stem": "—Are you teachers?　—____",
         "options": ["A. Yes, you are.", "B. Yes, we are.", "C. Yes, they are.", "D. Yes, I am."],
         "answer": "B",
         "explain": "teachers 是复数，说明这里的 you 是“你们”，所以回答要用 we。如果问的是 Are you a teacher?（单数），才答 Yes, I am. <b>看名词的单复数就能判断 you 指几个人</b>，这是这一节最实用的技巧。"},
        {"id": 8, "type": "multi", "point": "be 动词简答规则（想一想·辨析）",
         "stem": "关于 be 动词的简略回答，下列说法<b>正确</b>的有（　）【多选】",
         "options": ["A. Are these your books? 答 Yes, they are.", "B. Are these your books? 答 Yes, these are.", "C. Are you students? 可以答 Yes, we are.", "D. Are you a student? 答 Yes, I am.", "E. 简答的肯定形式不能缩写"],
         "answer": ["A", "C", "D", "E"],
         "explain": "B 错：简答一律用人称代词 they，不能重复指示代词 these。A 与 B 是一对，专门测这条规则；C 与 D 是一对，测 you 的单复数判断。"},
        {"id": 9, "type": "fill", "point": "形容词作定语时的冠词",
         "stem": "补全“一条新裙子”：______ new dress（填一个词）",
         "answer": ["a"],
         "explain": "语序是<b>冠词 + 形容词 + 名词</b>，new 以辅音音素 /n/ 开头，所以用 a。注意冠词放在最前面，不能说 new a dress。"},
        {"id": 10, "type": "choice", "point": "形容词位置与形态（易错）",
         "stem": "下列句子<b>没有错误</b>的是（　）",
         "options": ["A. The dresses are news.", "B. They are new dresses.", "C. They are dresses new.", "D. The dress is a new."],
         "answer": "B",
         "explain": "A 错：形容词不变复数，new 不能加 s（news 是“新闻”，另一个词）。C 错：形容词作定语要放名词<b>前面</b>。D 错：形容词作表语时前面不加冠词。只有 B 完全正确。"},
        {"id": 11, "type": "multi", "point": "英语形容词的特点（想一想·辨析）",
         "stem": "关于英语的形容词，下列说法<b>正确</b>的有（　）【多选】",
         "options": ["A. 作定语时放在名词前面", "B. 作表语时放在 be 动词后面", "C. 形容词要像名词一样变复数", "D. a beautiful girl 的语序是正确的", "E. 形容词前面可以加 very 加强语气"],
         "answer": ["A", "B", "D", "E"],
         "explain": "C 错：这正是英语比法语、西班牙语省事的地方 —— 英语形容词<b>永远不变形</b>，不管前面的名词是单数还是复数。这也是中国学生反而容易多加一个 s 的原因。"},
        {"id": 12, "type": "multi", "point": "be + 形容词表状态（想一想·刁钻）",
         "stem": "关于 “I’m hot.” 这句话，下列说法<b>正确</b>的有（　）【多选】",
         "options": ["A. 它表示“我觉得热”", "B. 描述天气热应该说 It’s hot.", "C. 表示“我累了”是 I’m tired.，不能说 I very tired.", "D. 表示“我渴了”可以说 I have thirsty.", "E. 中文的“了”在这类句子里，英语没有对应的词"],
         "answer": ["A", "B", "C", "E"],
         "explain": "D 错：have 是实义动词，后面不能直接跟形容词，应该说 I’m thirsty. 这题的关键是 A 和 B 的对比 —— 主语是人就是“人觉得热”，主语是 it 才是“天气热”，说错了含义会完全跑偏。"}
    ]
}

c1s4 = {
    "id": "e-c1-s4",
    "title": "第四节 Lesson 19-24：指示代词 · 人称代词宾格 · give sb sth · 祈使句",
    "notes": [
        {
            "point": "指示代词 this / that / these / those",
            "explain": "this（这个，近）的复数是 these（这些）；that（那个，远）的复数是 those（那些）。<b>近用 this/these，远用 that/those；单数用 this/that，复数用 these/those。</b>",
            "examples": [
                {"tag": "基础", "text": "This is a book. → <b>These are books.</b> ／ That is a car. → <b>Those are cars.</b>"},
                {"tag": "进阶", "text": "由单数改复数要<b>三处同时改</b>：① 指示代词 this→these ② be 动词 is→are ③ 名词加复数，同时<b>去掉冠词 a / an</b>。例：This is a box. → These are boxes.（a 消失了，box 变 boxes）"},
                {"tag": "易错", "text": "改复数最常见的是“只改一半”：“<u>These is</u> my books.” ✗（be 没改）／“These are <u>book</u>.” ✗（名词没改）／“These are <u>a</u> books.” ✗（冠词没去掉）。改一个词要牵动三个地方，动手前先在心里点一遍。"}
            ],
            "think": "打电话时说 “This is Tom.” 用的也是 this，可是电话那头的人明明离你很远 —— 英语为什么不用 that？（提示：this 指的到底是“离听话人近”还是“离说话人近”？）"
        },
        {
            "point": "Which 提问“哪一个”",
            "explain": "Which 用在<b>有限的、已知的范围</b>里做选择；What 用在<b>开放的、无限的范围</b>里提问。Which 后面可以直接跟名词，中间不加冠词。",
            "examples": [
                {"tag": "基础", "text": "<b>Which</b> is your coat? — The blue one. ／ <b>Which book</b> do you want? — The big one."},
                {"tag": "进阶", "text": "回答 Which 的问句时，常用 <b>one / ones</b> 代替重复的名词：the red <b>one</b>（单数）／ the big <b>ones</b>（复数），避免把名词再说一遍。"},
                {"tag": "易错", "text": "“<u>Which the book</u> do you want?” ✗ —— Which 本身已经起限定作用，后面跟名词时<b>不能再加冠词</b>：Which book ✓。另外别把 Which 和 What 混用：桌上摆着三本书问“要哪本”，用 Which；完全没有范围问“你想看什么书”，用 What。"}
            ],
            "think": "问“你想喝什么？”和“你想喝哪一杯？”，英语要分别用 What 和 Which，中文却都可以说“哪个”。这说明英语在提问时比中文更在意什么？"
        },
        {
            "point": "人称代词的主格与宾格",
            "explain": "<b>主格</b>（I / you / he / she / it / we / they）作主语，放在动词前面；<b>宾格</b>（me / you / him / her / it / us / them）作宾语，放在动词或介词后面。",
            "examples": [
                {"tag": "基础", "text": "<b>I</b> love <b>him</b>.（我爱他）／ <b>He</b> loves <b>me</b>.（他爱我）—— 同样两个人，位置一换，形式就跟着换。"},
                {"tag": "进阶", "text": "<b>介词后面一律用宾格</b>：Look at <b>them</b>! ／ Give it to <b>her</b>. ／ between you and <b>me</b>. 只有 you 和 it 的主格宾格长得一样，其余六个都要变。"},
                {"tag": "易错", "text": "“Look at <u>they</u>!” ✗ → Look at <b>them</b>! ✓ 还有一个连很多英语母语者都说错的：“between you and <u>I</u>” ✗ → between you and <b>me</b> ✓（between 是介词，后面必须跟宾格，哪怕中间夹着 you and 也一样）。"}
            ],
            "think": "中文里的“我”在“我打他”和“他打我”里长得一模一样，全靠位置区分；英语却要变成 I 和 me。你觉得英语这样做，对理解长句子有什么帮助？"
        },
        {
            "point": "双宾语句型 give sb sth",
            "explain": "give 后面可以带两个宾语：<b>give + 人 + 物</b>（Give me a book.），也可以换成 <b>give + 物 + to + 人</b>（Give a book to me.）。两种说法意思相同。",
            "examples": [
                {"tag": "基础", "text": "Give <b>me a book</b>. ＝ Give <b>a book to me</b>. ／ Give <b>him the pen</b>. ＝ Give <b>the pen to him</b>."},
                {"tag": "进阶", "text": "有一条硬限制：当“物”是代词 it / them 时，<b>只能用 give it to me 这种形式</b>，不能说 give me it。原因是英语不喜欢把两个短代词硬挤在一起。"},
                {"tag": "易错", "text": "“Give <u>to me</u> a book.” ✗ —— 用了 to 就必须把“物”放中间：Give a book to me. ✓ 或者干脆不用 to：Give me a book. ✓ <b>to 和“人在前”这两种结构不能混着用。</b>"}
            ],
            "think": "课本 Lesson 22 反复练 “Give me / him / her / them a ...” —— 为什么这一串人称代词全都是宾格形式？如果这里用了主格会怎么样？"
        },
        {
            "point": "祈使句：动词原形开头",
            "explain": "祈使句表示命令、请求或建议，主语 you 被省略，直接用<b>动词原形</b>开头。否定形式是 <b>Don’t + 动词原形</b>。加 please 可以让语气更客气。",
            "examples": [
                {"tag": "基础", "text": "Come in. ／ Sit down, please. ／ Look at the blackboard. ／ <b>Don’t</b> run in the corridor."},
                {"tag": "进阶", "text": "be 动词的祈使句要用原形 <b>Be</b>：Be quiet!（安静点！）／ Be careful! ／ 否定说 <b>Don’t be</b> late!（不能说 Aren’t late 或 Are quiet）"},
                {"tag": "易错", "text": "“<u>Don’t late</u>.” ✗ 漏了 be —— late 是形容词，前面必须有动词：Don’t <b>be</b> late. ✓ 另一个：“<u>Please to come in</u>.” ✗ —— please 后面直接跟动词原形：Please <b>come</b> in. ✓"}
            ],
            "think": "课本里的 “Come along, Dan.” 和 “Look at them!” 都没有主语，直接命令 —— 这样说会不会显得没礼貌？如果想客气一点，有哪几种办法可以软化祈使句的语气？"
        }
    ],
    "quiz": [
        {"id": 1, "type": "choice", "point": "单数句改复数（三处同改）",
         "stem": "把 This is an old car. 变成复数形式，正确的是（　）",
         "options": ["A. These is old cars.", "B. These are old cars.", "C. These are an old cars.", "D. This are old cars."],
         "answer": "B",
         "explain": "要同时改三处：this→these、is→are、car→cars，并且<b>去掉冠词 an</b>。A 漏改 be 动词，C 没去掉冠词，D 没改指示代词。只有 B 三处齐全。"},
        {"id": 2, "type": "multi", "point": "指示代词用法（想一想·辨析）",
         "stem": "关于 this / that / these / those，下列说法<b>正确</b>的有（　）【多选】",
         "options": ["A. this 的复数形式是 these", "B. that 的复数形式是 those", "C. 由单数改复数时 be 动词也要跟着改", "D. 打电话自我介绍用 This is...", "E. “These are book.” 是正确的"],
         "answer": ["A", "B", "C", "D"],
         "explain": "E 错：these 是复数，后面的名词必须也变复数，应为 These are books. D 对，这也是 this 的一个特殊用法 —— 打电话时说话人指的是“靠近自己的这个声音”，所以用 this 而不是 that。"},
        {"id": 3, "type": "fill", "point": "不规则复数拼写",
         "stem": "That is a knife. 改成复数：Those are ______.",
         "answer": ["knives"],
         "explain": "knife 以 fe 结尾，变复数要把 fe 改成 v 再加 es，写成 knives。同类词还有 wife→wives、leaf→leaves。"},
        {"id": 4, "type": "choice", "point": "Which 与 one",
         "stem": "____ is your umbrella? — The black ____.",
         "options": ["A. What; one", "B. Which; one", "C. Which; it", "D. What; ones"],
         "answer": "B",
         "explain": "在几把伞里选一把，范围有限，用 Which；回答时用 one 代替已经出现过的名词 umbrella。C 的 it 特指“那一把”，不能跟形容词 black 连用；D 的 ones 是复数，跟单数问句不匹配。"},
        {"id": 5, "type": "multi", "point": "Which 与 What 的分工（想一想·辨析）",
         "stem": "关于 Which 和 What，下列说法<b>正确</b>的有（　）【多选】",
         "options": ["A. Which 用于在有限范围内选择", "B. What 用于开放范围提问", "C. Which 后面可以直接跟名词", "D. 回答 Which 的问句常用 one / ones 代替名词", "E. “Which the book do you want?” 语序正确"],
         "answer": ["A", "B", "C", "D"],
         "explain": "E 错：Which 本身已经有限定作用，后面跟名词时不能再加冠词 the，应为 Which book do you want?"},
        {"id": 6, "type": "choice", "point": "主格与宾格",
         "stem": "Look at ____! ____ are my friends.",
         "options": ["A. they; Them", "B. them; They", "C. them; Them", "D. they; They"],
         "answer": "B",
         "explain": "第一空在介词 at 后面，必须用宾格 them；第二空作句子的主语，必须用主格 They。<b>介词后面用宾格、作主语用主格</b>，两条规则在同一题里各考一次。"},
        {"id": 7, "type": "judge", "point": "介词后的代词形式",
         "stem": "介词后面的人称代词要用主格。",
         "answer": "错",
         "explain": "错，正好相反：<b>介词后面一律用宾格</b>。Look at them. ✓ ／ Give it to her. ✓ ／ between you and me. ✓ 最后一个连很多母语者都会说成 between you and I，那是错的。"},
        {"id": 8, "type": "multi", "point": "人称代词规则（想一想·辨析）",
         "stem": "关于人称代词，下列说法<b>正确</b>的有（　）【多选】",
         "options": ["A. 主格作句子的主语", "B. 宾格作动词或介词的宾语", "C. “Look at they!” 是正确的", "D. between you and me 是正确的", "E. it 的主格和宾格形式相同"],
         "answer": ["A", "B", "D", "E"],
         "explain": "C 错：介词 at 后面要用宾格 them。E 对，这是个容易被忽略的点 —— 八个人称代词里，只有 <b>you 和 it</b> 的主格宾格长得一样，其余六个都要变形。"},
        {"id": 9, "type": "fill", "point": "双宾语的两种结构互换",
         "stem": "Give the book to me. 改成同义句：Give ______ the book.",
         "answer": ["me"],
         "explain": "去掉 to 之后，“人”要挪到 give 的正后面，且必须用宾格 me。两种结构：give + 人 + 物 ＝ give + 物 + to + 人。"},
        {"id": 10, "type": "multi", "point": "give 的双宾语限制（想一想·刁钻）",
         "stem": "关于 give 的双宾语用法，下列说法<b>正确</b>的有（　）【多选】",
         "options": ["A. Give me a pen. 是正确的", "B. Give a pen to me. 是正确的", "C. Give it to me. 是正确的", "D. Give me it. 是最地道的说法", "E. Give to me a pen. 是正确的"],
         "answer": ["A", "B", "C"],
         "explain": "D 错：当“物”是代词 it / them 时，英语<b>只用 give it to me</b>，Give me it. 虽然偶尔听得到，但绝不是“最地道”的说法。E 错：用了 to 就必须把物放中间。D 是本题最有迷惑性的选项，因为它看起来只是 A 的代词版。"},
        {"id": 11, "type": "choice", "point": "祈使句的否定与 be",
         "stem": "下列祈使句<b>正确</b>的是（　）",
         "options": ["A. Don’t late.", "B. Don’t be late.", "C. Are quiet!", "D. Please to sit down."],
         "answer": "B",
         "explain": "A 漏了 be（late 是形容词，不能直接跟在 don’t 后面）；C 错，be 动词的祈使句用原形 Be quiet!，不用 Are；D 错，please 后面直接跟动词原形，不加 to。"},
        {"id": 12, "type": "multi", "point": "祈使句的构成与语气（想一想·刁钻）",
         "stem": "关于祈使句，下列说法<b>正确</b>的有（　）【多选】",
         "options": ["A. 用动词原形开头，省略主语 you", "B. 否定形式是 Don’t + 动词原形", "C. be 动词的祈使句写作 Be quiet!", "D. 句首或句末加 please 可以让语气更礼貌", "E. 祈使句一定不礼貌，正式场合绝对不能用"],
         "answer": ["A", "B", "C", "D"],
         "explain": "E 错：祈使句本身<b>不带感情色彩</b>，礼貌与否取决于语气、please 和上下文。“Please have a seat.”“Enjoy your meal.” 都是正式又礼貌的祈使句。把语法结构和礼貌程度画等号，是这题要破除的误解。"}
    ]
}

CHAPTERS.append({
    "id": "e-c1",
    "title": "第一章 Lesson 1-24：入门核心（be 动词 · 冠词 · 代词）",
    "sections": [c1s1, c1s2, c1s3, c1s4]
})

DATA = {"chapters": CHAPTERS}
