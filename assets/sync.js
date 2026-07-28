/* 七年级学习测验 math-quiz — 云端同步层（可选 Gitee 码云[国内] / GitHub；私有仓库 mathquiz-data，每使用者一档 users/<昵称>.json）
   仿照精读 jingdu 的 assets/sync.js 同一套安全模式：
   - 令牌由使用者自己在设置窗口输入，只存本机 localStorage，绝不写入任何代码仓库/网页源码。
   - 离线优先：没设定同步照常可用；设定后错题本自动备份，清浏览器/换设备可还原。
   - 同步对象：所有以 mathquiz_ 开头的 localStorage 键（目前主要是错题本 mathquiz_wrongbook_v1）。 */
(function(){
  'use strict';
  const NS='mathquiz_', CFG_KEY=NS+'sync', UPD_KEY=NS+'updatedAt';
  let sha=null, timer=null, busy=false;

  function cfg(){ try{ return JSON.parse(localStorage.getItem(CFG_KEY))||null; }catch(e){ return null; } }
  function setCfg(c){ if(c) localStorage.setItem(CFG_KEY, JSON.stringify(c)); else localStorage.removeItem(CFG_KEY); sha=null; }
  function b64e(s){ return btoa(unescape(encodeURIComponent(s))); }
  function b64d(s){ return decodeURIComponent(escape(atob(String(s).replace(/\n/g,'')))); }
  function setStatus(t, ok){
    const el=document.getElementById('mqSyncStatus');
    if(el){ el.textContent=t; el.style.color = ok===false ? '#d13a3a' : '#888'; }
  }

  function snapshot(){
    const data={};
    for(let i=0;i<localStorage.length;i++){
      const k=localStorage.key(i);
      if(k && k.indexOf(NS)===0 && k!==CFG_KEY) data[k]=localStorage.getItem(k);
    }
    return { updatedAt: parseInt(localStorage.getItem(UPD_KEY)||'0',10) || Date.now(), data:data };
  }
  function applySnapshot(snap){
    const keep=localStorage.getItem(CFG_KEY);
    const kill=[];
    for(let i=0;i<localStorage.length;i++){
      const k=localStorage.key(i);
      if(k && k.indexOf(NS)===0 && k!==CFG_KEY) kill.push(k);
    }
    kill.forEach(k=>localStorage.removeItem(k));
    for(const k in snap.data){ if(k!==CFG_KEY) localStorage.setItem(k, snap.data[k]); }
    if(keep) localStorage.setItem(CFG_KEY, keep);
  }

  /* ---------- 供应商抽象（与 jingdu 完全一致） ---------- */
  function isGitee(c){ return (c&&c.provider)==='gitee'; }
  function repoOwner(c){ return (c && c.owner) || ''; }
  function repoName(c){ return (c && c.repo) || 'mathquiz-data'; }
  function contentsUrl(c, path){
    const base = isGitee(c) ? 'https://gitee.com/api/v5' : 'https://api.github.com';
    return base+'/repos/'+repoOwner(c)+'/'+repoName(c)+'/contents/'+path;
  }
  async function whoami(provider, token){
    if(provider==='gitee'){
      const r=await fetch('https://gitee.com/api/v5/user?access_token='+encodeURIComponent(token));
      if(!r.ok) throw 'auth'; const j=await r.json(); return j.login;
    }
    const r=await fetch('https://api.github.com/user', {headers:{'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'}});
    if(!r.ok) throw 'auth'; const j=await r.json(); return j.login;
  }
  async function getFile(c, path){
    let url=contentsUrl(c, path)+'?t='+Date.now(), opt={};
    if(isGitee(c)) url+='&access_token='+encodeURIComponent(c.token);
    else opt.headers={'Authorization':'Bearer '+c.token,'Accept':'application/vnd.github+json'};
    const r=await fetch(url, opt);
    if(r.status===404) return null;
    if(r.status===401||r.status===403) throw 'auth';
    if(!r.ok) throw 'http'+r.status;
    const j=await r.json();
    return { content:j.content, sha:j.sha };
  }
  async function writeFile(c, path, contentB64, message, curSha){
    if(isGitee(c)){
      const doWrite=async(sh)=>{
        const body={ access_token:c.token, content:contentB64, message:message };
        let method='POST'; if(sh){ body.sha=sh; method='PUT'; }
        return fetch(contentsUrl(c,path), {method:method, headers:{'Content-Type':'application/json'}, body:JSON.stringify(body)});
      };
      let r=await doWrite(curSha);
      if(r.status===401||r.status===403) throw 'auth';
      if(!r.ok){ const cur=await getFile(c,path).catch(()=>null); if(!cur) throw 'http'+r.status; r=await doWrite(cur.sha); if(!r.ok) throw 'http'+r.status; }
      const j=await r.json(); return j.content && j.content.sha;
    }
    const doWrite=async(sh)=>{
      const body={ message:message, content:contentB64 }; if(sh) body.sha=sh;
      return fetch(contentsUrl(c,path), {method:'PUT', headers:{'Authorization':'Bearer '+c.token,'Accept':'application/vnd.github+json'}, body:JSON.stringify(body)});
    };
    let r=await doWrite(curSha);
    if(r.status===401||r.status===403) throw 'auth';
    if(r.status===409||r.status===422){ const cur=await getFile(c,path).catch(()=>null); r=await doWrite(cur?cur.sha:null); }
    if(!r.ok) throw 'http'+r.status;
    const j=await r.json(); return j.content && j.content.sha;
  }

  function userPath(){ const c=cfg(); return 'users/'+encodeURIComponent(c.user)+'.json'; }

  function pull(){
    const c=cfg(); if(!c) return Promise.reject('nocfg');
    return getFile(c, userPath()).then(f=>{ if(!f){ sha=null; return null; } sha=f.sha; return JSON.parse(b64d(f.content)); });
  }
  async function push(){
    if(busy){ schedule(8000); return; }
    const c=cfg(); if(!c) return;
    busy=true;
    try{
      const content=b64e(JSON.stringify(snapshot()));
      const newSha=await writeFile(c, userPath(), content, 'sync '+c.user+' '+new Date().toISOString(), sha);
      if(newSha) sha=newSha;
      setStatus('☁️ 已备份 '+new Date().toLocaleTimeString('zh',{hour:'2-digit',minute:'2-digit'}), true);
      busy=false;
    }catch(e){
      busy=false;
      if(e==='auth'){ setStatus('⚠️ 同步码失效，请重新设定', false); return; }
      setStatus('📴 离线，联网后自动备份', false); schedule(30000);
    }
  }
  function schedule(delay){ if(!cfg()) return; clearTimeout(timer); timer=setTimeout(push, delay||4000); }

  function init(){
    const c=cfg(); if(!c){ setStatus(''); renderCard(); return; }
    renderCard();
    setStatus('☁️ 连线中…');
    pull().then(remote=>{
      const localUpd=parseInt(localStorage.getItem(UPD_KEY)||'0',10);
      if(remote && remote.updatedAt > localUpd){
        applySnapshot(remote.data ? remote : {data:{}});
        localStorage.setItem(UPD_KEY, String(remote.updatedAt));
        setStatus('☁️ 已从云端还原', true);
        if(window.MQSYNC_ONRESTORE) window.MQSYNC_ONRESTORE();
      }else if(localUpd && (!remote || localUpd > remote.updatedAt)){
        push();
      }else{
        setStatus('☁️ 已同步', true);
      }
    }).catch(e=>{
      setStatus(e==='auth' ? '⚠️ 同步码失效，请重新设定' : '📴 离线，资料先存本机', e!=='auth' ? undefined : false);
    });
  }

  /* ---------- 设定卡（只在有 #mqSyncCard 的页面渲染，目前是错题本页） ---------- */
  function ensureStyle(){
    if(document.getElementById('mq-sync-style')) return;
    const style=document.createElement('style');
    style.id='mq-sync-style';
    style.textContent=
      '.mq-sync-card{background:white;border-radius:12px;padding:14px 16px;margin-bottom:16px;box-shadow:0 1px 4px rgba(0,0,0,0.06);font-size:14px}'+
      '.mq-sync-row{display:flex;align-items:center;gap:10px;flex-wrap:wrap}'+
      '.mq-sync-btn{border:none;border-radius:8px;padding:8px 14px;font-size:13px;cursor:pointer;background:#eee;color:#444}'+
      '.mq-sync-btn.primary{background:#3a6df0;color:white}'+
      '.mq-modal-mask{position:fixed;inset:0;background:rgba(0,0,0,0.4);display:flex;align-items:center;justify-content:center;z-index:9999;padding:16px}'+
      '.mq-modal{background:white;border-radius:14px;padding:20px;max-width:420px;width:100%;max-height:90vh;overflow:auto}'+
      '.mq-modal h3{margin:0 0 14px;font-size:17px}'+
      '.mq-field{margin-bottom:12px}'+
      '.mq-field label{display:block;font-size:13px;color:#666;margin-bottom:4px}'+
      '.mq-field input,.mq-field select,.mq-field textarea{width:100%;padding:9px 10px;border:1px solid #ddd;border-radius:8px;font-size:14px;box-sizing:border-box;font-family:inherit}'+
      '.mq-field textarea{min-height:60px;resize:vertical}'+
      '.mq-hint{font-size:12px;color:#999;line-height:1.6;margin-bottom:14px}'+
      '.mq-modal-btns{display:flex;justify-content:flex-end;gap:8px}';
    document.head.appendChild(style);
  }

  function renderCard(){
    const box=document.getElementById('mqSyncCard'); if(!box) return;
    ensureStyle();
    box.className='mq-sync-card';
    const c=cfg();
    if(!c){
      box.innerHTML='<div class="mq-sync-row">'+
        '<span style="font-weight:600">☁️ 云端同步未开启</span>'+
        '<span style="color:#999;font-size:13px">开启后错题本可在多台设备间同步，也方便家长直接查看</span>'+
        '<button class="mq-sync-btn primary" style="margin-left:auto" onclick="MQSYNC.setup()">开启</button></div>';
      return;
    }
    const provName = isGitee(c) ? 'Gitee' : 'GitHub';
    box.innerHTML='<div class="mq-sync-row">'+
      '<span style="font-weight:600">👤 '+c.user+'</span>'+
      '<span id="mqSyncStatus" style="color:#888;font-size:13px">☁️</span>'+
      '<span style="color:#999;font-size:13px">· '+provName+'</span>'+
      '<span style="margin-left:auto;display:flex;gap:6px;flex-wrap:wrap">'+
      '<button class="mq-sync-btn" onclick="MQSYNC.setup()">设定</button>'+
      '<button class="mq-sync-btn" onclick="MQSYNC.turnOff()">关闭同步</button></span></div>';
  }

  function esc(s){ return String(s).replace(/[&<>"']/g, c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
  function openModal(opts){
    ensureStyle();
    return new Promise(resolve=>{
      const mask=document.createElement('div'); mask.className='mq-modal-mask';
      const box=document.createElement('div'); box.className='mq-modal';
      box.innerHTML = '<h3>'+esc(opts.title)+'</h3>'+
        opts.fields.map(f=>'<div class="mq-field"><label>'+esc(f.label)+'</label>'+
          (f.type==='textarea'
            ? '<textarea data-k="'+f.key+'" placeholder="'+esc(f.placeholder||'')+'">'+esc(f.value||'')+'</textarea>'
            : f.type==='select'
              ? '<select data-k="'+f.key+'">'+f.options.map(o=>'<option value="'+esc(o.value)+'"'+(o.value===(f.value||'')?' selected':'')+'>'+esc(o.label)+'</option>').join('')+'</select>'
              : '<input type="text" data-k="'+f.key+'" placeholder="'+esc(f.placeholder||'')+'" value="'+esc(f.value||'')+'">')+
          '</div>').join('') +
        (opts.hint ? '<div class="mq-hint">'+esc(opts.hint)+'</div>' : '') +
        '<div class="mq-modal-btns"><button type="button" class="mq-sync-btn" data-act="cancel">取消</button>'+
        '<button type="button" class="mq-sync-btn primary" data-act="ok">确定</button></div>';
      mask.appendChild(box); document.body.appendChild(mask);
      function close(v){ mask.remove(); resolve(v); }
      box.querySelector('[data-act=cancel]').onclick=()=>close(null);
      mask.addEventListener('click', e=>{ if(e.target===mask) close(null); });
      box.querySelector('[data-act=ok]').onclick=()=>{
        const vals={};
        opts.fields.forEach(f=>{ vals[f.key]=box.querySelector('[data-k="'+f.key+'"]').value.trim(); });
        close(vals);
      };
      const firstInput=box.querySelector('input,textarea,select');
      if(firstInput) setTimeout(()=>firstInput.focus(), 50);
    });
  }

  async function setup(){
    const c=cfg()||{};
    const vals = await openModal({
      title:'☁️ 设定云端同步',
      fields:[
        {key:'user', label:'这台设备上是谁在学？', type:'text', placeholder:'昵称（同一昵称=同一份错题本）', value:c.user||''},
        {key:'provider', label:'云端服务', type:'select', value:c.provider||'gitee', options:[
          {value:'gitee', label:'Gitee 码云（国内·不翻墙·推荐）'},
          {value:'github', label:'GitHub（需海外网络）'} ]},
        {key:'repo', label:'仓库名称', type:'text', placeholder:'你建的私有仓库名', value:c.repo||'mathquiz-data'},
        {key:'token', label:'同步码（私人令牌）', type:'textarea', placeholder:'贴上令牌（之前设过可留空不改）'}
      ],
      hint:'令牌只存这台设备、不外传、不会写进任何网页代码。先在 Gitee/GitHub 建一个「私有」仓库，把仓库名填上面。Gitee：设置→私人令牌，勾选权限生成。'
    });
    if(!vals || !vals.user) return;
    const token=vals.token||c.token||'';
    if(!token){ alert('没有同步码，先不开启云端同步。'); return; }
    const provider = vals.provider==='github' ? 'github' : 'gitee';
    const repo = (vals.repo||'').trim() || 'mathquiz-data';
    setStatus('☁️ 验证令牌中…');
    let owner;
    try{ owner = await whoami(provider, token); }
    catch(e){ alert('令牌验证失败：可能令牌不对、或连不上云端。请检查后重试。'); renderCard(); return; }
    setCfg({ user:vals.user, token:token, provider:provider, owner:owner, repo:repo }); sha=null;
    init();
  }
  function turnOff(){
    if(!confirm('确定要关闭云端同步吗？本机的错题本资料不会被删除，只是不再自动备份。')) return;
    setCfg(null);
    renderCard();
  }

  window.MQSYNC={ schedule:schedule, setup:setup, turnOff:turnOff, init:init,
                  _cfg:cfg, _pull:pull, _push:push, _snapshot:snapshot };
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', init);
  else init();
  window.addEventListener('online', ()=>schedule(2000));
})();
