// 功能：单词模块闭环测试（在 words.html 的 DATA 与判分逻辑上直接断言）
// 用法：node build/tests_words.js   （在专案根目录执行）
const fs = require('fs');
const src = fs.readFileSync('words.html', 'utf8');
let fails = 0;
const ok = (c, n, d) => { console.log((c ? '  ✅ ' : '  ❌ ') + n + (c ? '' : '   << ' + d)); if (!c) fails++; };

const m = src.match(/const DATA = ([\s\S]*?);\n/);
ok(!!m, 'words.html 中能定位到 const DATA');
const DATA = eval('(' + m[1] + ')');
const words = DATA.units.flatMap(u => u.sections.flatMap(s => s.words));
ok(Array.isArray(DATA.units) && DATA.units.length > 0, 'DATA 结构正确（含 units）');
// ⭐ 撇号归一：iPad 的智能标点会把 ' 变成 ’，拼写判分必须当成同一个答案
// （目前词表里没有带撇号的词，但加 o'clock / don't 那天就会踩，先锁死）
(function () {
  const nm = src.match(/function normalize\(t\) \{[\s\S]*?\n\}/);
  if (!nm) { ok(false, '抽得出 normalize'); return; }
  const normalize = new Function(nm[0] + '\nreturn normalize;')();
  ok(normalize('don\u2019t') === normalize("don't"), '弯引号和直引号归一成同一个（拼对不能判错）');
  ok(normalize('O\u2019clock') === normalize("o'clock"), "o'clock 大小写+撇号都归一");
})();

// ⭐ 英美拼写：新概念是英式教材，孩子写美式不该被当成拼错（他没拼错，判错会让他以为 color 是错的）
(function () {
  const blk = src.match(/\/\* ⭐ 英式 → 美式拼写对照[\s\S]*?\n\}/);
  if (!blk) { ok(false, '抽得出英美拼写对照表'); return; }
  const usSpellingOf = new Function(blk[0] + '\nreturn usSpellingOf;')();
  ok(!!usSpellingOf('colour', 'color'), 'colour 写成 color 要算对并说明');
  ok(!!usSpellingOf('mum', 'mom'), 'mum 写成 mom 要算对并说明（用词差异）');
  ok(!usSpellingOf('colour', 'colur'), '真拼错的仍然判错');
  ok(!usSpellingOf('book', 'book'), '完全相同不给多余提示');
  ok(/美式/.test(usSpellingOf('colour', 'color')) && /英式/.test(usSpellingOf('colour', 'color')),
     '提示里两边口径都说清楚');
})();
// ⭐ 判分要真的接上：两个模式都必须用 usSpellingOf，否则表写了也没用
ok(/const usNote = usSpellingOf\(w\.w, v\);/.test(src) &&
   (src.match(/usSpellingOf\(w\.w, v\)/g) || []).length >= 2, '记忆卡和背诵两处都接上了英美拼写判定');
// ⭐ 朗读要用英式（教材和音标都是英式，读美音会对不上）
ok(/u\.lang = 'en-GB'/.test(src), '朗读用 en-GB（英式教材）');

console.log(`     单元 ${DATA.units.length} / 节 ${DATA.units.reduce((a,u)=>a+u.sections.length,0)} / 单词 ${words.length}`);

// --- 例句规则（和建置校验同一套，双保险）---
const norm = s => String(s||'').toLowerCase().replace(/[^a-z0-9\s]/g,' ').replace(/\s+/g,' ').trim();
/* ⚠️ 不要在这里再写一份 hasWord——同一条规则写三份，迟早判不一致。
   直接把页面里那份抽出来用，测的就是孩子真正会碰到的那份逻辑。 */
