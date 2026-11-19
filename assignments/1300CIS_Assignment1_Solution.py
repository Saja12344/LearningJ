#!/usr/bin/env python3
"""Generate 1300CIS Assignment 1 solution as a formatted Word document."""

from docx import Document
from docx.shared import Pt, Cm, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


def set_run_font(run, size=12, bold=False):
    run.font.name = "Times New Roman"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    run.font.size = Pt(size)
    run.bold = bold


def add_para(doc, text, bold=False, size=12, space_after=6, first_line_indent=None):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    pf.space_after = Pt(space_after)
    pf.space_before = Pt(0)
    if first_line_indent is not None:
        pf.first_line_indent = first_line_indent
    run = p.add_run(text)
    set_run_font(run, size=size, bold=bold)
    return p


def add_heading_custom(doc, text):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    pf.space_before = Pt(10)
    pf.space_after = Pt(6)
    run = p.add_run(text)
    set_run_font(run, size=12, bold=True)
    return p


def set_cell_text(cell, text, bold=False):
    cell.text = ""
    p = cell.paragraphs[0]
    pf = p.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    pf.space_after = Pt(2)
    run = p.add_run(text)
    set_run_font(run, size=11, bold=bold)


def shade_cell(cell, color_hex="D9E2F3"):
    tc = cell._tePr if hasattr(cell, "_tePr") else cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), color_hex)
    shd.set(qn("w:val"), "clear")
    tcPr.append(shd)


