// 功能：造句写错时的「欧美人会怎么说」这一层的闭环测试
// 用法：node build/tests_native.js
// ⭐ 为什么要有：孩子写错了当场就要看到地道说法，而这一层**不能依赖 AI Key**。
//    两半：该报的必须报到（中式英语条目自测），不该报的一条都不能报
//    （误报＝把孩子本来对的说法说成中式英语，比漏报更伤）。
const fs = require('fs');
const src = fs.readFileSync('words.html', 'utf8');
const dataM = src.match(/const DATA = ([\s\S]*?);\n/);
// 连语法检查器一起抽出来：fix() 改好的句子必须自己也能过语法检查
const blkM  = src.match(/\/\* ========== 英语句子语法检查器[\s\S]*?(?=\/\* 把检查器)/);
if (!dataM || !blkM) { console.log('❌ 抽不出 DATA 或搭配表'); process.exit(1); }
const DATA = eval('(' + dataM[1] + ')');
const api = new Function('DATA', 'const esc = x => x, speak = () => {};\n' + blkM[0] +
  '\nreturn {COLLOC, collocHits, collocFix, senseHits, closestEg, nativeSuggest, bookEgHtml, checkGrammar};')(DATA);
const gErr = t => api.checkGrammar(t).filter(x => x.level === 'error');
let fails = 0;

// ① 每条搭配都要抓得到自己的反例（写了规则却抓不到 = 白写）
console.log('--- ① 每条中式英语搭配都要抓得到自己的反例 ---');
let noFix = 0;
api.COLLOC.forEach(c => {
  if (!api.collocHits(c.bad).some(h => h.good === c.good)) {
    console.log('  ❌ 抓不到：' + c.bad); fails++; return;
  }
  if (!c.fix) { noFix++; return; }
  // 自带 fix 的：改出来必须等于自己写的 exp，改完不能再被自己抓到，且改好的句子自己要过语法检查
  const got = c.fix(c.bad);
  if (got !== c.exp) { console.log('  ❌ 改错了：' + c.bad + ' → ' + got + '（应为 ' + c.exp + '）'); fails++; }
  if (api.collocHits(got).length) { console.log('  ❌ 改完还被判中式：' + got); fails++; }
  const ge = gErr(got);
  if (ge.length) { console.log('  ❌ 改好的句子语法不过：' + got + ' → ' + ge.map(x => x.why.replace(/<[^>]+>/g, '')).join('；')); fails++; }
});
console.log('  ' + api.COLLOC.length + ' 条规则自测完成（其中 ' + (api.COLLOC.length - noFix) + ' 条能自动改好整句）');

// ② 正常句一条都不能被报（宁可漏报，不可误报）
console.log('--- ② 正常说法必须零误报 ---');
const OK = [
  'Please open the door for me.',
  'Open the book at page ten.',
  'Close the door, please.',
  'Open your eyes and look at me.',
  'I like to listen to music at home.',
  'She listens to the radio every morning.',
  'I go home at six every day.',
  'He wants to go to school now.',
  'I read a book before I sleep.',
  'We watch TV after dinner every night.',
  'They watch a football game on Sunday.',
  'My father plays basketball with me.',
  'She plays the piano very well.',
  'I do my homework after school.',
  'She takes some medicine every morning.',
  'I have some soup for lunch today.',
  'The rain is very heavy this afternoon.',
  'This new car is very expensive.',
  'The price is too high for me.',
  'My book is better than his book.',
  'There are four people in my family.',
  'I like this book very much.',
  'I really like my new teacher.',
  'How do you say this word in English?',
  'Please turn on the light in my room.',
  'He turned off the TV and went to bed.',
  'My family lives in a small house.',
  'She returned the book to the library.',
  'We talked about the film after school.',
  'The film is boring and I am tired.',
  'It is very interesting to me.',
  'Everyday English is very useful.',
  'They joined in the game happily.',
  'She looks at the picture on the wall.',
  'He knows how to say it in English.',
  'I eat an apple every day.',
  'She drinks milk in the morning.',
  'The old man closed the door slowly.'
];
OK.forEach(s => {
  const h = api.collocHits(s);
  if (h.length) { console.log('  ❌ 误报  ' + s + '  → ' + h.map(x => x.bad).join('；')); fails++; }
});
console.log('  ' + (OK.length - fails) + '/' + OK.length + ' 零误报');

// ③ 全册 1803 个例句一条都不能被报（例句是母语者范句，被报就是规则太宽）
console.log('--- ③ 全册例句自检 ---');
let egBad = 0, nEg = 0;
DATA.units.forEach(u => u.sections.forEach(x => x.words.forEach(w => w.egs.forEach(e => {
  nEg++; const h = api.collocHits(e);
  if (h.length) { console.log('  ❌ ' + e + ' → ' + h.map(y => y.bad).join('；')); egBad++; }
}))));
console.log('  ' + (nEg - egBad) + '/' + nEg + ' 例句零误报');
fails += egBad;

// ④ 挑最接近的课本例句：要挑到有共同词的那一句
console.log('--- ④ closestEg 要挑最接近孩子那句的例句 ---');
const w4 = { w: 'book', egs: ['This is my English book.', 'She reads a book in the garden.', 'Put the book on the desk, please.'] };
const got = api.closestEg(w4, 'She reads a book in the garden every day.');
if (got !== w4.egs[1]) { console.log('  ❌ 挑成了：' + got); fails++; } else console.log('  ✅ 挑到共同词最多的一句');
// 完全没共同词时也要给得出一句（不能返回空）
if (!api.closestEg(w4, 'zzz qqq xxx')) { console.log('  ❌ 无共同词时给不出例句'); fails++; }
else console.log('  ✅ 无共同词时仍给得出一句');

