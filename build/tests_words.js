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
console.log(`     单元 ${DATA.units.length} / 节 ${DATA.units.reduce((a,u)=>a+u.sections.length,0)} / 单词 ${words.length}`);

// --- 例句规则（和建置校验同一套，双保险）---
const norm = s => String(s||'').toLowerCase().replace(/[^a-z0-9\s]/g,' ').replace(/\s+/g,' ').trim();
function hasWord(s, w) {
  const base = norm(w), S = ' ' + norm(s) + ' ';
  if (base.indexOf(' ') >= 0) return S.indexOf(' ' + base + ' ') >= 0;
  const stem = base.replace(/[ey]$/, '');
  return [base,base+'s',base+'es',base+'d',base+'ed',base+'ing',stem+'ing',stem+'ed',stem+'ies',stem+'ied']
    .some(f => S.indexOf(' ' + f + ' ') >= 0);
}
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
