"""
CV Engine V4 — Professional colors, dramatic layout variety
"""
import random
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from lxml.etree import SubElement

def _rgb(h): return RGBColor(int(h[:2],16),int(h[2:4],16),int(h[4:6],16))
def _border(p,color,sz="6",style="single"):
    pPr=p._p.get_or_add_pPr();pBdr=SubElement(pPr,qn('w:pBdr'))
    b=SubElement(pBdr,qn('w:bottom'));b.set(qn('w:val'),style);b.set(qn('w:sz'),sz);b.set(qn('w:color'),color);b.set(qn('w:space'),'4')
def _top_border(p,color,sz="6"):
    pPr=p._p.get_or_add_pPr();pBdr=SubElement(pPr,qn('w:pBdr'))
    b=SubElement(pBdr,qn('w:top'));b.set(qn('w:val'),'single');b.set(qn('w:sz'),sz);b.set(qn('w:color'),color);b.set(qn('w:space'),'4')
def _shading_run(r,color):
    rPr=r._r.get_or_add_rPr();shd=SubElement(rPr,qn('w:shd'));shd.set(qn('w:val'),'clear');shd.set(qn('w:fill'),color)
def _shading_cell(cell,color):
    tc=cell._tc;tcPr=tc.get_or_add_tcPr();shd=SubElement(tcPr,qn('w:shd'));shd.set(qn('w:fill'),color);shd.set(qn('w:val'),'clear')
def _no_borders(table):
    tbl=table._tbl;tblPr=tbl.tblPr if tbl.tblPr is not None else SubElement(tbl,qn('w:tblPr'))
    borders=SubElement(tblPr,qn('w:tblBorders'))
    for edge in['top','left','bottom','right','insideH','insideV']:
        e=SubElement(borders,qn(f'w:{edge}'));e.set(qn('w:val'),'none');e.set(qn('w:sz'),'0')
def _tab_right(p):
    pPr=p._p.get_or_add_pPr();tabs=SubElement(pPr,qn('w:tabs'));tab=SubElement(tabs,qn('w:tab'));tab.set(qn('w:val'),'right');tab.set(qn('w:pos'),'9360')

# Professional muted palettes
COLORS = [
    {"ac":"2D3436","lt":"F5F6FA","nm":"Graphite"},     # dark grey
    {"ac":"0C3547","lt":"EBF5FB","nm":"Deep Sea"},      # dark blue-green
    {"ac":"1E3A5F","lt":"EAF0F7","nm":"Corporate Blue"},
    {"ac":"2C3E50","lt":"ECF0F1","nm":"Slate"},
    {"ac":"1A472A","lt":"EDF5F0","nm":"Pine"},
    {"ac":"3C1518","lt":"F5EEEF","nm":"Wine"},
    {"ac":"2B2D42","lt":"EEEEF2","nm":"Midnight"},
    {"ac":"344E41","lt":"EDF2EF","nm":"Forest"},
    {"ac":"3D405B","lt":"EDEDF2","nm":"Storm"},
    {"ac":"283618","lt":"F0F2EB","nm":"Olive"},
    {"ac":"4A4238","lt":"F2F0ED","nm":"Espresso"},
    {"ac":"1B4332","lt":"EAF4EE","nm":"Emerald"},
    {"ac":"003049","lt":"E6EEF4","nm":"Navy"},
    {"ac":"3A0CA3","lt":"EDEBF7","nm":"Royal"},
    {"ac":"495057","lt":"F1F2F3","nm":"Ash"},
    {"ac":"5C374C","lt":"F2ECF0","nm":"Plum"},
    {"ac":"3E1F47","lt":"F0EBF3","nm":"Grape"},
    {"ac":"14213D","lt":"E8EBF2","nm":"Oxford"},
    {"ac":"4A5859","lt":"EFF1F1","nm":"Steel"},
    {"ac":"2F4858","lt":"ECF0F3","nm":"Petrol"},
]

