// 功能：用「我们自己的语法引擎」反查英语题库里的英文句子（内容正确性，不是结构检查）
// 用法：node build/tests/audit_eng_english.js
// ⭐ 为什么要有：题是 AI（我）写的，孩子没有判断能力，不能让他去发现我的错。
//    audit_eng.py 查的是结构（答案分布、去重键、标签闭合），一条都没查英文内容本身。
//    这支拿测验站的判分引擎当第三方，把题库里每个英文句子重新判一遍。
//
// 三条断言：
//   ① 硬红线：「选正确的」题里，被列为答案的选项，语法不能有错（0 容忍）
//   ② 判错的句子必须全在白名单里 —— 新写的英文句子有语法错会立刻变红
//   ③ 白名单里的句子必须仍然被判错 —— 防止我把一个正确句误列成「故意错例」
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const eng = fs.readFileSync(path.join(ROOT, 'eng.html'), 'utf8');
const words = fs.readFileSync(path.join(ROOT, 'words.html'), 'utf8');
const DATA = eval('(' + eng.match(/const DATA = ([\s\S]*?);\n/)[1] + ')');
const WD = eval('(' + words.match(/const DATA = ([\s\S]*?);\n/)[1] + ')');
const blk = words.match(/\/\* ========== 英语句子语法检查器[\s\S]*?(?=\/\* ========== 路由)/);
const GW = "const GRAMMAR_WORDS = DATA.units.reduce((a,u)=>a.concat(u.sections.reduce((b,x)=>b.concat(x.words.map(w=>({w:w.w,pos:w.pos}))),[])),[]);\n";
const api = new Function('DATA', 'const esc=x=>x,speak=()=>{};\n' + GW + blk[0] + '\nreturn {checkGrammar, collocHits, senseHits};')(WD);

