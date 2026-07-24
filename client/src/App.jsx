import { useState, useEffect } from "react";

const COUNTRIES = [
  { id: "France", flag: "🇫🇷", c: "#1B6B3A" },
  { id: "Belgique", flag: "🇧🇪", c: "#C2590A" },
  { id: "Ghana", flag: "🇬🇭", c: "#0D7377" },
  { id: "Ireland", flag: "🇮🇪", c: "#1B3A6B" },
];

const t = { title:"Capstone Generator", sub:"Unique AI-generated content every click", country:"Country", name:"Full Name", email:"Email", gen:"Generate & Preview", loading:["🤖 AI generating content...","📊 Building presentation...","📄 Filling document...","📝 Designing unique CV..."], dl:"⬇ Download ZIP", regen:"🔄 Regenerate", back:"← Back", pres:"Presentation", doc:"Document", cv:"CV", opp:"Opportunity", skills:"Skills", exp:"Experience", next:"Next Steps", profile:"Profile", education:"Education", langs:"Languages", namePh:"e.g. John Smith", emailPh:"e.g. john@email.com" };

export default function App() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [country, setCountry] = useState("Ghana");
  const [status, setStatus] = useState("idle");
  const [loadStep, setLoadStep] = useState(0);
  const [error, setError] = useState("");
  const [preview, setPreview] = useState(null);
  const [tab, setTab] = useState(0);
  const [dling, setDling] = useState(false);
  const [aiOn, setAiOn] = useState(null);

  const valid = name.trim().length >= 2 && email.includes("@");
  const ac = COUNTRIES.find(c => c.id === country)?.c || "#1B6B3A";

  useEffect(() => { fetch("/api/health").then(r=>r.json()).then(d=>setAiOn(d.ai)).catch(()=>{}); }, []);
  useEffect(() => { if(status!=="loading")return; const iv=setInterval(()=>setLoadStep(p=>(p+1)%4),2200); return()=>clearInterval(iv); }, [status]);

  const generate = async () => {
    if(!valid||status==="loading")return;
    setStatus("loading");setLoadStep(0);setError("");setPreview(null);
    try {
      const res = await fetch("/api/preview",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({name:name.trim(),email:email.trim(),country,lang:"en"})});
      if(!res.ok){const d=await res.json();throw new Error(d.error||"Failed");}
      const data=await res.json();
      setPreview(data.content);setTab(0);setStatus("preview");
    } catch(e){setError(e.message);setStatus("error");setTimeout(()=>setStatus("idle"),4000);}
  };

  const download = async () => {
    setDling(true);
    try{const res=await fetch("/api/download");const blob=await res.blob();const a=document.createElement("a");a.href=URL.createObjectURL(blob);a.download=`Capstone_${name.trim().replace(/\s+/g,"_")}.zip`;document.body.appendChild(a);a.click();document.body.removeChild(a);}catch(e){alert("Download failed");}
    setDling(false);
  };

  // ═══ PREVIEW ═══
  if(status==="preview"&&preview){
    const p=preview;
    const tabs=[{i:"📊",l:t.pres},{i:"📄",l:t.doc},{i:"📝",l:t.cv}];
    return(
      <div style={S.page}><div style={{...S.container,maxWidth:680}}>
        <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:18,flexWrap:"wrap",gap:8}}>
          <button onClick={()=>{setStatus("idle");setPreview(null)}} style={S.ghost}>{t.back}</button>
          <div style={{display:"flex",gap:8}}>
            <button onClick={generate} style={{...S.ghost,color:ac}}>{t.regen}</button>
            <button onClick={download} disabled={dling} style={{...S.dlBtn,background:ac}}>{dling?"⏳ ...":t.dl}</button>
          </div>
        </div>
        <div style={{display:"flex",gap:4,marginBottom:14}}>
          {tabs.map((tb,i)=>(<button key={i} onClick={()=>setTab(i)} style={{...S.tabBtn,background:tab===i?ac+"15":"transparent",borderColor:tab===i?ac+"44":"rgba(255,255,255,0.06)",color:tab===i?ac:"#666"}}>{tb.i} {tb.l}</button>))}
        </div>
        <div style={S.pCard}>
          {tab===0&&<><div style={{textAlign:"center",marginBottom:10}}><span style={{fontSize:9,background:ac+"15",color:ac,display:"inline-block",padding:"3px 10px",borderRadius:6,fontWeight:700}}>📐 Layout: {p.ppt_design}</span></div><Sec t={`${t.opp} 1`} ac={ac}><Opp o={p.opp1} ac={ac}/></Sec><Sec t={`${t.opp} 2`} ac={ac}><Opp o={p.opp2} ac={ac}/></Sec><Sec t={t.next} ac={ac}><div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10}}><div>{(p.next_immediate||[]).map((n,i)=><Bul key={i} t={n}/>)}</div><div>{(p.next_medium||[]).map((n,i)=><Bul key={i} t={n}/>)}</div></div></Sec></>}
          {tab===1&&<><div style={{textAlign:"center",marginBottom:14}}><span style={{fontSize:9,background:ac+"15",color:ac,display:"inline-block",padding:"3px 10px",borderRadius:6,fontWeight:700,marginBottom:6}}>📄 Capstone Project Document</span><div style={{fontSize:18,fontWeight:800,color:"#eee"}}>{p.name}</div><div style={{fontSize:11,color:"#777"}}>{p.country} · Green Pathways Capstone</div></div><Sec t="Section 1: Presentation — Project Summary" ac={ac}><div style={{background:"rgba(255,255,255,0.02)",border:`1px solid ${ac}22`,borderRadius:8,padding:12}}><p style={S.txt}>{p.summary}</p></div></Sec><Sec t="Section 2: CV/Resume — Professional Profile Improvements" ac={ac}><div style={{background:"rgba(255,255,255,0.02)",border:`1px solid ${ac}22`,borderRadius:8,padding:12}}><p style={S.txt}>{p.cv_improvements}</p></div></Sec></>}
          {tab===2&&<><div style={{textAlign:"center",marginBottom:14}}><span style={{fontSize:9,background:ac+"15",color:ac,display:"inline-block",padding:"3px 10px",borderRadius:6,fontWeight:700,marginBottom:6}}>🎨 {p.cv_design}</span><div style={{fontSize:18,fontWeight:800,color:"#eee"}}>{p.name}</div><div style={{fontSize:11,color:"#777"}}>{p.email} · {p.phone} · {p.city}</div></div><Sec t={t.profile} ac={ac}><p style={S.txt}>{p.profile}</p></Sec><Sec t={t.education} ac={ac}><div style={{fontWeight:700,fontSize:12,color:"#ddd"}}>{p.education?.degree}</div><div style={{fontSize:11,color:"#888",marginBottom:4}}>{p.education?.university}</div>{p.education?.specialization&&<Bul t={`Specialization: ${p.education.specialization}`}/>}{p.education?.project&&<Bul t={`Capstone Project: ${p.education.project}`}/>}{p.education?.coursework&&<Bul t={`Core Coursework: ${p.education.coursework}`}/>}{p.education?.academic_standing&&<Bul t={`Academic Standing: ${p.education.academic_standing}`}/>}</Sec><Sec t={t.exp} ac={ac}><div style={{fontWeight:700,fontSize:12,color:"#ddd"}}>{p.experience?.volunteer_org}</div>{p.experience?.volunteer_role&&<div style={{fontSize:11,color:"#888",fontStyle:"italic",marginBottom:2}}>{p.experience.volunteer_role}</div>}{(p.experience?.volunteer_bullets||[]).map((b,i)=><Bul key={i} t={b}/>)}<div style={{fontWeight:700,fontSize:12,color:"#ddd",marginTop:8}}>{p.experience?.placement_org}</div>{p.experience?.placement_role&&<div style={{fontSize:11,color:"#888",fontStyle:"italic",marginBottom:2}}>{p.experience.placement_role}</div>}{(p.experience?.placement_bullets||[]).map((b,i)=><Bul key={i} t={b}/>)}</Sec><Sec t={t.skills} ac={ac}><div style={{display:"flex",flexWrap:"wrap",gap:4}}>{[...(p.skills?.left||[]),...(p.skills?.right||[])].map((s,i)=>(<span key={i} style={{fontSize:10,background:"rgba(255,255,255,0.04)",border:"1px solid rgba(255,255,255,0.08)",padding:"3px 8px",borderRadius:6,color:"#bbb"}}>{s}</span>))}</div></Sec><Sec t={t.langs} ac={ac}>{(p.languages||[]).map((l,i)=><Bul key={i} t={l}/>)}</Sec></>}
        </div>
      </div><style>{CSS(ac)}</style></div>
    );
  }

  // ═══ FORM ═══
  return(
    <div style={S.page}><div style={S.container}>
      <div style={S.hero}>
        <div style={{...S.badge,borderColor:ac+"33",color:ac}}>🌱 Green Pathways</div>
        <h1 style={S.h1}>{t.title}</h1>
        <p style={S.sub}>{t.sub}</p>
      </div>
      <div style={{...S.card,borderColor:ac+"12"}}>
        <label style={S.label}>{t.country}</label>
        <div style={{display:"grid",gridTemplateColumns:"repeat(4,1fr)",gap:8,marginBottom:20}}>
          {COUNTRIES.map(c=>(
            <button key={c.id} onClick={()=>setCountry(c.id)} style={{...S.cBtn,borderColor:country===c.id?c.c+"55":"rgba(255,255,255,0.06)",background:country===c.id?c.c+"10":"transparent",color:country===c.id?c.c:"#555"}}>
              <span style={{fontSize:22}}>{c.flag}</span><span style={{fontSize:10,fontWeight:700}}>{c.id}</span>
            </button>
          ))}
        </div>
        <label style={S.label}>{t.name}</label>
        <input value={name} onChange={e=>setName(e.target.value)} placeholder={t.namePh} disabled={status==="loading"} style={S.input} onKeyDown={e=>e.key==="Enter"&&generate()}/>
        <label style={{...S.label,marginTop:16}}>{t.email}</label>
        <input value={email} onChange={e=>setEmail(e.target.value)} placeholder={t.emailPh} disabled={status==="loading"} type="email" style={S.input} onKeyDown={e=>e.key==="Enter"&&generate()}/>
        <button onClick={generate} disabled={!valid||status==="loading"} style={{...S.genBtn,marginTop:22,background:!valid||status==="loading"?"#1a1a1a":status==="error"?"#dc2626":ac,color:!valid&&status==="idle"?"#444":"#fff",cursor:valid&&status!=="loading"?"pointer":"not-allowed"}}>
          {status==="loading"?<><span style={S.spin}/>{t.loading[loadStep]}</>:status==="error"?`❌ ${error}`:t.gen}
        </button>
      </div>
      <p style={S.foot}>AI-powered · 15,000+ CV designs · English only</p>
    </div><style>{CSS(ac)}</style></div>
  );
}