FONTS = ["Calibri","Georgia","Garamond","Cambria","Arial","Trebuchet MS","Book Antiqua","Century Gothic","Tahoma","Palatino Linotype"]
BULLETS = ["•","–","▹","›","◦","·","▪","—","→","✧"]


class CVBuilder:
    def __init__(self):
        self.pal = random.choice(COLORS)
        self.font = random.choice(FONTS)
        self.bullet = random.choice(BULLETS)
        self.name_style = random.choice(["center","left","spaced","banner_dark","banner_light","two_tone","minimal","uppercase_line"])
        self.head_style = random.choice(["line","thick_line","block_dark","block_light","bar_left","caps_only","dotted","top_accent"])
        self.skill_layout = random.choice(["two_col","inline_dots","tag_list","simple_list"])
        self.body_sz = random.choice([9.5,10,10.5])
        self.head_sz = random.choice([10.5,11,12])
        self.name_sz = random.choice([18,20,22,24,26])
        self.margin = random.choice([1.6,1.8,2.0,2.2])
        self.contact_style = random.choice(["pipe","dot","dash","newline"])
        
        self.doc = Document()
        for s in self.doc.sections:
            s.top_margin=Cm(self.margin-0.4);s.bottom_margin=Cm(self.margin-0.4)
            s.left_margin=Cm(self.margin);s.right_margin=Cm(self.margin)
        
        self.ac = self.pal["ac"]
        self.lt = self.pal["lt"]
    
    def _r(self,p,text,sz=None,bold=False,italic=False,color=None):
        r=p.add_run(text);r.font.size=Pt(sz or self.body_sz);r.font.name=self.font
        r.bold=bold;r.italic=italic
        if color:r.font.color.rgb=_rgb(color) if isinstance(color,str) else color
        return r

    def add_name(self, name, email, phone, city):
        sep = {"pipe":" | ","dot":" · ","dash":" — ","newline":"\n"}[self.contact_style]
        contact = f"{email}{sep}{phone}{sep}{city}"
        
        if self.name_style == "banner_dark":
            t=self.doc.add_table(rows=1,cols=1);t.alignment=WD_TABLE_ALIGNMENT.CENTER;_no_borders(t)
            cell=t.rows[0].cells[0];_shading_cell(cell,self.ac)
            p=cell.paragraphs[0];p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.space_before=Pt(18);p.space_after=Pt(6)
            self._r(p,name.upper(),self.name_sz,bold=True,color="FFFFFF")
            p2=cell.add_paragraph();p2.alignment=WD_ALIGN_PARAGRAPH.CENTER;p2.space_after=Pt(12)
            self._r(p2,f"{email}{sep}{phone}{sep}{city}",9,color="CCCCCC")
        
        elif self.name_style == "banner_light":
            t=self.doc.add_table(rows=1,cols=1);t.alignment=WD_TABLE_ALIGNMENT.CENTER;_no_borders(t)
            cell=t.rows[0].cells[0];_shading_cell(cell,self.lt)
            p=cell.paragraphs[0];p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.space_before=Pt(16);p.space_after=Pt(6)
            self._r(p,name.upper(),self.name_sz,bold=True,color=self.ac)
            p2=cell.add_paragraph();p2.alignment=WD_ALIGN_PARAGRAPH.CENTER;p2.space_after=Pt(12)
            self._r(p2,f"{email}{sep}{phone}{sep}{city}",9,color="666666")
        
        elif self.name_style == "two_tone":
            parts=name.upper().split()
            p=self.doc.add_paragraph();p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.space_after=Pt(3)
            if len(parts)>=2:
                self._r(p,parts[0]+" ",self.name_sz,bold=True,color=self.ac)
                self._r(p," ".join(parts[1:]),self.name_sz,bold=False,color="444444")
            else:
                self._r(p,name.upper(),self.name_sz,bold=True,color=self.ac)
            p=self.doc.add_paragraph();p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.space_after=Pt(10)
            self._r(p,f"{email}{sep}{phone}{sep}{city}",9,color="888888")
        
        elif self.name_style == "left":
            p=self.doc.add_paragraph();p.space_after=Pt(1)
            self._r(p,name.upper(),self.name_sz,bold=True,color=self.ac)
            p=self.doc.add_paragraph();p.space_after=Pt(10)
            _border(p,self.ac,"4")
            self._r(p,f"{email}{sep}{phone}{sep}{city}",9,color="888888")
        
        elif self.name_style == "spaced":
            p=self.doc.add_paragraph();p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.space_after=Pt(3)
            self._r(p,"    ".join(name.upper().split()),self.name_sz,bold=True,color=self.ac)
            p=self.doc.add_paragraph();p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.space_after=Pt(10)
            _border(p,self.ac,"6")
            self._r(p,f"{email}{sep}{phone}{sep}{city}",9,color="888888")
        
        elif self.name_style == "minimal":
            p=self.doc.add_paragraph();p.space_after=Pt(1)
            self._r(p,name,self.name_sz,bold=True,color="222222")
            p=self.doc.add_paragraph();p.space_after=Pt(10)
            self._r(p,f"{email}{sep}{phone}{sep}{city}",9,color="999999")
        
        elif self.name_style == "uppercase_line":
            p=self.doc.add_paragraph();p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.space_after=Pt(3)
            self._r(p,name.upper(),self.name_sz,bold=True,color=self.ac)
            # Thin accent line
            p2=self.doc.add_paragraph();p2.alignment=WD_ALIGN_PARAGRAPH.CENTER;p2.space_after=Pt(3)
            self._r(p2,"━" * 20,8,color=self.ac)
            p3=self.doc.add_paragraph();p3.alignment=WD_ALIGN_PARAGRAPH.CENTER;p3.space_after=Pt(10)
            self._r(p3,f"{email}{sep}{phone}{sep}{city}",9,color="888888")
        
        else:  # center
            p=self.doc.add_paragraph();p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.space_after=Pt(3)
            self._r(p,name.upper(),self.name_sz,bold=True,color=self.ac)
            p=self.doc.add_paragraph();p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.space_after=Pt(10)
            self._r(p,f"{email}{sep}{phone}{sep}{city}",9,color="888888")
    
    def add_section(self, title):
        p=self.doc.add_paragraph();p.space_before=Pt(13);p.space_after=Pt(5)
        
        if self.head_style == "block_dark":
            r=self._r(p,f"  {title.upper()}  ",self.head_sz,bold=True,color="FFFFFF")
            _shading_run(r,self.ac)
        elif self.head_style == "block_light":
            r=self._r(p,f"  {title.upper()}  ",self.head_sz,bold=True,color=self.ac)
            _shading_run(r,self.lt)
        elif self.head_style == "bar_left":
            self._r(p,f"▎ {title.upper()}",self.head_sz,bold=True,color=self.ac)
        elif self.head_style == "caps_only":
            self._r(p,title.upper(),self.head_sz+1,bold=True,color=self.ac)
        elif self.head_style == "dotted":
            self._r(p,title.upper(),self.head_sz,bold=True,color=self.ac)
            _border(p,self.ac,"4","dotted")
        elif self.head_style == "top_accent":
            _top_border(p,self.ac,"10")
            self._r(p,title.upper(),self.head_sz,bold=True,color=self.ac)
        elif self.head_style == "thick_line":
            self._r(p,title.upper(),self.head_sz,bold=True,color=self.ac)
            _border(p,self.ac,"12")
        else:  # line
            self._r(p,title.upper(),self.head_sz,bold=True,color=self.ac)
            _border(p,self.ac,"4")
    
    def add_entry(self, left, right):
        p=self.doc.add_paragraph();p.space_before=Pt(6);p.space_after=Pt(1)
        self._r(p,left,self.body_sz+0.5,bold=True,color="222222")
        p.add_run("\t")
        self._r(p,right,self.body_sz,italic=True,color="888888")
        _tab_right(p)
    
    def add_sub(self,text):
        p=self.doc.add_paragraph();p.space_after=Pt(1)
        self._r(p,text,self.body_sz,italic=True,color="777777")
    
    def add_bullet(self,text):
        p=self.doc.add_paragraph();p.space_after=Pt(1)
        self._r(p,f"  {self.bullet} {text}",self.body_sz,color="444444")
    
    def add_text(self,text):
        p=self.doc.add_paragraph();p.space_after=Pt(3)
        self._r(p,text,self.body_sz,color="444444")
    
    def add_skills(self, left, right):
        if self.skill_layout == "two_col":
            t=self.doc.add_table(rows=max(len(left),len(right)),cols=2);_no_borders(t)
            for i in range(max(len(left),len(right))):
                if i<len(left):
                    c=t.rows[i].cells[0].paragraphs[0];c.clear();self._r(c,f"  {self.bullet} {left[i]}",self.body_sz,color="444444")
                if i<len(right):
                    c=t.rows[i].cells[1].paragraphs[0];c.clear();self._r(c,f"  {self.bullet} {right[i]}",self.body_sz,color="444444")
        elif self.skill_layout == "inline_dots":
            all_s=left+right;p=self.doc.add_paragraph();p.space_after=Pt(3)
            for i,s in enumerate(all_s):
                self._r(p,s,self.body_sz,color=self.ac)
                if i<len(all_s)-1:self._r(p,"  ·  ",self.body_sz,color="CCCCCC")
        elif self.skill_layout == "tag_list":
            all_s=left+right;p=self.doc.add_paragraph();p.space_after=Pt(3)
            for i,s in enumerate(all_s):
                r=self._r(p,f" {s} ",self.body_sz,color=self.ac)
                _shading_run(r,self.lt)
                if i<len(all_s)-1:self._r(p,"  ",self.body_sz)
        else:  # simple_list
            for s in left+right:self.add_bullet(s)
    
    def get_id(self):
        return f"{self.pal['nm']}_{self.name_style}_{self.head_style}_{self.skill_layout}"
    
    def save(self,path):self.doc.save(str(path))


