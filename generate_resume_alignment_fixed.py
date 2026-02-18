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


OUT_FILE = ROOT / "assets" / "Abinesh_RS_Resume_Alignment_Fixed.pdf"


def reg_font() -> str:
    return "Calibri" if "Calibri" in pdfmetrics.getRegisteredFontNames() else "Helvetica"


def bold_font() -> str:
    return "Calibri-Bold" if "Calibri-Bold" in pdfmetrics.getRegisteredFontNames() else "Helvetica-Bold"


def register_fonts() -> None:
    calibri = Path("C:/Windows/Fonts/calibri.ttf")
    calibri_bold = Path("C:/Windows/Fonts/calibrib.ttf")
    if calibri.exists():
        pdfmetrics.registerFont(TTFont("Calibri", str(calibri)))
    if calibri_bold.exists():
        pdfmetrics.registerFont(TTFont("Calibri-Bold", str(calibri_bold)))


def wrap_text(c: canvas.Canvas, x: float, y: float, width: float, text: str, size: float = 10.3, leading: float = 14) -> float:
    c.setFont(reg_font(), size)
    c.setFillColor(colors.HexColor("#1f2e45"))
    words = text.split()
    line = ""
    for word in words:
        cand = (line + " " + word).strip()
        if c.stringWidth(cand, reg_font(), size) <= width:
            line = cand
        else:
            c.drawString(x, y, line)
            y -= leading
            line = word
    if line:
        c.drawString(x, y, line)
        y -= leading
    return y


def section_head(c: canvas.Canvas, x: float, y: float, label: str, line_width: float) -> float:
    c.setFont(bold_font(), 11.5)
    c.setFillColor(colors.HexColor("#122d53"))
    c.drawString(x, y, label.upper())
    c.setStrokeColor(colors.HexColor("#2f63b7"))
    c.setLineWidth(1.2)
    c.line(x, y - 4, x + line_width, y - 4)
    return y - 20


def bullets(c: canvas.Canvas, x: float, y: float, width: float, items: list[str], size: float = 10.2, leading: float = 14) -> float:
    for item in items:
        c.setFillColor(colors.HexColor("#2f63b7"))
        c.circle(x + 2, y + 4, 1.6, fill=1, stroke=0)
        y = wrap_text(c, x + 9, y, width - 9, item, size=size, leading=leading)
        y -= 1
    return y