const WL_PATH = path.join(__dirname, 'known_bad_sentences.txt');
const WL = new Set(fs.readFileSync(WL_PATH, 'utf8').split('\n')
  .map(l => l.replace(/\s*#.*$/, '').trim()).filter(Boolean));

const strip = t => String(t || '').replace(/<[^>]+>/g, ' ').replace(/&nbsp;/g, ' ').replace(/\s+/g, ' ').trim();
const SENT = /[A-Z][A-Za-z0-9'’,\-’ ]{8,}[.?!]/g;
const errsOf = s => api.checkGrammar(s).filter(x => x.level === 'error');
let fails = 0;

// ---- ① 硬红线：「选正确」题的答案选项不能有语法错 ----
console.log('--- ① 「选正确的」题里，答案选项不能有语法错（0 容忍）---');
const isFullEn = b => /^[A-Z]/.test(b) && /[.?!]$/.test(b) && b.split(/\s+/).length >= 3 && !/[一-鿿]/.test(b);
let checkedOpt = 0, wrongAsRight = 0;
DATA.chapters.forEach(c => c.sections.forEach(sec => (sec.quiz || []).forEach(q => {
  if (!q.options || !q.options.length) return;
  const stem = strip(q.stem);
  if (!/正确/.test(stem) || /不正确|错误/.test(stem)) return;
  const ans = [].concat(q.answer);
  q.options.forEach(o => {
    const s = strip(o), letter = s.charAt(0);
    const body = s.replace(/^[A-E][.、．]\s*/, '').trim();
    if (!isFullEn(body)) return;
    checkedOpt++;
    if (!ans.includes(letter)) return;
    const e = errsOf(body);
    if (e.length) {
      wrongAsRight++; fails++;
      console.log('  🚨 ' + sec.id + ' ' + q.id + ' 选项' + letter + '「' + body + '」→ ' +
        e.map(x => x.why.replace(/<[^>]+>/g, '')).join('；'));
    }
  });
})));
console.log('  检查 ' + checkedOpt + ' 个整句英文选项，语法错却当答案的：' + wrongAsRight + ' 个');

// ---- ② 判错的句子必须全在白名单 ----
console.log('--- ② 题库里被判错的英文句子，必须是「刻意写的错误示范」---');
const hit = new Map();
DATA.chapters.forEach(c => c.sections.forEach(sec => {
  const scan = (kind, txt) => (strip(txt).match(SENT) || []).forEach(x => {
    x = x.trim();
    if (hit.has(x) || !errsOf(x).length) return;
    hit.set(x, sec.id + ' · ' + kind);
  });
  (sec.notes || []).forEach(n => {
    scan('讲解', n.explain);
    (n.examples || []).forEach(e => scan('例句', typeof e === 'string' ? e : JSON.stringify(e)));
    if (n.think) scan('思考', n.think);
    if (n.card) scan('卡片', JSON.stringify(n.card));
  });
  (sec.quiz || []).forEach(q => {
    scan('题干', q.stem);
    (q.options || []).forEach(o => scan('选项', o));
    scan('解释', q.explain);
  });
}));
let notInWL = 0;
hit.forEach((where, s) => {
  if (!WL.has(s)) {
    notInWL++; fails++;
    console.log('  ❌ 新的语法错句（不在白名单里）：' + where + '\n     「' + s + '」→ ' +
      errsOf(s).map(x => x.why.replace(/<[^>]+>/g, '')).join('；') +
      '\n     若确实是刻意的错误示范，加进 build/tests/known_bad_sentences.txt；否则请改对它');
  }
});
console.log('  题库判错 ' + hit.size + ' 句，全部在白名单：' + (notInWL === 0 ? '是' : '否（' + notInWL + ' 句不在）'));

// ---- ③ 白名单不能过期 ----
console.log('--- ③ 白名单里的句子必须仍然被判错（否则可能是我把正确句当成了错例）---');
let stale = 0;
WL.forEach(s => {
  if (!errsOf(s).length) {
    stale++; fails++;
    console.log('  ⚠️ 白名单里这句现在判不出错了，请复查它到底对不对：「' + s + '」');
  }
});
console.log('  白名单 ' + WL.size + ' 句，过期 ' + stale + ' 句');

// ---- ④ 判断题与引擎不能自相矛盾 ----
//   题目说「这句话是正确的」而答案是「对」→ 引擎绝不能判它错。
//   否则孩子在造句关写同一句会被判错：这边说对、那边说错，他不知道该信谁。
console.log('--- ④ 判断题说「这句是对的」，引擎就不能判它错 ---');
let judged = 0, contradict = 0;
DATA.chapters.forEach(c => c.sections.forEach(sec => (sec.quiz || []).forEach(q => {
  if (q.type !== 'judge') return;
  const stem = strip(q.stem);
  // 形如「<英文句子> 这句话是正确的／语法正确／是正确的英语表达」
  const m = stem.match(/^([A-Z][^。]*?[.?!])\s*(这句话?|这个句子)?\s*(是正确的|语法正确|是正确的英语表达)/);
  if (!m) return;
  const sent = m[1].trim();
  judged++;
  const e = errsOf(sent), col = api.collocHits(sent), sen = api.senseHits(sent);
  const engineSaysBad = e.length || col.length || sen.length;
  if (q.answer === '对' && engineSaysBad) {
    contradict++; fails++;
    console.log('  🚨 题目说这句对，引擎却判它错：' + sec.id + ' ' + q.id + '「' + sent + '」→ ' +
      e.map(x => x.why.replace(/<[^>]+>/g, '')).concat(col.map(x => '中式：' + x.good))
       .concat(sen.map(x => x.why)).join('；'));
  }
  if (q.answer === '错' && !engineSaysBad) {
    console.log('  ℹ️ 题目说这句错，但引擎挑不出来（属于语义/用法错，规则层覆盖不到）：' +
      sec.id + ' ' + q.id + '「' + sent + '」');
  }
})));
console.log('  形如「某句是正确的」的判断题 ' + judged + ' 题，与引擎矛盾的：' + contradict + ' 题');

console.log(fails ? '\n❌ 失败 ' + fails + ' 项' : '\n✅ 英语题库的英文内容全部通过判分引擎复核');
process.exit(fails ? 1 : 0);
