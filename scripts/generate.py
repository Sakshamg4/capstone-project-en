#!/usr/bin/env python3
"""
Capstone Generator V2 — EN/FR templates, Groq AI, 100+ CV layouts
Usage: python generate.py "Name" "email" "Country" "fr|en"
"""
import os, sys, json, random
from pathlib import Path

try:
    from pptx import Presentation
    from pptx.util import Pt
    from pptx.dml.color import RGBColor
    from docx import Document
    from docx.shared import Pt as DPt, RGBColor as DRC
    from lxml import etree
except ImportError:
    print("Run: pip install python-pptx python-docx lxml"); sys.exit(1)

from groq_client import generate_content
from cv_engine import build_cv

BASE = Path(__file__).parent
TDIR = BASE.parent / "templates" if (BASE.parent / "templates").exists() else BASE / "templates"
OUT = BASE / "output"
def fill_tf(tf, items):
    tf.word_wrap = True
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    tf.clear()
    for i, (bold, text, bullet_char) in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(6)
        r = p.add_run()
        r.text = text
        r.font.size = Pt(13)
        r.font.bold = bold
        r.font.name = "Arial"
        
        # Override PPT bullet settings on the paragraph properties level
        pPr = p._p.get_or_add_pPr()
        for tag in ["buChar", "buNone", "buAutoNum", "buBlip"]:
            el = pPr.find("{http://schemas.openxmlformats.org/drawingml/2006/main}" + tag)
            if el is not None:
                pPr.remove(el)
        
        if bullet_char:
            buChar = etree.SubElement(pPr, "{http://schemas.openxmlformats.org/drawingml/2006/main}buChar")
            buChar.set("char", bullet_char)
            # Indent and hang for neat bullet alignment
            pPr.set("marL", "360000")
            pPr.set("indent", "-180000")
        else:
            etree.SubElement(pPr, "{http://schemas.openxmlformats.org/drawingml/2006/main}buNone")
            pPr.set("marL", "0")
            pPr.set("indent", "0")

