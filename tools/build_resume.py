"""Build the selectable-text portfolio resume with ReportLab."""
import sys
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether

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
    story.append(Spacer(1,5))
def link(label,url):
    return '<link href="'+url+'" color="#1D5369">'+label+'</link>'

story.extend([
 p('AKSHAY KUMAR','Name'),
 p('Freelance Web Developer | Network Engineer','Role'),
 p('New Delhi, NCR (Open to Noida / Gurugram) | +91 7549645076 | '+link('akshaykumarstm2020@gmail.com','mailto:akshaykumarstm2020@gmail.com'),'Contact'),
 p(link('theakshaydev.space','https://theakshaydev.space/')+' | '+link('GitHub: akshay7549','https://github.com/akshay7549')+' | '+link('LinkedIn: Akshay Kumar','https://www.linkedin.com/in/akshay-kumar-090990249/'),'Contact')
])
section('Professional Summary')
story.append(p('Freelance Web Developer and Network Engineer with hands-on experience building responsive business websites and supporting networks, Windows/Linux systems and end users. Develops service catalogues, booking workflows and management dashboards, with deployment and troubleshooting experience. Skilled in IP configuration, subnetting, LAN/WAN connectivity, VPN access and ticket-based incident handling, with a customer-first approach.'))
section('Key Skills')
for text in [
 '<b>Web development:</b> HTML, CSS, JavaScript, Python, Django, Flask, PHP, Laravel, MySQL, Git/GitHub; responsive websites and deployment.',
 '<b>Networking:</b> LAN/WAN, TCP/IP, IP configuration, subnetting, VPN access, Cisco Packet Tracer, network troubleshooting and connectivity diagnostics.',
 '<b>Systems &amp; security:</b> Windows, Linux, user/account access, patch management, VMware, network security fundamentals.',
 '<b>Support &amp; tools:</b> MSG91 ticketing, incident logging and escalation, SLA-based resolution, desktop/laptop/printer diagnostics, AnyDesk, UltraViewer, Microsoft 365 and Outlook.'
]: story.append(p(text))
section('Professional Experience')
job('Freelance Web Developer', 'Independent | Business websites &amp; web applications | Project-based', [
 'Build responsive business websites and web applications, including NextGen Lapy World, Sukoon Wellness &amp; Spa and Khushi Decoration.',
 'Develop service catalogues, booking workflows, contact pages and management dashboards based on project requirements.',
 'Handle website deployment, domain setup, troubleshooting and ongoing content updates.'
])
job('Network Engineer (Network Support)', 'Tech Guru IT Solutions, New Delhi | April 2026 - Present', [
 'Provide first-line network support for up to 50 end users, configuring and troubleshooting IP settings, VPN access and LAN/WAN connectivity.',
 'Diagnose network, hardware, software and printer issues; resolve 10-20 support tickets per day with clear user communication.',
 'Log, track and resolve incidents through MSG91, following documented SLA and escalation processes for complex issues.',
 'Carry out patch/update management and Windows system configuration; configure VMware virtual machines for testing and system setup.',
 'Document resolutions and configurations in a shared knowledge base; follow up after escalation to confirm resolution and user satisfaction.'
])

story.append(PageBreak())
story.append(p('AKSHAY KUMAR','JobTitle'))
story.append(p('Selected projects, education &amp; certifications','Meta'))
section('Selected Projects')
projects=[
 ('NextGen Lapy World', 'Business website | Repair booking, tracking &amp; device catalogue', [
 'Built a customer-facing website for a device repair business in Nehru Place, with device-specific service discovery and repair booking.',
 'Added repair tracking using a tracking ID, a laptop catalogue and WhatsApp contact pathways.'
 ], [('Live website: nextgenlapyworld.in','https://nextgenlapyworld.in/')]),
 ('Sukoon Wellness &amp; Spa', 'Booking &amp; operations platform | Laravel, PHP, MySQL', [
 'Developed booking workflows, staff allocation with double-booking protection, staff dashboards and role-based access.',
 'Built business management features covering services, rooms, bookings and payments, with CRM, billing, inventory and reporting workflows.'
 ], [('Live website: sukoonwellnessandspa.in','https://sukoonwellnessandspa.in/')]),
 ('Khushi Decoration &amp; Seasonal Store', 'Responsive business showcase | HTML, CSS, JavaScript', [
 'Built a responsive showcase for a business in Dema, Bihar, featuring decoration collections, bouquets, gifts and wedding car decoration.',
 'Implemented category filters, photo galleries, a photo viewer, an event catalogue and an interactive shop map; published with GitHub Pages.'
 ], [('Live website','https://akshay7549.github.io/khushi-decoration/'),('GitHub repository','https://github.com/akshay7549/khushi-decoration')])
]
for title,meta,bullets,links in projects:
    job(title,meta,bullets)
    story.append(p(' | '.join(link(label,url) for label,url in links),'LinkLine'))

section('Education & Training')
story.append(p('Bachelor of Computer Applications | CGPA: 8/10','JobTitle'))
story.append(p('Datta Meghe Institute of Higher Education and Research, Wardha | Sep 2022 - June 2025','Meta'))
story.append(p('Advanced Cyber Security (In Progress)','JobTitle'))
story.append(p('CRAW Security, Delhi | Aug 2025 - Present','Meta'))
section('Certifications')
story.append(bullet('Computer Networking - CRAW Security'))
story.append(bullet('Linux Essentials (Basic Commands, Networking) - CRAW Security'))

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
doc=SimpleDocTemplate(str(out),pagesize=A4,rightMargin=42,leftMargin=42,topMargin=35,bottomMargin=49,title='Akshay Kumar - Resume',author='Akshay Kumar',subject='Freelance Web Developer and Network Engineer')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(out)
