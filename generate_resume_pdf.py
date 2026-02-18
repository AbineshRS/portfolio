"""
Generate resume PDF to match your uploaded design exactly:
- White background, black/grey text
- Header: name left, contact (phone, email, location) top right, thin horizontal line
- Left column: EDUCATION, then SKILLS (two-column bullet list)
- Right column: PROFESSIONAL SUMMARY, then EXPERIENCE
"""
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
dep_path = ROOT / ".pydeps"
if dep_path.exists():
    sys.path.insert(0, str(dep_path))

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT_FILE = ROOT / "assets" / "Abinesh_RS_Resume.pdf"

# Your uploaded style: simple black/grey
TEXT_COLOR = colors.HexColor("#1a1a1a")
HEADING_COLOR = colors.HexColor("#1a1a1a")
LINE_COLOR = colors.HexColor("#888888")
BULLET_COLOR = colors.HexColor("#555555")


def register_fonts() -> None:
    for name, path in [
        ("Calibri", Path("C:/Windows/Fonts/calibri.ttf")),
        ("Calibri-Bold", Path("C:/Windows/Fonts/calibrib.ttf")),
    ]:
        if path.exists():
            pdfmetrics.registerFont(TTFont(name, str(path)))


def f_regular() -> str:
    return "Calibri" if "Calibri" in pdfmetrics.getRegisteredFontNames() else "Helvetica"


def f_bold() -> str:
    return "Calibri-Bold" if "Calibri-Bold" in pdfmetrics.getRegisteredFontNames() else "Helvetica-Bold"


def draw_section_title(c: canvas.Canvas, x: float, y: float, title: str, width: float) -> float:
    c.setFillColor(HEADING_COLOR)
    c.setFont(f_bold(), 11)
    c.drawString(x, y, title.upper())
    c.setStrokeColor(LINE_COLOR)
    c.setLineWidth(0.8)
    c.line(x, y - 3, x + width, y - 3)
    return y - 18


def draw_wrapped_text(
    c: canvas.Canvas, x: float, y: float, text: str, width: float,
    font_size: float = 10, leading: float = 13,
) -> float:
    c.setFont(f_regular(), font_size)
    c.setFillColor(TEXT_COLOR)
    words = text.split()
    line = ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if c.stringWidth(candidate, f_regular(), font_size) <= width:
            line = candidate
        else:
            c.drawString(x, y, line)
            y -= leading
            line = word
    if line:
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_bullets(
    c: canvas.Canvas, x: float, y: float, items: list[str], width: float,
    font_size: float = 10, leading: float = 13,
) -> float:
    for item in items:
        c.setFillColor(BULLET_COLOR)
        c.circle(x + 2.5, y + 4, 1.2, fill=1, stroke=0)
        y = draw_wrapped_text(c, x + 8, y, item, width - 8, font_size=font_size, leading=leading)
        y -= 2
    return y


