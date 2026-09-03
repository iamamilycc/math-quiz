// 功能：验证 eng.html 产出的 DATA 在浏览器端能正确解析、结构完整、HTML 标签未被破坏
// 用法：node build/test_eng.js   （在 math_quiz_deploy 目录下执行）
// 成功标准：打印 "全部通过"，退出码 0
const fs = require('fs');
const path = require('path');

const root = path.dirname(__dirname);
const src = fs.readFileSync(path.join(root, 'eng.html'), 'utf8');

let fail = 0;
function ok(cond, msg) {
  if (cond) { console.log('  ✅ ' + msg); }
  else { console.log('  ❌ ' + msg); fail++; }
}

// 1. 能取出 DATA 并解析
const m = src.match(/const DATA = ([\s\S]*?);\n\s*let currentChapterId/);
ok(!!m, 'eng.html 中能定位到 const DATA');
const DATA = eval('(' + m[1] + ')');
ok(DATA && Array.isArray(DATA.chapters), 'DATA 可解析且含 chapters 数组');

// 2. 结构统计
let notes = 0, quiz = 0;
const types = {};
DATA.chapters.forEach(c => c.sections.forEach(s => {
  notes += s.notes.length;
  quiz += s.quiz.length;
  s.quiz.forEach(x => { types[x.type] = (types[x.type] || 0) + 1; });
}));
ok(DATA.chapters.length >= 1, '至少 1 章（实际 ' + DATA.chapters.length + '）');
ok(notes >= 20, '知识点 >= 20（实际 ' + notes + '）');
ok(quiz >= 40, '题目 >= 40（实际 ' + quiz + '）');
ok(Object.keys(types).length >= 4, '题型齐全 ' + JSON.stringify(types));

// 3. HTML 标签在 JSON 转义后仍能还原（曾因 </ 转义踩坑）
const firstEx = DATA.chapters[0].sections[0].notes[0].examples[0].text;
ok(/<b>.*<\/b>/.test(firstEx), '例子中的 <b></b> 标签完整未被破坏');

// 4. 判分逻辑仿真：复刻 gradeQuiz 的判分算法，正确答案必判对、错误答案必判错
function normalize(t) {
  if (t === null || t === undefined) return '';
  return String(t).trim().replace(/\s+/g, '').replace(/\u3000/g, '').toLowerCase();
}
function grade(q, userAnswer) {
  if (q.type === 'multi') {
    const user = [...userAnswer].sort();
    const correct = [...q.answer].sort();
    return JSON.stringify(user) === JSON.stringify(correct);
  }
  if (q.type === 'fill') {
    const accepted = Array.isArray(q.answer) ? q.answer : [q.answer];
    return accepted.map(normalize).includes(normalize(userAnswer));
  }
  return normalize(userAnswer) === normalize(q.answer);
}
let nPos = 0, nNeg = 0, badPos = 0, badNeg = 0;
DATA.chapters.forEach(c => c.sections.forEach(s => s.quiz.forEach(q => {
  // 正例：标准答案必须判对
  nPos++;
  if (!grade(q, q.type === 'fill' ? q.answer[0] : q.answer)) {
    badPos++; console.log('    正例失败：' + q.stem.slice(0, 30));
  }
  // 反例：构造一个确定错误的答案，必须判错
  let bad = null;
  if (q.type === 'choice') {
    const letters = q.options.map(o => o[0]);
    bad = letters.find(l => l !== q.answer);
  } else if (q.type === 'multi') {
    const letters = q.options.map(o => o[0]);
    const missing = letters.find(l => !q.answer.includes(l));
    if (missing !== undefined) bad = [...q.answer, missing];   // 多选一个干扰项
    else bad = q.answer.slice(0, q.answer.length - 1);
  } else if (q.type === 'judge') {
    bad = q.answer === '对' ? '错' : '对';
  } else if (q.type === 'fill') {
    bad = '__zzz_definitely_wrong__';
  }
  if (bad !== null && bad !== undefined) {
    nNeg++;
    if (grade(q, bad)) { badNeg++; console.log('    反例失败(错答被判对)：' + q.stem.slice(0, 30)); }
  }
})));
ok(badPos === 0, '正例：' + nPos + ' 道题用标准答案作答，全部判对');
ok(badNeg === 0, '反例：' + nNeg + ' 道题用错误答案作答，全部判错');

// 4b. 答案合法性：选择题答案必须落在选项字母范围内（防止直接改 eng.html 改出孤儿答案）
let orphan = 0;
DATA.chapters.forEach(c => c.sections.forEach(s => s.quiz.forEach(q => {
  if (q.type === 'choice' || q.type === 'multi') {
    const letters = q.options.map(o => o[0]);
    const answers = Array.isArray(q.answer) ? q.answer : [q.answer];
    answers.forEach(a => {
      if (!letters.includes(a)) {
        orphan++; console.log('    孤儿答案 "' + a + '"：' + q.stem.slice(0, 30));
      }
    });
    if (q.type === 'multi' && answers.length === letters.length) {
      orphan++; console.log('    多选题全选即对：' + q.stem.slice(0, 30));
    }
  }
})));
ok(orphan === 0, '所有选择题/多选题的答案都落在选项范围内，且多选题不是全选即对');

// 5. 错题本科目标识必须是 eng
ok(src.includes("saveWrongAnswers('eng'"), "gradeQuiz 写入错题本时科目标识为 'eng'");
ok(!src.includes("saveWrongAnswers('bio'"), '没有残留 bio 科目标识');

// 6. 填空题答案不含撇号（iPad 智能引号会误判）
let apo = 0;
DATA.chapters.forEach(c => c.sections.forEach(s => s.quiz.forEach(q => {
  if (q.type === 'fill') q.answer.forEach(a => { if (/['’]/.test(a)) apo++; });
})));
ok(apo === 0, '填空题答案不含撇号（避免 iPad 智能引号误判）');

console.log(fail === 0 ? '\n全部通过' : '\n失败 ' + fail + ' 项');
process.exit(fail === 0 ? 0 : 1);