def build_cv(data, output_path):
    cv = CVBuilder()
    d = data
    name = " ".join(d["name"].split())
    
    cv.add_name(name, d["email"], d["phone"], d["city"])
    
    cv.add_section("Profile")
    cv.add_text(d["profile_summary"])
    
    edu = d["education"]
    cv.add_section("Education")
    cv.add_entry(edu["degree"], d.get("edu_years","2023 – 2026"))
    cv.add_sub(edu["university"])
    cv.add_bullet(edu["specialization"])
    cv.add_bullet(edu["project"])
    cv.add_entry(f"Secondary — {edu['secondary_spec']}", d.get("sec_year","2023"))
    cv.add_sub(edu["secondary_school"])
    cv.add_bullet(edu["grade"])
    
    exp = d["experience"]
    cv.add_section("Experience")
    cv.add_entry(exp["volunteer_org"], d.get("vol_dates","2025 – Present"))
    cv.add_sub(d["city"])
    for b in exp["volunteer_bullets"]: cv.add_bullet(b)
    cv.add_entry(exp["placement_org"], d.get("stage_date","June 2024"))
    cv.add_sub(d["city"])
    for b in exp["placement_bullets"]: cv.add_bullet(b)
    
    cv.add_section("Skills")
    cv.add_skills(d["cv_skills"]["left"], d["cv_skills"]["right"])
    
    cv.add_section("Languages")
    for l in d["languages"]: cv.add_bullet(l)
    
    cv.add_section("Interests")
    cv.add_text(d["interests"])
    
    cv.save(output_path)
    return cv.get_id()
