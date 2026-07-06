#!/usr/bin/env python3
"""
Capstone Generator V2 — EN/FR templates, Groq AI, 100+ CV layouts
Usage: python generate.py "Name" "email" "Country" "fr|en"
"""
import os, sys, json
from pathlib import Path

try:
    from pptx import Presentation
    from pptx.util import Pt
    from pptx.dml.color import RGBColor
    from docx import Document
    from docx.shared import Pt as DPt, RGBColor as DRC
except ImportError:
    print("Run: pip install python-pptx python-docx lxml"); sys.exit(1)

from groq_client import generate_content, fallback_content
from cv_engine import build_cv

BASE = Path(__file__).parent
TDIR = BASE.parent / "templates" if (BASE.parent / "templates").exists() else BASE / "templates"
OUT = BASE / "output"

def fill_tf(tf, items):
    tf.clear()
    for i, (bold, text) in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(6); r = p.add_run(); r.text = text
        r.font.size = Pt(14); r.font.bold = bold; r.font.name = "Arial"

# ═══ 1. PRESENTATION ═══
def gen_pptx(name, d, lang):
    is_fr = lang == "fr"
    template = TDIR / ("presentation_template_en.pptx" if is_fr else "presentation_template_en.pptx")
    prs = Presentation(str(template))
    o1, o2 = d["opportunity1"], d["opportunity2"]
    
    # Slide 0: Title — replace Name/Nom and Date
    for sh in prs.slides[0].shapes:
        if sh.has_text_frame:
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    t = r.text.strip()
                    if t in ("Nom", "Name"): r.text = name
                    elif t == "Date": r.text = "June 2026" if not is_fr else "Juin 2026"
    
    # EN has Executive Summary at slide index 1 — fill it
    if not is_fr and len(prs.slides) >= 12:
        for sh in prs.slides[1].shapes:
            if sh.has_text_frame:
                tf = sh.text_frame
                full_text = tf.text
                if "100 words" in full_text or "Executive" in full_text:
                    tf.clear()
                    r = tf.paragraphs[0].add_run()
                    r.text = d.get("capstone_summary", "")[:500]
                    r.font.size = Pt(14); r.font.name = "Arial"
                    break
    
    db = RGBColor(0x1B, 0x3C, 0x6D)
    opp = "Opportunité" if is_fr else "Opportunity"
    pos = "Poste" if is_fr else "Position"
    loc = "Lieu" if is_fr else "Location"
    dur = "Durée : 6 mois (dès septembre 2026)" if is_fr else "Duration: 6 months (from September 2026)"
    
    # Content slide indices: FR=[3,5,7,9], EN=[4,6,8,10]
    if is_fr:
        ci = [3, 5, 7, 9]
    else:
        ci = [4, 6, 8, 10]
    
    slide_content = [
        # Opportunities
        {"t": "Deux opportunités en énergies renouvelables" if is_fr else "Two renewable energy opportunities",
         "l": [(True, f"{opp} 1 : {o1['company']}"), (False, f"{pos} : {o1['position']}"), (False, f"{loc} : {o1['location']}"), (False, dur), (False, o1['description'])],
         "r": [(True, f"{opp} 2 : {o2['company']}"), (False, f"{pos} : {o2['position']}"), (False, f"{loc} : {o2['location']}"), (False, dur), (False, o2['description'])]},
        # Skills
        {"t": "Compétences et formations requises" if is_fr else "Required skills and qualifications",
         "l": [(True, f"{o1['company']} — {'Compétences' if is_fr else 'Skills'}")] + [(False, f"• {s}") for s in o1['skills']] + [(True, "Formation requise" if is_fr else "Required qualification"), (False, o1['qualification'])],
         "r": [(True, f"{o2['company']} — {'Compétences' if is_fr else 'Skills'}")] + [(False, f"• {s}") for s in o2['skills']] + [(True, "Formation requise" if is_fr else "Required qualification"), (False, o2['qualification'])]},
        # Experience
        {"t": "Mon expérience et compétences transférables" if is_fr else "My experience and transferable skills",
         "l": [(True, f"{'Pour' if is_fr else 'For'} {o1['company']}")] + [(False, f"• {e}") for e in o1['my_experience']],
         "r": [(True, f"{'Pour' if is_fr else 'For'} {o2['company']}")] + [(False, f"• {e}") for e in o2['my_experience']]},
        # Next Steps
        {"t": "Mes prochaines étapes" if is_fr else "My next steps",
         "l": [(True, "Actions immédiates (été 2026)" if is_fr else "Immediate actions (Summer 2026)")] + [(False, f"• {x}") for x in d['next_steps_immediate']],
         "r": [(True, "Développement à moyen terme" if is_fr else "Medium-term development")] + [(False, f"• {x}") for x in d['next_steps_medium']]},
    ]
    
    for idx, c in zip(ci, slide_content):
        if idx >= len(prs.slides): continue
        sl = prs.slides[idx]
        swtf = [(s, s.text_frame) for s in sl.shapes if s.has_text_frame]
        swtf.sort(key=lambda x: (x[0].top, x[0].left))
        if len(swtf) >= 3:
            tf = swtf[0][1]; tf.clear()
            r = tf.paragraphs[0].add_run(); r.text = c["t"]
            r.font.size = Pt(20); r.font.bold = True; r.font.name = "Arial"; r.font.color.rgb = db
            bs = sorted(swtf[1:], key=lambda x: x[0].left)
            if len(bs) >= 2:
                fill_tf(bs[0][1], c["l"]); fill_tf(bs[1][1], c["r"])
    
    out = OUT / f"Presentation_{name.replace(' ','_')}.pptx"
    prs.save(str(out)); return out