def draw() -> None:
    register_fonts()
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(OUT_FILE), pagesize=A4)
    pw, ph = A4

    # white page
    c.setFillColor(colors.white)
    c.rect(0, 0, pw, ph, fill=1, stroke=0)

    # Keep uploaded style: dark left panel + clean right area
    left_w = 176
    c.setFillColor(colors.HexColor("#10294d"))
    c.rect(0, 0, left_w, ph, fill=1, stroke=0)

    # Header
    c.setFillColor(colors.white)
    c.setFont(bold_font(), 20)
    c.drawString(20, ph - 60, "ABINESH R S")
    c.setFont(reg_font(), 11.4)
    c.setFillColor(colors.HexColor("#d2e1ff"))
    c.drawString(20, ph - 82, "Full-Stack .NET Developer")

    sx = 20
    sy = ph - 126

    def side_title(t: str) -> None:
        nonlocal sy
        c.setFillColor(colors.white)
        c.setFont(bold_font(), 11)
        c.drawString(sx, sy, t.upper())
        sy -= 16

    side_title("Contact")
    c.setFillColor(colors.HexColor("#eaf1ff"))
    for line in [
        "+91 8300893013",
        "abiabinesh483@gmail.com",
        "Kanyakumari, Tamil Nadu",
        "linkedin.com/in/abineshrs",
        "github.com/AbineshRS",
    ]:
        sy = wrap_text(c, sx, sy, left_w - 28, line, size=9.4, leading=12.5)
        sy -= 1

    sy -= 8
    side_title("Skills")
    skill_lines = [
        "C#, .NET, ASP.NET Core",
        ".NET Web API, MVC",
        "SQL Server, EF, SPs",
        "Angular, React, TypeScript",
        "HTML, CSS, Bootstrap",
        "WPF, Git, Agile",
    ]
    for skill in skill_lines:
        c.setFillColor(colors.HexColor("#90b8ff"))
        c.circle(sx + 2, sy + 4, 1.5, fill=1, stroke=0)
        sy = wrap_text(c, sx + 8, sy, left_w - 34, skill, size=9.5, leading=12.3)

    sy -= 6
    side_title("Languages")
    sy = wrap_text(c, sx, sy, left_w - 28, "Tamil, Malayalam, English", size=9.6, leading=12.3)

    # Right content
    rx = left_w + 24
    rw = pw - rx - 28
    y = ph - 62

    y = section_head(c, rx, y, "Professional Summary", 235)
    summary = (
        ".NET Developer with strong experience in designing, developing, and maintaining "
        "web and desktop applications. Proficient in C#, ASP.NET Core/MVC, WPF, and API "
        "development. Skilled in SQL Server, Entity Framework, Angular, React, HTML, CSS, "
        "and Bootstrap. Passionate about clean, maintainable code and team collaboration."
    )
    y = wrap_text(c, rx, y, rw, summary, size=10.5, leading=14.3)
    y -= 2

    y = section_head(c, rx, y, "Experience", 150)

    c.setFillColor(colors.HexColor("#122d53"))
    c.setFont(bold_font(), 12)
    c.drawString(rx, y, ".NET Developer | Keesa Express")
    c.setFillColor(colors.HexColor("#5f6f86"))
    c.setFont(reg_font(), 10.1)
    c.drawRightString(rx + rw, y, "Aug 2024 - Present")
    y -= 16
    y = bullets(
        c,
        rx,
        y,
        rw,
        [
            "Worked on Digital ESET Keys Purchasing and Custom Clearance Invoice systems.",
            "Developed .NET Web APIs with authentication, validation, and business workflows.",
            "Designed SQL Server tables and stored procedures for efficient data retrieval.",
            "Built UI modules with Angular/TypeScript and integrated with backend APIs.",
        ],
        size=10.4,
        leading=14.1,
    )
    y -= 6

    c.setFillColor(colors.HexColor("#122d53"))
    c.setFont(bold_font(), 12)
    c.drawString(rx, y, ".NET Developer Intern | Srishti Innovative")
    c.setFillColor(colors.HexColor("#5f6f86"))
    c.setFont(reg_font(), 10.1)
    c.drawRightString(rx + rw, y, "Dec 2023 - Jun 2024")
    y -= 16
    y = bullets(
        c,
        rx,
        y,
        rw,
        [
            "Developed a WPF Hospital Management project with patient and appointment workflows.",
            "Worked on School Management and Real Estate modules using .NET + SQL Server.",
            "Collaborated with cross-functional teams and used Git for version control.",
        ],
        size=10.4,
        leading=14.1,
    )
    y -= 4

    y = section_head(c, rx, y, "Education", 140)
    y = bullets(
        c,
        rx,
        y,
        rw,
        [
            "Master's Degree in Computer Science | 2022 - 2024 | CGPA 8.14 | Nesamony Memorial Christian College, Marthandam",
            "Bachelor's Degree in Computer Science | 2019 - 2022 | CGPA 7.74 | Nesamony Memorial Christian College, Marthandam",
            "12th Grade | 2018 - 2019 | 57% | Hindu Vidyalaya Marthandam HSS",
            "10th Grade | 2016 - 2017 | 78% | Hindu Vidyalaya Marthandam HSS",
        ],
        size=9.8,
        leading=13.2,
    )

    c.showPage()
    c.save()


if __name__ == "__main__":
    draw()
    print(f"Alignment-fixed resume PDF created: {OUT_FILE}")
