#!/usr/bin/env python3
"""Build a filled assignment PDF: questions + answers in one file."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

OUT = (
    "/agent/repos/LearningJ/assignments/"
    "Assignment_1300CIS_Answers.pdf"
)
ARTIFACT = "/opt/cursor/artifacts/Assignment_1300CIS_Answers.pdf"


def styles():
    base = getSampleStyleSheet()
    s = {}
    s["title"] = ParagraphStyle(
        "title",
        parent=base["Normal"],
        fontName="Times-Bold",
        fontSize=13,
        leading=18,
        alignment=TA_CENTER,
        spaceAfter=2,
    )
    s["center"] = ParagraphStyle(
        "center",
        parent=base["Normal"],
        fontName="Times-Roman",
        fontSize=11,
        leading=15,
        alignment=TA_CENTER,
        spaceAfter=1,
    )
    s["meta"] = ParagraphStyle(
        "meta",
        parent=base["Normal"],
        fontName="Times-Roman",
        fontSize=11,
        leading=16,
        spaceAfter=2,
    )
    s["h"] = ParagraphStyle(
        "h",
        parent=base["Normal"],
        fontName="Times-Bold",
        fontSize=12,
        leading=17,
        spaceBefore=8,
        spaceAfter=4,
    )
    s["body"] = ParagraphStyle(
        "body",
        parent=base["Normal"],
        fontName="Times-Roman",
        fontSize=11,
        leading=16,  # ~1.5 line spacing for size 11
        alignment=TA_JUSTIFY,
        spaceAfter=4,
    )
    s["q"] = ParagraphStyle(
        "q",
        parent=base["Normal"],
        fontName="Times-Italic",
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#333333"),
        spaceAfter=3,
    )
    s["cell"] = ParagraphStyle(
        "cell",
        parent=base["Normal"],
        fontName="Times-Roman",
        fontSize=9,
        leading=12,
        alignment=TA_LEFT,
    )
    s["cellb"] = ParagraphStyle(
        "cellb",
        parent=base["Normal"],
        fontName="Times-Bold",
        fontSize=9,
        leading=12,
        alignment=TA_LEFT,
    )
    s["small"] = ParagraphStyle(
        "small",
        parent=base["Normal"],
        fontName="Times-Roman",
        fontSize=10,
        leading=14,
        spaceAfter=2,
    )
    return s


def main():
    s = styles()
    doc = SimpleDocTemplate(
        OUT,
        pagesize=A4,
        leftMargin=2.5 * cm,
        rightMargin=2.5 * cm,
        topMargin=2.0 * cm,
        bottomMargin=2.0 * cm,
        title="1300CIS Assignment – Answers",
    )
    story = []

    # Header
    story.append(Paragraph("King Khalid University", s["title"]))
    story.append(Paragraph("College of Computer Science", s["center"]))
    story.append(
        Paragraph(
            "Department of Informatics and Computer Systems", s["center"]
        )
    )
    story.append(Spacer(1, 6))
    story.append(
        Paragraph(
            "<b>Course:</b> Introduction to Information Systems – 1300CIS",
            s["meta"],
        )
    )
    story.append(
        Paragraph(
            "<b>Assignment:</b> An Information System in Your Daily Life",
            s["meta"],
        )
    )
    story.append(Paragraph("<b>Name:</b> _______________________________", s["meta"]))
    story.append(Paragraph("<b>Student ID:</b> ___________________________", s["meta"]))
    story.append(Paragraph("<b>Section:</b> _____________________________", s["meta"]))
    story.append(Spacer(1, 4))

    # Q1
    story.append(Paragraph("1. Describe Your Experience", s["h"]))
    story.append(
        Paragraph(
            "The information system I used is the <b>King Khalid University student "
            "portal</b> (university registration / academic system). The specific "
            "process is <b>registering for a course</b>. I used it on "
            "<b>18 November 2026</b> to add one required course to my study plan "
            "before the registration deadline.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "Three steps I completed: (1) I signed in to the student portal with my "
            "university username and password and opened the course registration page. "
            "(2) I searched for the course by its code and selected an available section "
            "that fit my timetable. (3) I confirmed the selection and submitted the "
            "registration request.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "One specific detail I observed was a <b>confirmation message</b> after "
            "submission showing that the course was added successfully, with the course "
            "code, section number, and credit hours. The system also required me to "
            "re-enter my password before final confirmation.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "<i>[Insert screenshots here: registration page, course selection, and "
            "confirmation message. Hide personal information.]</i>",
            s["small"],
        )
    )

    # Q2
    story.append(Paragraph("2. Identify the Information System Components", s["h"]))
    story.append(
        Paragraph(
            "The table below shows each component with an example from the course "
            "registration process and its role.",
            s["body"],
        )
    )

    def cell(text, bold=False):
        return Paragraph(text, s["cellb"] if bold else s["cell"])

    data = [
        [cell("Component", True), cell("Example", True), cell("Role", True)],
        [
            cell("Hardware", True),
            cell("My laptop/phone and university servers"),
            cell(
                "Devices used to access the portal; servers process registration requests."
            ),
        ],
        [
            cell("Software", True),
            cell("Student portal web app and browser"),
            cell(
                "Shows registration screens, checks seats/rules, and sends requests."
            ),
        ],
        [
            cell("Data", True),
            cell("Course code, section, student ID, term"),
            cell(
                "Raw facts needed to assign the correct course and update the timetable."
            ),
        ],
        [
            cell("People", True),
            cell("Students, advisors, administrators"),
            cell(
                "Students register; advisors guide; admins maintain the system."
            ),
        ],
        [
            cell("Networks", True),
            cell("Internet link to university network"),
            cell(
                "Transfers login/registration data and returns confirmation securely."
            ),
        ],
        [
            cell("Database", True),
            cell("Academic DB of courses, seats, records"),
            cell(
                "Stores and updates registered courses and remaining section seats."
            ),
        ],
    ]

    table = Table(data, colWidths=[2.6 * cm, 5.2 * cm, 8.0 * cm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#D9E2F3")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [colors.white, colors.HexColor("#F7F7F7")],
                ),
            ]
        )
    )
    story.append(table)

    # Q3
    story.append(Paragraph("3. Explain How Data Becomes Information", s["h"]))
    story.append(
        Paragraph(
            "Data are raw facts. Information is data that has been processed and "
            "organized so it becomes useful for decisions.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>Two examples of data:</b> (1) the course code I selected (e.g., 1300CIS); "
            "(2) the section number and term. These are only stored facts at entry time.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>One example of information:</b> my updated registered-course list "
            "(registration summary), which combines course name, section, schedule, and "
            "credit hours into a clear result.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "This information helps me confirm the correct course was added and plan my "
            "weekly schedule. It helps the university monitor section capacity and manage "
            "academic resources.",
            s["body"],
        )
    )

    # Q4
    story.append(Paragraph("4. Identify a Problem and Suggest an Improvement", s["h"]))
    story.append(
        Paragraph(
            "<b>Problem:</b> During peak hours the portal was slow, and the available-seats "
            "number did not refresh quickly. I selected a section that looked available, "
            "but the request failed because seats were already taken.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>Impact:</b> Wasted time, frustration, and risk of missing a preferred "
            "section; students may repeat search and selection many times.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>Improvement:</b> Show a real-time seat counter and a clear message such as "
            "“Seats just filled—please choose another section,” with automatic refresh of "
            "availability before final submission.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>Component involved:</b> mainly <b>Software</b> and <b>Database</b> "
            "(also related to <b>Networks</b> for timely updates).",
            s["body"],
        )
    )

    # Q5
    story.append(
        Paragraph(
            "5. Confidentiality, Integrity, and Availability (CIA Triad)",
            s["h"],
        )
    )
    story.append(
        Paragraph(
            "<b>Confidentiality:</b> Access requires a username and password, so only the "
            "authenticated student can view personal records such as registered courses "
            "and grades.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>Integrity:</b> The system checks rules (prerequisites, seat capacity, "
            "schedule conflicts) before saving changes. The confirmation message and "
            "updated course list show that stored data matches what I selected.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>Availability:</b> The portal should stay accessible online during the "
            "registration period from different locations and devices. When it is slow "
            "or temporarily unavailable at peak times, availability is weakened, which "
            "shows why continuous access matters.",
            s["body"],
        )
    )

    # References + AI
    story.append(Paragraph("References", s["h"]))
    story.append(
        Paragraph(
            "1. King Khalid University student portal (personal use experience).<br/>"
            "2. Course materials: Introduction to Information Systems – 1300CIS.",
            s["small"],
        )
    )
    story.append(Paragraph("Use of AI Tools", s["h"]))
    story.append(
        Paragraph(
            "I used an AI tool to improve English wording and organize answers by "
            "question. The system choice, steps, observations, and examples are based on "
            "my own use of the university registration system. I reviewed the final text "
            "before submission.",
            s["body"],
        )
    )

    doc.build(story)

    import shutil
    import os

    os.makedirs("/opt/cursor/artifacts", exist_ok=True)
    shutil.copy2(OUT, ARTIFACT)
    print(f"Saved: {OUT}")
    print(f"Artifact: {ARTIFACT}")


if __name__ == "__main__":
    main()
