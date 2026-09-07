// 功能：造句语法检查器的闭环测试（在 words.html 里直接跑 checkGrammar）
// 用法：node build/tests_grammar.js
// ⭐ 为什么要有：孩子没有判断能力，造句这关必须由系统判对错。
//    这个测试有两半——错句必须被抓到（否则孩子把错的当对的），
//    正确句必须零误报（否则孩子把对的当错的记，更伤）。
const fs = require('fs');
const src = fs.readFileSync('words.html', 'utf8');

// 把页面里的检查器和它依赖的 DATA 抽出来单独跑
const dataM = src.match(/const DATA = ([\s\S]*?);\n/);
const chkM  = src.match(/\/\* ========== 英语句子语法检查器[\s\S]*?(?=\/\* ========== 路由)/);
if (!dataM || !chkM) { console.log('❌ 抽不出 DATA 或检查器'); process.exit(1); }
const sandbox = { DATA: eval('(' + dataM[1] + ')') };
const fn = new Function('DATA', chkM[0] + '\nreturn checkGrammar;');
const checkGrammar = fn(sandbox.DATA);

const ERR = [
  ['Excuse me, where is you book?',      '物主代词'],
  ['Is this you handbag?',               '物主代词'],
  ['This is me handbag on the table.',   '物主代词'],
  ['He like apples very much.',          '三单漏 s'],
  ['She go to school every morning.',    '三单漏 s'],
  ['He have two brothers.',              '三单漏 s'],
  ['I is a student here.',               'I 配 am'],
  ['They is very happy today.',          '复数配 are'],
  ['Does he likes coffee every day?',    'does 后要原形'],
  ['Did he went to school yesterday?',   'did 后要原形'],
  ["He doesn't likes coffee at all.",    "doesn't 后要原形"],
  ['He can swims very fast now.',        '情态后要原形'],
  ['I am go to school every day.',       'be+原形'],
  ['I have a apple in my bag.',          'a→an'],
  ['She is an teacher in our school.',   'an→a'],
  ["I don't never go there alone.",      '双重否定'],
  ['I very like this new book.',         'very 修饰动词'],
  ['Although he is old, but he is strong.', 'although+but'],
  ['The the book is on my desk.',        '重复词'],
  ['excuse me can you help me',          '大小写+标点'],
  // 缺 be 动词（这一条的保险条件调过好几轮，边界全锁在下面 OK 列表里）
  ['My father a doctor.',                '缺 be'],
  ['I a student in this school.',        '缺 be'],
  ['He my best friend here.',            '缺 be'],
  ['Her mother a nurse here.',           '缺 be'],
];
const OK = [
  'Excuse me, where is your book?', 'Is this your handbag?', 'This is my handbag on the table.',
  'He likes apples very much.', 'She goes to school every morning.', 'He has two brothers.',
  'I am a student here.', 'They are very happy today.', 'Does he like coffee every day?',
  'Did he go to school yesterday?', "He doesn't like coffee at all.", 'He can swim very fast now.',
  'I go to school every day.', 'I have an apple in my bag.', 'She is a teacher in our school.',
  'I never go there alone at night.', 'I like this new book very much.',
  'Although he is old, he is strong.', 'The book is on my desk.', 'Excuse me, can you help me?',
  // 逗号后的称呼不能被当成「你的先生」
  'The waiter said thank you, sir.', 'Sorry, sir, this is not your coat.',
  'Good morning, sir, may I help you?',
  // 原形和过去式同形的动词不能被当成「漏 s」
  'She put her keys into the handbag.', 'He read a book last night.',
  // 全册例句抽样：一条都不能被判错
  'My father wears an old gold watch.', 'Please lend me your pencil for a minute.',
  'Take your umbrella because it may rain.', 'Their daughter plays the piano very well.',
  'The children come home from school at four.', 'Is this your handbag on the chair?',
  'We live in a big white house.', 'My uncle bought a small red car.',
  'Here is my ticket and my passport.', 'A large number of students came here.',
  'She is the daughter of a famous doctor.', 'I write my homework with a pen.',
  'He washed his dirty shirt this morning.', 'Thank you very much, that was really kind.',
  'Mr. Green has one son and two daughters.', 'My little brother is only five years old.',
  // ↓ 以下每一条都是实测撞出来的误报，修完锁在这里防回退
  'He cannot find his tie this morning.',      // 动词是 find，cannot 不在情态词表里
  'Is this your handbag?',                     // be 在句首（疑问句）
  'I share a room with my sister.',            // share 不在动词表里，但不能因此判「缺 be」
  'American English sounds a little different.',// sounds 曾被判成「没有动词」
  'We spent two weeks in Italy.',              // spent 同上
  'The kitchen looks very clean today.',       // very clean 是对的（clean 也是形容词）
  'The bus stopped in front of us.',
  'He likes this excuse very much.',           // this 是限定词不是主语，excuse 是名词
  'Is this your coat or her coat?',            // her 本身就是物主代词
  'The cat caught a mouse last night.',        // caught 是 catch 的变形
  'He is the tallest boy in our class.',       // tallest 是 tall 的变形
];

let fails = 0;
const errs = s => checkGrammar(s).filter(x => x.level === 'error');

console.log('--- 错句必须被抓到（漏报 = 孩子把错的当对的）---');
ERR.forEach(([s, why]) => {
  const r = errs(s);
  if (!r.length) { console.log('  ❌ 漏报 [' + why + ']  ' + s); fails++; }
});
console.log('  ' + (ERR.length - fails) + '/' + ERR.length + ' 抓到');

const fpBefore = fails;
console.log('--- 正确句必须零误报（误报 = 孩子把对的当错的记，更伤）---');
OK.forEach(s => {
  const r = errs(s);
  if (r.length) { console.log('  ❌ 误报  ' + s + '  → ' + r.map(x => x.why.replace(/<[^>]+>/g, '')).join('；')); fails++; }
});
console.log('  ' + (OK.length - (fails - fpBefore)) + '/' + OK.length + ' 零误报');

// 全册例句一条都不能被判错（例句是标准答案，判错说明检查器有问题）
console.log('--- 全册例句自检（' + '例句本身是范例，被判错就是检查器的锅' + '）---');
let egBad = 0;
sandbox.DATA.units.forEach(u => u.sections.forEach(x => x.words.forEach(w => {
  w.egs.forEach(e => { const r = errs(e); if (r.length) { console.log('  ❌ ' + e + ' → ' + r.map(y => y.why.replace(/<[^>]+>/g, '')).join('；')); egBad++; } });
})));
const nEg = sandbox.DATA.units.reduce((a,u)=>a+u.sections.reduce((b,x)=>b+x.words.length*3,0),0);
console.log('  ' + (nEg - egBad) + '/' + nEg + ' 例句通过检查器');
fails += egBad;

// 检查器必须真的接进了造句流程
const wired = /const issues = checkGrammar\(s\)/.test(src) && /检查通过/.test(src);
if (!wired) { console.log('  ❌ 检查器没有接进 makeCheck'); fails++; }
else console.log('--- 检查器已接进造句判分流程 ✅');
if (/都核对过，没问题/.test(src)) { console.log('  ❌ 还留着「你自己核对」式自评'); fails++; }

console.log(fails ? '\n❌ 失败 ' + fails + ' 项' : '\n全部通过');
process.exit(fails ? 1 : 0);