# ═══ 1. PRESENTATION ═══
def gen_pptx(name, d, lang):
    template = TDIR / "presentation_template_en.pptx"
    prs = Presentation(str(template))
    o1, o2 = d["opportunity1"], d["opportunity2"]
    
    # 1. Randomize slide layout parameters
    header_style = random.choice([1, 2, 3, 4])
    bullet = random.choice(["•", "✔", "✦", "➤", "❖"])
    skills_split = random.choice([1, 2, 3])
    layout_type = random.choice([1, 2, 3, 4, 5])
    
    # Slide 0: Title — replace Name and Date
    for sh in prs.slides[0].shapes:
        if sh.has_text_frame:
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    t = r.text.strip()
                    if t == "Name": r.text = name
                    elif t == "Date": r.text = "July 2026"
    
    # EN has Executive Summary at slide index 1 — fill it
    if len(prs.slides) >= 12:
        for sh in prs.slides[1].shapes:
            if sh.has_text_frame:
                tf = sh.text_frame
                full_text = tf.text
                if "100 words" in full_text or "Executive" in full_text:
                    tf.clear()
                    r = tf.paragraphs[0].add_run()
                    r.text = d.get("capstone_summary", "")
                    r.font.size = Pt(12); r.font.name = "Arial"
                    # Explicitly remove bullets on executive summary paragraph
                    pPr = tf.paragraphs[0]._p.get_or_add_pPr()
                    for tag in ["buChar", "buNone", "buAutoNum", "buBlip"]:
                        el = pPr.find("{http://schemas.openxmlformats.org/drawingml/2006/main}" + tag)
                        if el is not None:
                            pPr.remove(el)
                    etree.SubElement(pPr, "{http://schemas.openxmlformats.org/drawingml/2006/main}buNone")
                    pPr.set("marL", "0")
                    pPr.set("indent", "0")
                    break
    
    db = RGBColor(0x1B, 0x3C, 0x6D)
    opp = "Opportunity"
    pos = "Position"
    loc = "Location"
    dur = "Duration: 6 months (from September 2026)"
    
    # Human-style slide titles
    opp_titles = [
        "Target Internship Opportunities",
        "Selected Career Pathways",
        "My Target Roles in Renewable Energy",
        "Key Opportunities of Interest",
        "Renewable Energy Internship Targets"
    ]
    skills_titles = [
        "Skills & Core Qualifications",
        "My Core Competencies",
        "Technical Skills & Requirements",
        "Prerequisites & What I Bring",
        "Required Skills and Training"
    ]
    exp_titles = [
        "My Relevant Experience",
        "Practical Background & Transferable Skills",
        "Projects & Volunteering Accomplishments",
        "What I Have Achieved So Far",
        "Transferable Experience & Accomplishments"
    ]
    steps_titles = [
        "My Action Plan & Next Steps",
        "Career Roadmap & Immediate Actions",
        "Future Development & Next Steps",
        "My Next Steps & Career Strategy",
        "Roadmap to My Professional Goals"
    ]
    
    t_opp = random.choice(opp_titles)
    t_skills = random.choice(skills_titles)
    t_exp = random.choice(exp_titles)
    t_steps = random.choice(steps_titles)
    
    # 2. Format Opportunities text according to header_style (bold, text, bullet_char)
    if header_style == 1:
        o1_hdr = [(True, f"{opp} 1 : {o1['company']}", None), (False, f"{pos} : {o1['position']}", None), (False, f"{loc} : {o1['location']}", None)]
        o2_hdr = [(True, f"{opp} 2 : {o2['company']}", None), (False, f"{pos} : {o2['position']}", None), (False, f"{loc} : {o2['location']}", None)]
    elif header_style == 2:
        o1_hdr = [(True, f"{o1['position']} @ {o1['company']}", None), (False, f"{loc}: {o1['location']}", None)]
        o2_hdr = [(True, f"{o2['position']} @ {o2['company']}", None), (False, f"{loc}: {o2['location']}", None)]
    elif header_style == 3:
        o1_hdr = [(True, f"✨ {o1['company']} — {o1['position']}", None), (False, f"📍 {o1['location']}", None)]
        o2_hdr = [(True, f"✨ {o2['company']} — {o2['position']}", None), (False, f"📍 {o2['location']}", None)]
    else:
        o1_hdr = [(True, o1['company'], None), (False, f"Role: {o1['position']} ({o1['location']})", None)]
        o2_hdr = [(True, o2['company'], None), (False, f"Role: {o2['position']} ({o2['location']})", None)]
        
    o1_opp_content = o1_hdr + [(False, dur, None), (False, o1['description'], None)]
    o2_opp_content = o2_hdr + [(False, dur, None), (False, o2['description'], None)]

    # 3. Format Skills & Qualifications based on skills_split style (bold, text, bullet_char)
    q_label = random.choice(["Academic Requirements", "Required Qualifications", "Minimum Prerequisites", "Target Education Level"])
    
    if skills_split == 1:
        lbl_s1 = random.choice([f"Core Skills for {o1['company']}", f"Technical Competencies - {o1['company']}", f"Skills Required by {o1['company']}"])
        lbl_s2 = random.choice([f"Core Skills for {o2['company']}", f"Technical Competencies - {o2['company']}", f"Skills Required by {o2['company']}"])
        skills_left = [(True, lbl_s1, None)] + [(False, s, bullet) for s in o1['skills']] + [(True, q_label, None), (False, o1['qualification'], None)]
        skills_right = [(True, lbl_s2, None)] + [(False, s, bullet) for s in o2['skills']] + [(True, q_label, None), (False, o2['qualification'], None)]
    elif skills_split == 2:
        tech_skills = sorted(list(set(o1['skills'] + o2['skills'])))[:5]
        soft_skills = d.get("cv_skills", {}).get("right", ["Teamwork", "Communication", "Problem-solving"])
        lbl_tech = random.choice(["Technical Skills Checklist", "My Technical Skills", "Solar & Energy Skills", "Target Hard Skills"])
        lbl_soft = random.choice(["Professional Soft Skills", "Core Competencies", "Key Transferable Skills", "Interpersonal Strengths"])
        skills_left = [(True, lbl_tech, None)] + [(False, s, bullet) for s in tech_skills] + [(True, "Education Requirements", None), (False, o1['qualification'], bullet), (False, o2['qualification'], bullet)]
        skills_right = [(True, lbl_soft, None)] + [(False, s, bullet) for s in soft_skills]
    else:
        all_skills = sorted(list(set(o1['skills'] + o2['skills'])))[:6]
        lbl_all = random.choice(["Combined Skills Checklist", "Prerequisites & Core Competencies", "Full Skills Profile"])
        lbl_roles = random.choice(["Role Alignment Details", "Target Internships & Positions", "Internship Opportunities"])
        skills_left = [(True, lbl_all, None)] + [(False, s, bullet) for s in all_skills]
        skills_right = [(True, lbl_roles, None), (True, o1['company'], None), (False, o1['position'], bullet), (True, o2['company'], None), (False, o2['position'], bullet)]

    # Content slide definitions
    opps_slide = {"t": t_opp, "l": o1_opp_content, "r": o2_opp_content}
    skills_slide = {"t": t_skills, "l": skills_left, "r": skills_right}
    
    lbl_exp1 = random.choice([f"My Work for {o1['company']}", f"Key Contributions - {o1['company']}", f"Value Added at {o1['company']}", f"Prepared for {o1['company']}"])
    lbl_exp2 = random.choice([f"My Work for {o2['company']}", f"Key Contributions - {o2['company']}", f"Value Added at {o2['company']}", f"Prepared for {o2['company']}"])
    
    exp_slide = {
        "t": t_exp,
        "l": [(True, lbl_exp1, None)] + [(False, e, bullet) for e in o1['my_experience']],
        "r": [(True, lbl_exp2, None)] + [(False, e, bullet) for e in o2['my_experience']]
    }
    
    lbl_step1 = random.choice(["Immediate Actions (Summer 2026)", "Short-Term Action Items", "Priority Action Plan", "Immediate Next Steps"])
    lbl_step2 = random.choice(["Medium-Term Development", "Professional Development Goals", "Long-Term Objectives", "Development Strategy"])
    
    steps_slide = {
        "t": t_steps,
        "l": [(True, lbl_step1, None)] + [(False, x, bullet) for x in d['next_steps_immediate']],
        "r": [(True, lbl_step2, None)] + [(False, x, bullet) for x in d['next_steps_medium']]
    }

    slide_content = [opps_slide, skills_slide, exp_slide, steps_slide]
    
    # 4. Apply Column Order Swapping dynamically per slide (50% chance)
    for s_dict in slide_content:
        if random.choice([True, False]):
            s_dict["l"], s_dict["r"] = s_dict["r"], s_dict["l"]
            
    ci = [4, 6, 8, 10]
    layout_sequence = []
    
    # Default coordinates (EMUs)
    top_y = 1152475
    left_x = 311700
    col_w = 3999900
    full_w = 8520600
    right_x = 4832400
    height_y = 3416400
    
    for idx, c in zip(ci, slide_content):
        if idx >= len(prs.slides): continue
        sl = prs.slides[idx]
        swtf = [(s, s.text_frame) for s in sl.shapes if s.has_text_frame]
        swtf.sort(key=lambda x: (x[0].top, x[0].left))
        
        if len(swtf) >= 3:
            # Title positioning and text replacement
            tf = swtf[0][1]; tf.clear()
            r = tf.paragraphs[0].add_run(); r.text = c["t"]
            r.font.size = Pt(20); r.font.bold = True; r.font.name = "Arial"; r.font.color.rgb = db
            
            # Reset bullet settings for slide titles
            pPr = tf.paragraphs[0]._p.get_or_add_pPr()
            for tag in ["buChar", "buNone", "buAutoNum", "buBlip"]:
                el = pPr.find("{http://schemas.openxmlformats.org/drawingml/2006/main}" + tag)
                if el is not None:
                    pPr.remove(el)
            etree.SubElement(pPr, "{http://schemas.openxmlformats.org/drawingml/2006/main}buNone")
            pPr.set("marL", "0")
            pPr.set("indent", "0")

            bs = sorted(swtf[1:], key=lambda x: x[0].left)
            if len(bs) >= 2:
                s1, s2 = bs[0][0], bs[1][0]
                
                # Record the consistent layout sequence
                layout_sequence.append(f"L{layout_type}")
                
                # Delete old placeholder shapes to prevent master slide styling overrides
                sl.shapes._element.remove(s1._element)
                sl.shapes._element.remove(s2._element)
                
                if layout_type == 1:
                    # Side-by-side Columns
                    tb1 = sl.shapes.add_textbox(left_x, top_y, col_w, height_y)
                    tb2 = sl.shapes.add_textbox(right_x, top_y, col_w, height_y)
                    fill_tf(tb1.text_frame, c["l"])
                    fill_tf(tb2.text_frame, c["r"])
                    
                elif layout_type == 2:
                    # Top-and-Bottom Split (Vertical Stack)
                    tb1 = sl.shapes.add_textbox(left_x, top_y, full_w, 1600000)
                    tb2 = sl.shapes.add_textbox(left_x, 2900000, full_w, 1600000)
                    fill_tf(tb1.text_frame, c["l"])
                    fill_tf(tb2.text_frame, c["r"])
                    
                elif layout_type == 3:
                    # Single Column Full-Width
                    tb1 = sl.shapes.add_textbox(left_x, top_y, full_w, height_y)
                    # Merge content from both columns
                    merged = c["l"] + [(True, "", None)] + c["r"]
                    fill_tf(tb1.text_frame, merged)
                    
                elif layout_type == 4:
                    # Asymmetric (Left Highlight / Right List)
                    tb1 = sl.shapes.add_textbox(left_x, top_y, 2800000, height_y)
                    tb2 = sl.shapes.add_textbox(3400000, top_y, 5432000, height_y)
                    fill_tf(tb1.text_frame, c["l"])
                    fill_tf(tb2.text_frame, c["r"])
                    
                else:
                    # Asymmetric (Left List / Right Highlight)
                    tb1 = sl.shapes.add_textbox(left_x, top_y, 5432000, height_y)
                    tb2 = sl.shapes.add_textbox(6032300, top_y, 2800000, height_y)
                    fill_tf(tb1.text_frame, c["l"])
                    fill_tf(tb2.text_frame, c["r"])
    
    # Clean metadata - set author to user
    prs.core_properties.author = name
    prs.core_properties.last_modified_by = name
    prs.core_properties.title = f'Green Pathways Capstone - {name}'
    prs.core_properties.comments = ''
    prs.core_properties.subject = 'Green Pathways Capstone Project'
    
    # Safe PPT design ID for filename compatibility (no special chars like arrow, check, diamond in filenames)
    bullet_names = {"•": "dot", "✔": "check", "✦": "star", "➤": "arrow", "❖": "diamond"}
    bullet_name = bullet_names.get(bullet, "bullet")
    layout_code = "".join(layout_sequence)
    ppt_design_safe = f"H{header_style}_B_{bullet_name}_S{skills_split}_{layout_code}"
    
    out = OUT / f"Presentation_{name.replace(' ','_')}_{ppt_design_safe}.pptx"
    prs.save(str(out)); return out, ppt_design_safe