const hasWord = (() => {
  const mv = src.match(/const VERB_FORMS = \{[\s\S]*?\n\};/);
  const mn = src.match(/function normSent\(s\) \{[\s\S]*?\n\}/);
  const mh = src.match(/function hasWord\(s, w\) \{[\s\S]*?\n\}/);
  if (!mv || !mn || !mh) { console.log('  ❌ 抽不出页面里的 hasWord'); process.exit(1); }
  return new Function(mv[0] + '\n' + mn[0] + '\n' + mh[0] + '\nreturn hasWord;')();
})();
function tooSimilar(a, b) {
  const A = norm(a), B = norm(b);
  if (A === B) return true;
  const ta = A.split(' '), tb = B.split(' '), sb = new Set(tb);
  const inter = ta.filter(t => sb.has(t)).length, uni = new Set(ta.concat(tb)).size;
  return uni > 0 && inter / uni >= 0.8;
}
let bad3 = [], badLen = [], badHas = [], badCap = [], badEnd = [], badDup = [];
words.forEach(w => {
  if (!Array.isArray(w.egs) || w.egs.length !== 3) { bad3.push(w.w); return; }
  w.egs.forEach((e, i) => {
    if (e.trim().split(/\s+/).length < 5) badLen.push(w.w + '#' + (i+1));
    if (!hasWord(e, w.w)) badHas.push(w.w + '#' + (i+1));
    if (!/^[A-Z]/.test(e.trim())) badCap.push(w.w + '#' + (i+1));
    if (!/[.!?]$/.test(e.trim())) badEnd.push(w.w + '#' + (i+1));
  });
  for (let a = 0; a < 3; a++) for (let b = a+1; b < 3; b++)
    if (tooSimilar(w.egs[a], w.egs[b])) badDup.push(w.w);
});
ok(!bad3.length,   '每个词正好 3 个例句', bad3.slice(0,3));
ok(!badLen.length, '每个例句 ≥5 个单词', badLen.slice(0,3));
ok(!badHas.length, '每个例句都用上了该词', badHas.slice(0,3));
ok(!badCap.length, '每个例句句首大写', badCap.slice(0,3));
ok(!badEnd.length, '每个例句句尾有标点', badEnd.slice(0,3));
ok(!badDup.length, '同一个词的 3 个例句互不重复', badDup.slice(0,3));

// --- 单词本身 ---
const seen = new Map(); let dupW = [];
words.forEach(w => { const k = norm(w.w); if (seen.has(k)) dupW.push(w.w); seen.set(k, 1); });
ok(!dupW.length, '没有重复收录的单词', dupW.slice(0,3));
ok(words.every(w => w.ipa && w.pos && w.zh), '每个词都有音标/词性/中文');
ok(words.every(w => Number.isInteger(w.lesson) && w.lesson >= 1 && w.lesson <= 144), '课次都在 1..144');

// --- 背诵不能泄露答案（孩子只要照抄就过了，这一关等于白练）---
const leakZh = words.filter(w => (' ' + norm(w.zh) + ' ').includes(' ' + norm(w.w) + ' '));
ok(!leakZh.length, '中文释义里没有混进英文原词', leakZh.map(w => w.w).slice(0,3));
ok(src.includes('function shortTitle('), '背诵页首用短标题（节标题里的英文课名本身就是答案）');
ok(/setHead\('🧠 背诵 · ' \+ shortTitle\(/.test(src), '背诵确实调用了 shortTitle');

// --- 页面引擎 ---
ok(/MK_MIN_WORDS\s*=\s*5/.test(src), '造句内建下限是 5 个单词');
ok(/MK_PER_WORD\s*=\s*3/.test(src), '每个词要造 3 句');
ok(src.includes('hasWord(') && src.includes('tooSimilar('), '造句检查含「用上该词」与「不得重复」');
ok(src.includes('function checkGrammar('), '造句有真正的语法检查器（孩子没有判断能力，必须系统判对错）');
ok(/const issues = checkGrammar\(s\)/.test(src), '检查器已接进造句判分流程');
ok(src.includes('检查通过') && src.includes('个地方要改'), '判分会给明确结论（通过 / 哪几处要改）');
ok(!src.includes('都核对过，没问题') && !src.includes('你觉得'), '不再有「你自己判断对不对」式的自评');
ok(src.includes("subject: 'engword'"), '错题本科目标识为 engword');
ok(!/subject:\s*'(math|geo|bio)'/.test(src), '没有残留其他科目标识');

console.log(fails ? `\n❌ 失败 ${fails} 项` : '\n全部通过');
process.exit(fails ? 1 : 0);
