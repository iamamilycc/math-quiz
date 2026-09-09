// 功能：造句写错时的「欧美人会怎么说」这一层的闭环测试
// 用法：node build/tests_native.js
// ⭐ 为什么要有：孩子写错了当场就要看到地道说法，而这一层**不能依赖 AI Key**。
//    两半：该报的必须报到（中式英语条目自测），不该报的一条都不能报
//    （误报＝把孩子本来对的说法说成中式英语，比漏报更伤）。
const fs = require('fs');
const src = fs.readFileSync('words.html', 'utf8');
const dataM = src.match(/const DATA = ([\s\S]*?);\n/);
const blkM  = src.match(/\/\* ========== 中式英语搭配表[\s\S]*?(?=\/\* AI 给的)/);
if (!dataM || !blkM) { console.log('❌ 抽不出 DATA 或搭配表'); process.exit(1); }
const DATA = eval('(' + dataM[1] + ')');
const api = new Function('DATA', 'const esc = x => x, speak = () => {}, nativeBlock = () => "";\n' +
                         blkM[0] + '\nreturn {COLLOC, collocHits, closestEg, nativeSuggest, bookEgHtml};')(DATA);
let fails = 0;

// ① 每条搭配都要抓得到自己的反例（写了规则却抓不到 = 白写）
console.log('--- ① 每条中式英语搭配都要抓得到自己的反例 ---');
api.COLLOC.forEach(c => {
  if (!api.collocHits(c.bad).some(h => h.good === c.good)) {
    console.log('  ❌ 抓不到：' + c.bad); fails++;
  }
});
console.log('  ' + api.COLLOC.length + ' 条规则自测完成');

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
  'We talked about the film after school.'
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

// ⑤ 必须真的接进「写错」那条路径——不能只写了函数没人调用
console.log('--- ⑤ 接线检查 ---');
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

console.log(fails ? '\n❌ 失败 ' + fails + ' 项' : '\n全部通过');
process.exit(fails ? 1 : 0);