# ═══ 2. CAPSTONE DOCUMENT ═══
def gen_docx(name, d, lang):
    template = TDIR / "capstone_template_en.docx"
    doc = Document(str(template))
    
    # Put name on RIGHT side of table
    for table in doc.tables:
        for row in table.rows:
            cells = row.cells
            if len(cells) >= 2:
                left = cells[0].text.strip()
                if "Your Name" in left or "Name" in left:
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
    
    # Clean metadata
    doc.core_properties.author = name
    doc.core_properties.last_modified_by = name
    doc.core_properties.title = f'Green Pathways Capstone - {name}'
    doc.core_properties.comments = ''
    
    out = OUT / f"Capstone_Document_{name.replace(' ','_')}.docx"
    doc.save(str(out)); return out

# ═══ MAIN ═══
def main():
    if len(sys.argv) >= 4:
        name, email, country = sys.argv[1], sys.argv[2], sys.argv[3]
    elif len(sys.argv) >= 3:
        name, email, country = sys.argv[1], sys.argv[2], "France"
    else:
        print('Usage: python generate.py "Name" "email" "Country"'); sys.exit(1)
    
    name = " ".join(name.split())
    lang = "en"
    
    flags = {"France": "🇫🇷", "Belgique": "🇧🇪", "Ghana": "🇬🇭", "Ireland": "🇮🇪"}
    print(f"\n{'='*50}")
    print(f"🌱 {name} | {flags.get(country, '')} {country} | EN")
    print(f"{'='*50}")
    
    print("\n🌱 Generating content from database...")
    data = generate_content(name, email, country, lang)
    print(f"   ✅ Content ready")
    print(f"   🏢 {data['opportunity1']['company']} + {data['opportunity2']['company']}")
    print(f"   🎓 {data['education']['university']}")
    
    OUT.mkdir(exist_ok=True)
    
    print(f"\n📊 [1/3] Presentation ({lang.upper()})...")
    p1_path, ppt_design = gen_pptx(name, data, lang); print(f"   ✅ {p1_path.name}")
    
    print(f"📄 [2/3] Capstone Document ({lang.upper()})...")
    p2 = gen_docx(name, data, lang); print(f"   ✅ {p2.name}")
    
    print("📝 [3/3] CV...")
    temp_path = OUT / f"CV_{name.replace(' ','_')}_temp.docx"
    design = build_cv(data, temp_path)
    cv_path = OUT / f"CV_{name.replace(' ','_')}_{design.replace(' ', '_')}.docx"
    if temp_path.exists():
        temp_path.rename(cv_path)
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
        "ppt_design": ppt_design,
    }
    with open(OUT / "content.json", "w") as f:
        json.dump(preview, f, ensure_ascii=False, indent=2)
    
    print(f"\n🎉 Done! → {OUT}/\n")

if __name__ == "__main__":
    main()