def main():
    doc = Document()

    # Page setup: 2.5 cm margins
    for section in doc.sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.5)

    # Default style
    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(12)
    style._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    style.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE

    # Header / student info
    add_para(doc, "King Khalid University", bold=True, space_after=0)
    add_para(doc, "College of Computer Science", bold=True, space_after=0)
    add_para(
        doc,
        "Department of Informatics and Computer Systems",
        bold=True,
        space_after=6,
    )
    add_para(doc, "Course: Introduction to Information Systems – 1300CIS", space_after=0)
    add_para(
        doc,
        "Assignment: An Information System in Your Daily Life",
        space_after=0,
    )
    add_para(doc, "Name: [Write your full name here]", space_after=0)
    add_para(doc, "Student ID: [Write your student ID here]", space_after=0)
    add_para(doc, "Section: [Write your section number here]", space_after=12)

    # ========== Question 1 ==========
    add_heading_custom(doc, "1. Describe Your Experience")
    add_para(
        doc,
        "The information system I used is the King Khalid University student portal "
        "(university registration / academic system). The specific process I focused on "
        "is registering for a course for the current academic term. I used the system on "
        "18 November 2026 for the purpose of adding one required course to my study plan "
        "so that I could complete my registration before the deadline.",
    )
    add_para(
        doc,
        "Three steps I completed during this process were as follows. First, I signed in "
        "to the student portal using my university username and password and opened the "
        "course registration page. Second, I searched for the course by its code and "
        "selected an available section that fit my timetable. Third, I confirmed the "
        "selection and submitted the registration request.",
    )
    add_para(
        doc,
        "One specific detail I observed was a confirmation message that appeared after "
        "submission. The message showed that the course had been added successfully and "
        "displayed the course code, section number, and credit hours. The system also "
        "required me to enter my password again before final confirmation, which helped "
        "prevent accidental registration changes.",
    )
    add_para(
        doc,
        "[Insert screenshots here: (1) login / registration page with personal data "
        "hidden, (2) course selection screen, (3) confirmation message after successful "
        "registration. Hide your name, ID, and password fields.]",
        bold=False,
    )

    # ========== Question 2 ==========
    add_heading_custom(doc, "2. Identify the Information System Components")
    add_para(
        doc,
        "The following table shows the six main components of the information system "
        "and how each one appears in the course registration process.",
    )

    table = doc.add_table(rows=7, cols=3)
    table.style = "Table Grid"

    headers = ["Component", "Example in the process", "Role"]
    for i, h in enumerate(headers):
        set_cell_text(table.rows[0].cells[i], h, bold=True)
        shade_cell(table.rows[0].cells[i], "D9E2F3")

    rows = [
        (
            "Hardware",
            "My laptop (or smartphone) and the university servers that host the portal.",
            "The laptop is the device I used to access the system. The servers store and "
            "process registration requests so many students can register at the same time.",
        ),
        (
            "Software",
            "The student portal web application and the web browser (for example, Chrome).",
            "The portal software provides the registration screens, checks available seats, "
            "and applies registration rules. The browser displays the interface and sends "
            "my requests to the server.",
        ),
        (
            "Data",
            "Course code, section number, my student ID, and the selected term.",
            "These raw facts are entered or retrieved during registration. Without accurate "
            "data, the system cannot assign the correct course or update my timetable.",
        ),
        (
            "People",
            "Students (users), academic advisors, and system administrators.",
            "Students use the system to register. Advisors may approve or guide course "
            "choices. Administrators maintain the portal, open registration periods, and "
            "fix technical problems.",
        ),
        (
            "Networks",
            "The Internet connection between my device and the university network.",
            "The network transfers login data and registration requests securely from my "
            "device to the university servers and returns confirmation messages to me.",
        ),
        (
            "Database",
            "The academic database that stores courses, sections, seats, and student records.",
            "The database keeps organized records of offered courses, remaining seats, and "
            "my registered courses. When I register, it updates my record and reduces the "
            "available seats in that section.",
        ),
    ]

    for r_idx, (comp, example, role) in enumerate(rows, start=1):
        set_cell_text(table.rows[r_idx].cells[0], comp, bold=True)
        set_cell_text(table.rows[r_idx].cells[1], example)
        set_cell_text(table.rows[r_idx].cells[2], role)

    doc.add_paragraph()  # spacing after table

    # ========== Question 3 ==========
    add_heading_custom(doc, "3. Explain How Data Becomes Information")
    add_para(
        doc,
        "Data are raw facts, while information is data that has been processed and "
        "organized so that it becomes meaningful for decision-making.",
    )
    add_para(
        doc,
        "Two examples of data entered or recorded during the process are: (1) the course "
        "code I typed or selected (for example, 1300CIS), and (2) the section number and "
        "term I chose. At that stage, these values are only facts stored by the system.",
    )
    add_para(
        doc,
        "One example of information produced by the system is my updated registered-course "
        "list (or registration summary). This summary combines several data items—course "
        "name, section, schedule, and credit hours—into a clear result that shows whether "
        "registration succeeded and how my timetable looks.",
    )
    add_para(
        doc,
        "This information helps me as a user because I can immediately confirm that the "
        "correct course was added and plan my weekly schedule. It also helps the "
        "organization (the university) because staff can monitor section capacity, manage "
        "classroom resources, and support academic planning based on accurate registration "
        "results.",
    )

    # ========== Question 4 ==========
    add_heading_custom(doc, "4. Identify a Problem and Suggest an Improvement")
    add_para(
        doc,
        "One weak point I observed was that during peak registration hours the portal "
        "sometimes became slow, and the available-seats number did not refresh quickly. "
        "As a result, I tried to select a section that appeared available, but the system "
        "later rejected the request because the seats had already been taken.",
    )
    add_para(
        doc,
        "Impact: This caused wasted time, frustration, and the risk of missing a preferred "
        "section. Students may need to repeat the search and selection steps several times, "
        "especially when many users access the system at once.",
    )
    add_para(
        doc,
        "Suggested improvement: The system should display a real-time seat counter and show "
        "a clear message such as “Seats just filled—please choose another section” before "
        "final submission. Adding an automatic page refresh every few seconds, or a live "
        "update of seat availability, would reduce failed attempts.",
    )
    add_para(
        doc,
        "System component involved: This improvement mainly involves the Software "
        "(registration application interface and update logic) and the Database (accurate, "
        "up-to-date seat records). The Networks component is also related because faster "
        "and more reliable communication supports timely updates.",
    )

    # ========== Question 5 ==========
    add_heading_custom(
        doc,
        "5. How the System Supports Confidentiality, Integrity, and Availability (CIA Triad)",
    )
    add_para(
        doc,
        "Based on my experience with the university registration system, the CIA triad "
        "appears as follows.",
    )
    add_para(
        doc,
        "Confidentiality: The system protects private academic data by requiring a "
        "username and password before access. Only the authenticated student can view "
        "personal records such as registered courses and grades. This prevents unauthorized "
        "people from seeing sensitive information.",
        first_line_indent=Cm(0),
    )
    add_para(
        doc,
        "Integrity: The system maintains the correctness of registration data by applying "
        "rules before saving changes—for example, checking prerequisites, section capacity, "
        "and schedule conflicts. After a successful registration, the confirmation message "
        "and updated course list show that the stored record matches what I selected. This "
        "helps ensure that student records are accurate and not changed incorrectly.",
    )
    add_para(
        doc,
        "Availability: The portal is expected to be accessible online during the official "
        "registration period so students can register from different locations and devices. "
        "When the system is available, I can complete registration on time. When it becomes "
        "slow or temporarily unavailable during peak hours, availability is weakened, which "
        "shows why continuous access is important for both students and the university.",
    )

    # References & AI disclosure
    add_heading_custom(doc, "References")
    add_para(
        doc,
        "1. King Khalid University student portal / academic registration system "
        "(personal use experience).",
        space_after=0,
    )
    add_para(
        doc,
        "2. Course materials: Introduction to Information Systems – 1300CIS "
        "(system components and CIA triad concepts).",
        space_after=6,
    )

    add_heading_custom(doc, "Use of AI Tools")
    add_para(
        doc,
        "I used an AI tool to improve English wording and to organize the answers according "
        "to the assignment questions. The selected system, process steps, observations, "
        "problem, and examples are based on my own use of the university registration "
        "system. I reviewed and edited the final text before submission.",
    )

    out_path = (
        "/agent/repos/LearningJ/assignments/"
        "StudentID_Assignment_1300CIS_Solution.docx"
    )
    doc.save(out_path)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