# ═══ 2. CAPSTONE DOCUMENT ═══
def gen_docx(name, d, lang):
    is_fr = lang == "fr"
    template = TDIR / ("capstone_template_en.docx" if is_fr else "capstone_template_en.docx")
    doc = Document(str(template))
    
    # Put name on RIGHT side of table
    for table in doc.tables:
        for row in table.rows:
            cells = row.cells
            if len(cells) >= 2:
                left = cells[0].text.strip()
                if "Prénom" in left or "NOM" in left or "Your Name" in left or "Name" in left:
                    cells[1].paragraphs[0].clear()
                    r = cells[1].paragraphs[0].add_run(name)
                    r.font.name = "Sora"; r.font.size = DPt(14)
                    r.italic = True; r.font.color.rgb = DRC(0x15, 0x39, 0x88)
                    break
    
    # Fill Table 1 = summary, Table 3 = CV improvements
    tables = doc.tables
    if len(tables) >= 4:
        cell = tables[1].rows[0].cells[0]
        cell.paragraphs[0].clear()
        r = cell.paragraphs[0].add_run(d["capstone_summary"])
        r.font.name = "Sora"; r.font.size = DPt(10)
        
        cell = tables[3].rows[0].cells[0]
        cell.paragraphs[0].clear()
        r = cell.paragraphs[0].add_run(d["cv_improvements"])
        r.font.name = "Sora"; r.font.size = DPt(10)
    
    out = OUT / f"Capstone_Document_{name.replace(' ','_')}.docx"
    doc.save(str(out)); return out

# ═══ MAIN ═══
def main():
    if len(sys.argv) >= 5:
        name, email, country, lang = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    elif len(sys.argv) >= 4:
        name, email, country, lang = sys.argv[1], sys.argv[2], sys.argv[3], "en"
    elif len(sys.argv) >= 3:
        name, email, country, lang = sys.argv[1], sys.argv[2], "France", "en"
    else:
        print('Usage: python generate.py "Name" "email" "Country" "fr|en"'); sys.exit(1)
    
    name = " ".join(name.split())
    if lang not in ("en", "en"): lang = "en"
    
    flags = {"France": "🇫🇷", "Belgique": "🇧🇪", "Ghana": "🇬🇭", "Ireland": "🇮🇪"}
    print(f"\n{'='*50}")
    print(f"🌱 {name} | {flags.get(country, '')} {country} | {'FR' if lang == 'fr' else 'EN'}")
    print(f"{'='*50}")
    
    print("\n🤖 Generating content via AI...")
    data = None
    try:
        data = generate_content(name, email, country, lang)
    except Exception as e:
        print(f"  ⚠ AI error: {e}")
    
    if not data:
        print("  ⚠ AI unavailable, using fallback")
        data = fallback_content(name, email, country, lang)
    else:
        print(f"   ✅ AI content ready")
        print(f"   🏢 {data['opportunity1']['company']} + {data['opportunity2']['company']}")
        print(f"   🎓 {data['education']['university']}")
    
    OUT.mkdir(exist_ok=True)
    
    print(f"\n📊 [1/3] Presentation ({lang.upper()})...")
    p1 = gen_pptx(name, data, lang); print(f"   ✅ {p1.name}")
    
    print(f"📄 [2/3] Capstone Document ({lang.upper()})...")
    p2 = gen_docx(name, data, lang); print(f"   ✅ {p2.name}")
    
    print("📝 [3/3] CV...")
    cv_path = OUT / f"CV_{name.replace(' ','_')}.docx"
    design = build_cv(data, cv_path)
    print(f"   🎨 Layout: {design}")
    print(f"   ✅ {cv_path.name}")
    
    # Save content for preview
    preview = {
        "name": name, "email": data.get("email",""), "country": data.get("country",""),
        "phone": data.get("phone",""), "city": data.get("city",""), "lang": lang,
        "opp1": data.get("opportunity1",{}), "opp2": data.get("opportunity2",{}),
        "education": data.get("education",{}), "experience": data.get("experience",{}),
        "profile": data.get("profile_summary",""), "skills": data.get("cv_skills",{}),
        "languages": data.get("languages",[]), "interests": data.get("interests",""),
        "summary": data.get("capstone_summary",""), "cv_improvements": data.get("cv_improvements",""),
        "next_immediate": data.get("next_steps_immediate",[]), "next_medium": data.get("next_steps_medium",[]),
        "cv_design": design,
    }
    with open(OUT / "content.json", "w") as f:
        json.dump(preview, f, ensure_ascii=False, indent=2)
    
    print(f"\n🎉 Done! → {OUT}/\n")

if __name__ == "__main__":
    main()