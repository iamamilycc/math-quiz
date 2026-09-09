// 功能：造句写错时，系统要直接给出「改好应该是这样」的完整句子
// 用法：node build/tests_autofix.js
// ⭐ 为什么：孩子看不懂「三单要加 s」也能照着改好的句子抄一遍，边抄边记。
const fs = require('fs');
const src = fs.readFileSync('words.html', 'utf8');
const data = src.match(/const DATA = ([\s\S]*?);\n/);
const chk  = src.match(/\/\* ========== 英语句子语法检查器[\s\S]*?(?=\/\* 把检查器)/);
const fix  = src.match(/\/\* 把检查器查到的错自动改好[\s\S]*?\n\}/);
const ns   = src.match(/function normSent\(s\) \{[\s\S]*?\n\}/);
if (!data || !chk || !fix || !ns) { console.log('❌ 抽不出检查器或 autoFix'); process.exit(1); }
const api = new Function('DATA', 'const GRAMMAR_WORDS = DATA.units.reduce((a,u)=>a.concat(u.sections.reduce((b,x)=>b.concat(x.words.map(w=>({w:w.w,pos:w.pos}))),[])),[]);\n' + chk[0] + '\n' + fix[0] + '\n' + ns[0] +
                         '\nreturn {checkGrammar, autoFix};')(eval('(' + data[1] + ')'));

const CASES = [
  // ⭐ iPad 的智能标点会把 ' 变成 ’，autoFix 也必须能改（否则「改好应该是这样」原样吐回来）
  ['I don\u2019t never go there.',      'I never go there.'],
  ['He doesn\u2019t likes coffee.',     "He doesn't like coffee."],
  ['He can\u2019t swims.',              "He can't swim."],
  ['She have two brothers.',            'She has two brothers.'],
  ['He like apples very much.',         'He likes apples very much.'],
  ['My sister study English every day.','My sister studies English every day.'],
  ['my father work in a bank',          'My father works in a bank.'],
  ['I have a apple in my bag.',         'I have an apple in my bag.'],
  ['She is an teacher in our school.',  'She is a teacher in our school.'],
  ['This is you book.',                 'This is your book.'],
  ['I very like this book.',            'I like this book very much.'],
  ['He goed to school yesterday.',      'He went to school yesterday.'],
  ['There is many books on the desk.',  'There are many books on the desk.'],
  ["I don't never go there.",           'I never go there.'],
  ['I am go to school every day.',      'I go to school every day.'],
  ['Does he likes coffee?',             'Does he like coffee?'],
  ['Did he went to school yesterday?',  'Did he go to school yesterday?'],
  ['The the book is on my desk.',       'The book is on my desk.'],
  ['i is a student',                    'I am a student.'],
  ['They is very happy today.',         'They are very happy today.'],
];
let fails = 0;
CASES.forEach(([s, exp]) => {
  const errs = api.checkGrammar(s).filter(x => x.level === 'error');
  const got = api.autoFix(s, errs);
  if (got !== exp) { console.log('  ❌ ' + s + '\n       得到：' + got + '\n       期望：' + exp); fails++; }
});
console.log('  ' + (CASES.length - fails) + '/' + CASES.length + ' 条自动改对');

// 正确的句子不能被 autoFix 改坏
const OK = ['He likes apples very much.', 'I have an apple in my bag.', 'This is your book.',
            'There are many books on the desk.', 'She put her keys into the handbag.',
            'My father wears an old gold watch.', 'Excuse me, is this your handbag?'];
OK.forEach(s => {
  const errs = api.checkGrammar(s).filter(x => x.level === 'error');
  const got = api.autoFix(s, errs);
  if (got !== s) { console.log('  ❌ 把对的句子改坏了：' + s + ' → ' + got); fails++; }
});
console.log('  ' + OK.length + ' 条正确句未被改动');

// 界面要真的把改好的句子显示出来
if (!/改好应该是这样/.test(src)) { console.log('  ❌ 界面没有显示「改好应该是这样」'); fails++; }
if (!/欧美人平常会这样说/.test(src)) { console.log('  ❌ 界面没有「欧美人会这样说」'); fails++; }
console.log(fails ? '\n❌ 失败 ' + fails + ' 项' : '\n全部通过');
process.exit(fails ? 1 : 0);