def draw_resume() -> None:
    register_fonts()
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(OUT_FILE), pagesize=A4)
    page_w, page_h = A4

    c.setFillColor(colors.white)
    c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

    margin = 40
    left = margin
    right = page_w - margin
    split_x = 300
    left_col_w = split_x - left - 20
    right_col_w = right - split_x

    # ----- Header (your design) -----
    header_y = page_h - 44
    c.setFillColor(HEADING_COLOR)
    c.setFont(f_bold(), 22)
    c.drawString(left, header_y, "ABINESH R S")

    c.setFont(f_regular(), 9.5)
    c.setFillColor(TEXT_COLOR)
    c.drawRightString(right, header_y, "8300893013")
    c.drawRightString(right, header_y - 12, "abiabinesh483@gmail.com")
    c.drawRightString(right, header_y - 24, "Kanyakumari, Tamil Nadu, India 629168")
    c.drawRightString(right, header_y - 36, "linkedin.com/in/abineshrs")

    # Thin horizontal line under header
    line_y = page_h - 70
    c.setStrokeColor(LINE_COLOR)
    c.setLineWidth(0.6)
    c.line(left, line_y, right, line_y)

    content_start = line_y - 24

    # ==================== LEFT COLUMN: EDUCATION + SKILLS ====================
    y_left = content_start

    y_left = draw_section_title(c, left, y_left, "Education", left_col_w)

    # Nesamony - Master's
    c.setFillColor(HEADING_COLOR)
    c.setFont(f_bold(), 10)
    c.drawString(left, y_left, "Nesamony Memorial Christian College, Marthandam")
    y_left -= 12
    c.setFont(f_regular(), 9.5)
    c.setFillColor(TEXT_COLOR)
    c.drawString(left, y_left, "Master's Degree in Computers Science")
    y_left -= 11
    c.drawString(left, y_left, "2022-2024")
    y_left -= 11
    c.drawString(left, y_left, "CGPA-8.14")
    y_left -= 18

    # Nesamony - Bachelor's
    c.setFillColor(HEADING_COLOR)
    c.setFont(f_bold(), 10)
    c.drawString(left, y_left, "Nesamony Memorial Christian College, Marthandam")
    y_left -= 12
    c.setFont(f_regular(), 9.5)
    c.setFillColor(TEXT_COLOR)
    c.drawString(left, y_left, "Bachelor Degree in Computers Science")
    y_left -= 11
    c.drawString(left, y_left, "2019-2022")
    y_left -= 11
    c.drawString(left, y_left, "CGPA-7.74")
    y_left -= 18

    # Hindu Vidyalaya - 12th
    c.setFillColor(HEADING_COLOR)
    c.setFont(f_bold(), 10)
    c.drawString(left, y_left, "Hindu Vidyalaya Marthandam. HSS")
    y_left -= 12
    c.setFont(f_regular(), 9.5)
    c.setFillColor(TEXT_COLOR)
    c.drawString(left, y_left, "12th Grade | 2018-2019")
    y_left -= 11
    c.drawString(left, y_left, "Percentage: 57%")
    y_left -= 18

    # Hindu Vidyalaya - 10th
    c.setFillColor(HEADING_COLOR)
    c.setFont(f_bold(), 10)
    c.drawString(left, y_left, "Hindu Vidyalaya Marthandam. HSS")
    y_left -= 12
    c.setFont(f_regular(), 9.5)
    c.setFillColor(TEXT_COLOR)
    c.drawString(left, y_left, "10th Grade | 2016-2017")
    y_left -= 11
    c.drawString(left, y_left, "Percentage: 78%")
    y_left -= 22

    # SKILLS (two-column list, as in your upload)
    y_left = draw_section_title(c, left, y_left, "Skills", left_col_w)
    skill_w = (left_col_w - 8) / 2
    skills_left = ["HTML CSS", "Angular js", "WPF", "React js"]
    skills_right = ["ASP.NET", ".Net (web api)", "SQL server", "Git"]
    c.setFont(f_regular(), 9.5)
    c.setFillColor(TEXT_COLOR)
    for i, sk in enumerate(skills_left):
        c.drawString(left, y_left - i * 14, sk)
    for i, sk in enumerate(skills_right):
        c.drawString(left + skill_w + 8, y_left - i * 14, sk)

    # ==================== RIGHT COLUMN: PROFESSIONAL SUMMARY + EXPERIENCE ====================
    y_right = content_start

    y_right = draw_section_title(c, split_x, y_right, "Professional Summary", right_col_w)
    summary = (
        ".NET Developer with a strong background in designing, developing, and maintaining "
        "web and desktop applications. Proficient in C#, ASP.NET Core/MVC, WPF, and API development. "
        "Skilled in database management using SQL Server and Entity Framework. Experienced in front-end "
        "technologies such as Angular js, HTML, CSS, Bootstrap. Passionate about writing clean, maintainable "
        "code and collaborating with teams."
    )
    y_right = draw_wrapped_text(c, split_x, y_right, summary, right_col_w, font_size=10, leading=13)
    y_right -= 16

    y_right = draw_section_title(c, split_x, y_right, "Experience", right_col_w)

    # Srishti Innovative - [Internship]
    c.setFillColor(HEADING_COLOR)
    c.setFont(f_bold(), 10.5)
    c.drawString(split_x, y_right, "Srishti Innovative - [Internship] | December 2023-June 2024")
    y_right -= 12
    c.setFont(f_regular(), 9.5)
    c.setFillColor(TEXT_COLOR)
    c.drawString(split_x, y_right, "Role: React js + .Net - E-Commerce")
    y_right -= 14
    y_right = draw_bullets(c, split_x, y_right, [
        "Developed and maintained a Real Estate Management System using .NET and React js, ensuring a user-friendly interface and seamless patient data management.",
        "Database structures using SQL Server, improving data retrieval and storage efficiency, and using stored procedures. Utilized Git for version control and collaborated with cross-functional teams to deliver timely project updates.",
    ], right_col_w, font_size=9.2, leading=12)
    y_right -= 10

    # Keesa Express - [Working]
    c.setFillColor(HEADING_COLOR)
    c.setFont(f_bold(), 10.5)
    c.drawString(split_x, y_right, "Keesa Express - [Working] | Currently August 2024")
    y_right -= 12
    c.setFont(f_regular(), 9.5)
    c.setFillColor(TEXT_COLOR)
    c.drawString(split_x, y_right, "Role: NET Developer (WPF Framework) - Hospital Management Project")
    y_right -= 14
    y_right = draw_bullets(c, split_x, y_right, [
        "Developed and maintained a Hospital Management System using .NET and WPF, ensuring a user-friendly interface and seamless patient data management.",
        "Database structures using SQL Server, improving data retrieval and storage efficiency, and using stored procedures. Utilized Git for version control and collaborated with cross-functional teams to deliver timely project updates.",
    ], right_col_w, font_size=9.2, leading=12)
    y_right -= 10

    # NET Developer (Angular + .Net) - Digital ESET Keys Purchasing
    c.setFillColor(HEADING_COLOR)
    c.setFont(f_bold(), 10.5)
    c.drawString(split_x, y_right, "NET Developer (Angular + .Net) - Digital ESET Keys Purchasing")
    y_right -= 14
    y_right = draw_bullets(c, split_x, y_right, [
        "Developed and maintained an ESET key using .NET web API, Angular Type script.",
        "Database structures using SQL Server, improving data retrieval and storage efficiency, and using stored procedures for the user interface using Tailwind, HTML, CSS.",
        "Used Git for version control and followed agile methodologies for efficient project development.",
    ], right_col_w, font_size=9.2, leading=12)
    c.setFont(f_regular(), 8.5)
    c.setFillColor(colors.HexColor("#333333"))
    c.drawString(split_x, y_right, "https://github.com/AbineshRS/OnSoft_api.git")
    y_right -= 11
    c.drawString(split_x, y_right, "https://github.com/AbineshRS/Oonsoft_admin.git")
    y_right -= 14

    # NET Developer (Angular + .Net) - Custom Clearance Invoice
    c.setFillColor(HEADING_COLOR)
    c.setFont(f_bold(), 10.5)
    c.drawString(split_x, y_right, "NET Developer (Angular + .Net) - Custom Clearance Invoice")
    y_right -= 14
    y_right = draw_bullets(c, split_x, y_right, [
        "Custom Clearance Invoice's sending to customer from the company will verify the invoice and update it key using .NET web API, Angular.",
        "Type script, Database structures using SQL Server, improving data retrieval and storage efficiency and using stored procedures for the user interface using Tailwind, HTML, CSS. Used Git for version control and followed agile methodologies for efficient project development.",
    ], right_col_w, font_size=9.2, leading=12)

    c.save()


if __name__ == "__main__":
    draw_resume()
    print(f"Resume PDF (your uploaded design) created: {OUT_FILE}")
