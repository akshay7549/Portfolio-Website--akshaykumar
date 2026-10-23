"""Build the selectable-text portfolio resume with ReportLab."""
import sys
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

FONT_DIR = Path('C:/Windows/Fonts')
for name, filename in [('Calibri', 'calibri.ttf'), ('Calibri-Bold', 'calibrib.ttf'), ('Calibri-Italic', 'calibrii.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / filename)))
pdfmetrics.registerFontFamily('Calibri', normal='Calibri', bold='Calibri-Bold', italic='Calibri-Italic', boldItalic='Calibri-Bold')

INK = colors.HexColor('#17232F')
ACCENT = colors.HexColor('#1D5369')
MUTED = colors.HexColor('#4C5964')
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Name', fontName='Calibri-Bold', fontSize=23, leading=27, textColor=INK, alignment=TA_CENTER, spaceAfter=4))
styles.add(ParagraphStyle(name='Role', fontName='Calibri', fontSize=11.5, leading=15, textColor=ACCENT, alignment=TA_CENTER, spaceAfter=6))
styles.add(ParagraphStyle(name='Contact', fontName='Calibri', fontSize=9, leading=12.5, textColor=MUTED, alignment=TA_CENTER))
styles.add(ParagraphStyle(name='SectionTitle', fontName='Calibri-Bold', fontSize=11.3, leading=14, textColor=ACCENT, spaceBefore=14, spaceAfter=7, keepWithNext=True))
styles.add(ParagraphStyle(name='ResumeBody', fontName='Calibri', fontSize=10.1, leading=13.5, textColor=INK, spaceAfter=5))
styles.add(ParagraphStyle(name='BulletText', parent=styles['ResumeBody'], leftIndent=10, firstLineIndent=-8, spaceAfter=4))
styles.add(ParagraphStyle(name='JobTitle', fontName='Calibri-Bold', fontSize=11, leading=14, textColor=INK, spaceAfter=2, keepWithNext=True))
styles.add(ParagraphStyle(name='Meta', fontName='Calibri-Italic', fontSize=9.8, leading=13, textColor=MUTED, spaceAfter=6, keepWithNext=True))
styles.add(ParagraphStyle(name='LinkLine', fontName='Calibri', fontSize=9, leading=12, textColor=ACCENT, spaceAfter=7))

# Compact spacing for a readable single-page resume.
styles['Name'].fontSize=21
styles['Name'].leading=24
styles['Role'].spaceAfter=4
styles['Contact'].leading=11
styles['SectionTitle'].spaceBefore=9
styles['SectionTitle'].spaceAfter=4
styles['ResumeBody'].fontSize=9.7
styles['ResumeBody'].leading=12
styles['ResumeBody'].spaceAfter=3
styles['BulletText'].fontSize=9.7
styles['BulletText'].leading=12
styles['BulletText'].spaceAfter=3
styles['JobTitle'].fontSize=10.5
styles['JobTitle'].leading=13
styles['Meta'].fontSize=9.2
styles['Meta'].leading=11.5
styles['Meta'].spaceAfter=3
styles['LinkLine'].leading=11
styles['LinkLine'].spaceAfter=4

story=[]
def p(text, style='ResumeBody'):
    return Paragraph(text, styles[style])
def section(title):
    story.append(p(title.upper(), 'SectionTitle'))
def bullet(text):
    return p('&#8226; '+text, 'BulletText')
def job(title, meta, bullets):
    story.append(KeepTogether([p(title, 'JobTitle'), p(meta, 'Meta'), bullet(bullets[0])]))
    story.extend(bullet(text) for text in bullets[1:])
    story.append(Spacer(1,3))
def link(label,url):
    return '<link href="'+url+'" color="#1D5369">'+label+'</link>'

story.extend([
 p('AKSHAY KUMAR','Name'),
 p('Freelance Web Developer | Network Engineer','Role'),
 p('New Delhi, NCR (Open to Noida / Gurugram) | +91 7549645076 | '+link('akshaykumarstm2020@gmail.com','mailto:akshaykumarstm2020@gmail.com'),'Contact'),
 p(link('theakshaydev.space','https://theakshaydev.space/')+' | '+link('GitHub: akshay7549','https://github.com/akshay7549')+' | '+link('LinkedIn: Akshay Kumar','https://www.linkedin.com/in/akshay-kumar-090990249/'),'Contact')
])
section('Professional Summary')
story.append(p('Freelance Web Developer and Network Engineer building responsive business websites, booking platforms and dashboards. Hands-on experience in deployment, network troubleshooting, Windows/Linux support and ticket-based incident resolution.'))
section('Key Skills')
for text in [
 '<b>Web:</b> HTML, CSS, JavaScript, Python, Django, Flask, PHP, Laravel, MySQL, Git/GitHub.',
 '<b>Infrastructure:</b> LAN/WAN, TCP/IP, subnetting, VPN, Cisco Packet Tracer, Windows, Linux, VMware.',
 '<b>Support:</b> MSG91 ticketing, incident escalation, patch management, remote and hardware troubleshooting.'
]: story.append(p(text))
section('Professional Experience')
job('Freelance Web Developer', 'Independent | Business websites &amp; web applications | Project-based', [
 'Build responsive business websites, service catalogues, booking workflows and management dashboards, including NextGen, Sukoon and Khushi projects.',
 'Manage website deployment, domain setup, troubleshooting and ongoing content updates.'
])
job('Network Engineer (Network Support)', 'Tech Guru IT Solutions, New Delhi | April 2026 - Present', [
 'Support up to 50 end users across IP configuration, VPN and LAN/WAN connectivity; resolve 10-20 network, hardware and software tickets daily.',
 'Track incidents through MSG91; handle escalation, patching, Windows/VMware configuration and resolution documentation.'
])
section('Selected Projects')
projects=[
 ('NextGen Lapy World', 'Business website | Repair booking, tracking &amp; device catalogue', [
 'Built a device repair website with service discovery, repair booking and tracking IDs, a laptop catalogue and WhatsApp contact pathways.'
 ], [('Live website: nextgenlapyworld.in','https://nextgenlapyworld.in/')]),
 ('Sukoon Wellness &amp; Spa', 'Booking &amp; operations platform | Laravel, PHP, MySQL', [
 'Built booking and staff allocation workflows with double-booking protection, role-based dashboards, billing, CRM, inventory and reports.'
 ], [('Live website: sukoonwellnessandspa.in','https://sukoonwellnessandspa.in/')]),
 ('Khushi Decoration &amp; Seasonal Store', 'Responsive business showcase | HTML, CSS, JavaScript', [
 'Built a responsive shop showcase with category filters, photo galleries, an event catalogue and interactive shop map; deployed on GitHub Pages.'
 ], [('Live website','https://akshay7549.github.io/khushi-decoration/'),('GitHub repository','https://github.com/akshay7549/khushi-decoration')])
]
for title,meta,bullets,links in projects:
    job(title,meta,bullets)
    story.append(p(' | '.join(link(label,url) for label,url in links),'LinkLine'))

section('Education & Certifications')
story.append(p('<b>Bachelor of Computer Applications</b> | CGPA: 8/10 | Sep 2022 - June 2025'))
story.append(p('Datta Meghe Institute of Higher Education and Research, Wardha','Meta'))
story.append(p('<b>Advanced Cyber Security (In Progress)</b> | CRAW Security, Delhi | Aug 2025 - Present'))
story.append(p('<b>Certifications:</b> Computer Networking; Linux Essentials - CRAW Security'))

def footer(canvas,doc):
    width,height=A4
    canvas.setStrokeColor(colors.HexColor('#D6DEE3'))
    canvas.setLineWidth(.5)
    canvas.line(42,37,width-42,37)
    canvas.setFont('Calibri',8)
    canvas.setFillColor(MUTED)
    canvas.drawString(42,25,'Akshay Kumar | theakshaydev.space')
    canvas.drawRightString(width-42,25,str(doc.page))

out=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'assets'/'Akshay-Kumar-Resume.pdf'
out.parent.mkdir(parents=True,exist_ok=True)
doc=SimpleDocTemplate(str(out),pagesize=A4,rightMargin=36,leftMargin=36,topMargin=27,bottomMargin=47,title='Akshay Kumar - Resume',author='Akshay Kumar',subject='Freelance Web Developer and Network Engineer')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(out)