function Sec({t,ac,children}){return <div style={{marginBottom:14}}><div style={{fontSize:10,fontWeight:800,textTransform:"uppercase",letterSpacing:".08em",color:ac,marginBottom:6,paddingBottom:3,borderBottom:`2px solid ${ac}22`}}>{t}</div>{children}</div>}
function Opp({o,ac}){return <div style={{background:ac+"06",border:`1px solid ${ac}12`,borderRadius:10,padding:12,marginBottom:6}}><div style={{fontWeight:700,fontSize:13,color:"#eee"}}>{o?.company}</div><div style={{fontSize:11,color:"#888",marginBottom:4}}>{o?.position} · {o?.location}</div><div style={{fontSize:12,color:"#aaa",lineHeight:1.5}}>{o?.description}</div>{o?.skills&&<div style={{display:"flex",flexWrap:"wrap",gap:3,marginTop:6}}>{o.skills.map((s,i)=><span key={i} style={{fontSize:9,background:ac+"12",color:ac,padding:"2px 7px",borderRadius:5,fontWeight:600}}>{s}</span>)}</div>}</div>}
function Bul({t}){return <div style={{fontSize:12,color:"#aaa",lineHeight:1.7,paddingLeft:6}}>• {t}</div>}

const CSS=ac=>`*{margin:0;padding:0;box-sizing:border-box}body{background:#090909}@keyframes spin{to{transform:rotate(360deg)}}input::placeholder{color:#3a3a3a}input:focus{border-color:${ac}66!important;outline:none;box-shadow:0 0 0 3px ${ac}10}button{transition:all .15s}button:hover:not(:disabled){filter:brightness(1.1)}`;
const S={
  page:{minHeight:"100vh",background:"linear-gradient(170deg,#090909,#0d160f 40%,#0a100d 70%,#090909 100%)",fontFamily:"'Inter',-apple-system,sans-serif",color:"#ddd",display:"flex",justifyContent:"center",padding:"30px 14px"},
  container:{width:"100%",maxWidth:480},
  hero:{textAlign:"center",marginBottom:22},
  badge:{display:"inline-block",border:"1px solid",borderRadius:100,padding:"5px 14px",fontSize:11,fontWeight:700,letterSpacing:".06em",textTransform:"uppercase",marginBottom:10,background:"rgba(0,0,0,0.3)"},
  h1:{fontSize:34,fontWeight:900,letterSpacing:"-.04em",color:"#f5f5f5",lineHeight:1},
  sub:{fontSize:13,color:"#555",marginTop:8,fontWeight:500},
  pill:{display:"inline-block",padding:"3px 10px",borderRadius:100,fontSize:10,fontWeight:600,marginTop:8},
  card:{background:"rgba(255,255,255,0.015)",border:"1px solid",borderRadius:16,padding:"22px 20px"},
  label:{display:"block",fontSize:9,fontWeight:800,color:"#555",textTransform:"uppercase",letterSpacing:".1em",marginBottom:6},
  cBtn:{padding:"10px 4px",borderRadius:10,border:"1px solid",cursor:"pointer",display:"flex",flexDirection:"column",alignItems:"center",gap:3,background:"transparent"},
  input:{width:"100%",padding:"12px 14px",fontSize:14,fontWeight:500,borderRadius:10,border:"1px solid rgba(255,255,255,0.07)",background:"rgba(0,0,0,0.4)",color:"#eee",fontFamily:"inherit"},
  genBtn:{width:"100%",padding:"16px",fontSize:14,fontWeight:800,borderRadius:12,border:"none",fontFamily:"inherit",display:"flex",alignItems:"center",justifyContent:"center",gap:10},
  spin:{display:"inline-block",width:16,height:16,border:"2px solid rgba(255,255,255,0.15)",borderTopColor:"#fff",borderRadius:"50%",animation:"spin .7s linear infinite"},
  foot:{marginTop:16,fontSize:10,color:"#2a2a2a",textAlign:"center",fontWeight:500},
  pCard:{background:"rgba(255,255,255,0.015)",border:"1px solid rgba(255,255,255,0.05)",borderRadius:14,padding:18,minHeight:200},
  tabBtn:{flex:1,padding:"9px 6px",borderRadius:9,border:"1px solid",fontSize:12,fontWeight:700,cursor:"pointer",textAlign:"center",background:"transparent"},
  ghost:{background:"none",border:"none",fontSize:12,fontWeight:600,cursor:"pointer",padding:"5px 10px",color:"#666"},
  dlBtn:{border:"none",color:"#fff",fontSize:12,fontWeight:700,padding:"8px 16px",borderRadius:8,cursor:"pointer"},
  txt:{fontSize:12,color:"#aaa",lineHeight:1.7},
};
