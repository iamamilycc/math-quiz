// 功能：以「孩子实际作答」的视角走查判分，重点覆盖本轮改动过的题。
// 用法：node build/tests/walkthrough_eng.js   （在专案根目录执行）
// 成功标准：末尾输出「✅ 走查全部符合预期」。
const fs = require('fs');
const src = fs.readFileSync('eng.html', 'utf8');
const m = src.match(/const DATA = ([\s\S]*?);\n\s*let currentChapterId/);
const DATA = eval('(' + m[1] + ')');

function normalize(t) {
  if (t === null || t === undefined) return '';
  return String(t).trim().replace(/\s+/g, '').replace(/　/g, '').toLowerCase();
}
function grade(q, ans) {
  if (q.type === 'fill') {
    const a = Array.isArray(q.answer) ? q.answer : [q.answer];
    return a.map(normalize).includes(normalize(ans));
  }
  if (q.type === 'multi') {
    return [...ans].sort().join(',') === [...q.answer].sort().join(',');
  }
  return normalize(ans) === normalize(q.answer);
}
const find = (sid, qid) => {
  for (const c of DATA.chapters) for (const s of c.sections)
    if (s.id === sid) for (const q of s.quiz) if (q.id === qid) return q;
};

let bad = 0;
console.log('=== 正向：孩子的自然答法必须判对 ===\n');
[
  ['e-c5-s1', 9, 'C',        'will not 的缩写（原为填空题，写 won’t 必被判错，已改选择题）'],
  ['e-c2-s3', 9, 'B',        '否定祈使句（原题干措辞混乱，已改选择题）'],
  ['e-c3-s1', 10, 'like',    'doesn’t 后动词还原'],
  ['e-c3-s1', 10, 'Like',    '同上：判分不分大小写'],
  ['e-c3-s1', 10, ' like ',  '同上：前后多打空格也该算对'],
  ['e-c4-s1', 10, 'go',      'didn’t 后动词还原'],
  ['e-c2-s1', 9, 'Are any',  'There be 变疑问句'],
  ['e-c2-s1', 9, 'are  any', '同上：中间多打空格也该算对'],
  ['e-c2-s1', 10, 'There',   'There be 与 have'],
  ['e-c2-s1', 10, 'there',   '同上：小写也该算对'],
  ['e-c6-s1', 9, 'whose',    'whose 问所有权（小写）'],
  ['e-c7-s6', 9, 'how',      '对方式提问（小写）'],
].forEach(([sid, qid, ans, desc]) => {
  const q = find(sid, qid);
  if (!q) { console.log(`  ❌ 找不到 ${sid} q${qid}`); bad++; return; }
  const ok = grade(q, ans);
  console.log(`  ${ok ? '✅' : '❌'} ${sid} q${qid} 答「${ans}」→ ${ok ? '判对' : '判错'}   ${desc}`);
  if (!ok) bad++;
});

console.log('\n=== 反向：错误答法必须判错 ===\n');
[
  ['e-c3-s1', 10, 'likes', 'doesn’t 后面写 likes 是典型错误'],
  ['e-c4-s1', 10, 'went',  'didn’t 后面写 went 是典型错误'],
  ['e-c5-s1', 9, 'A',      'willn’t 不是英语单词'],
  ['e-c2-s3', 9, 'A',      '否定祈使句不能光用 not'],
].forEach(([sid, qid, ans, desc]) => {
  const q = find(sid, qid);
  const ok = grade(q, ans);
  console.log(`  ${!ok ? '✅' : '❌'} ${sid} q${qid} 答「${ans}」→ ${ok ? '判对（不该！）' : '判错'}   ${desc}`);
  if (ok) bad++;
});

console.log(bad ? `\n❌ ${bad} 项不符预期` : '\n✅ 走查全部符合预期');
process.exit(bad ? 1 : 0);