// ⑤ 意思说不通：查表能确定的那一类必须抓到，正常句零误报
console.log('--- ⑤ 意思说不通（吃书喝桌子这类，不用 AI 也能确定）---');
[['I eat a book every day.', 'eat book'],
 ['He eats his shoes at home.', 'eat shoes'],
 ['She drinks the desk slowly.', 'drink desk'],
 ['We drink some bread for lunch.', 'drink bread']].forEach(([t, why]) => {
  if (!api.senseHits(t).length) { console.log('  ❌ 没抓到：' + t + '（' + why + '）'); fails++; }
});
const SENSE_OK = ['I eat an apple every day.', 'She eats some bread for breakfast.',
  'He drinks a glass of milk.', 'We drink tea in the afternoon.',
  'I read a book every night.', 'She watches TV after dinner.',
  'My mother cooks rice for us.', 'He wants to eat some fish.'];
SENSE_OK.forEach(t => {
  const h = api.senseHits(t);
  if (h.length) { console.log('  ❌ 误报  ' + t + '  → ' + h.map(x => x.why).join('；')); fails++; }
});
let senseEg = 0;
DATA.units.forEach(u => u.sections.forEach(x => x.words.forEach(w => w.egs.forEach(e => {
  if (api.senseHits(e).length) { console.log('  ❌ 例句被判说不通：' + e); senseEg++; }
}))));
fails += senseEg;
console.log('  4 类反例全抓到 · ' + SENSE_OK.length + ' 条正常句零误报 · 全册例句零误报');

// ⑥ 必须真的接进「写错」那条路径——不能只写了函数没人调用
console.log('--- ⑥ 接线检查 ---');
const errBranch = src.match(/if \(errs\.length\) \{[\s\S]*?\n  \}/);
if (!errBranch) { console.log('  ❌ 找不到写错分支'); fails++; }
else {
  if (!/nativeSuggest\(w, s\)/.test(errBranch[0])) { console.log('  ❌ 写错时没给地道说法'); fails++; }
  else console.log('  ✅ 写错时会给「欧美人会这样说」');
  if (!/aiGetKey\(\)/.test(errBranch[0])) { console.log('  ❌ 写错时没有 AI 加强层'); fails++; }
  else console.log('  ✅ 有 Key 时写错也会拿改好的句子去问 AI');
}
if (/通过之后我会告诉你/.test(src)) { console.log('  ❌ 还留着「改对了才告诉你怎么说」的旧文案'); fails++; }
else console.log('  ✅ 旧文案（改对了才给）已经去掉');

// ⑥b 回显的必须是孩子自己写的那一段，不能拿规则表里的例句充数
const demoW = { w: 'excuse', egs: ['Excuse me, is this your handbag?', 'Excuse me, what is your name?',
                                   'Please excuse my bad writing.'] };
const nsHtml = api.nativeSuggest(demoW, 'I very like this excuse.');
if (nsHtml.indexOf('very like') < 0) { console.log('  ❌ 没有回显孩子句子里命中的那一段'); fails++; }
else console.log('  ✅ 回显的是孩子自己写的「very like」');
if (nsHtml.indexOf('this book') >= 0) { console.log('  ❌ 拿规则表里的例句（this book）充数了'); fails++; }
else console.log('  ✅ 没有拿规则表的例句充数');

// ⑦ ⭐ 规则能确定的时候绝不调 AI
console.log('--- ⑦ 规则已有确定结论时不调 AI ---');
if (!/const sure = cHits\.length > 0 \|\| sHits\.length > 0/.test(src)) { console.log('  ❌ 没有「规则已确定」这个判断'); fails++; }
else console.log('  ✅ 有 sure（中式说法／意思说不通 = 规则已确定）');
if (!/if \(aiGetKey\(\) && !sure\)/.test(src)) { console.log('  ❌ 写错分支没有用 sure 挡住 AI'); fails++; }
else console.log('  ✅ 写错时规则已确定 → 不调 AI');
// 语法对但命中搭配表／语义表的两条分支，必须在调 AI 之前就 return
const afterGram = src.slice(src.indexOf('const gramOkHtml'));
const aiPos = afterGram.indexOf('await aiCheckSentence');
const sensePos = afterGram.indexOf('if (sHits.length)');
const colPos = afterGram.indexOf('if (cHits.length)');
if (!(sensePos > -1 && sensePos < aiPos && colPos > -1 && colPos < aiPos)) {
  console.log('  ❌ 中式说法／意思说不通的分支没有排在 AI 之前'); fails++;
} else console.log('  ✅ 语法对但规则有话说时，先给规则的结论并 return，不走 AI');
if (!/系统能确定的都查过了/.test(src)) { console.log('  ❌ 没 Key 时没告诉孩子查过哪些'); fails++; }
else console.log('  ✅ 没 Key 时明确告诉孩子「系统能确定的都查过了」');

console.log(fails ? '\n❌ 失败 ' + fails + ' 项' : '\n全部通过');
process.exit(fails ? 1 : 0);
