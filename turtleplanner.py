"""
Turtle Diaries Planner Generator
Generates a PDF planner with 5 page templates
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas

# Colors
TURTLE_GREEN = HexColor('#16a085')
DARK_GRAY = HexColor('#2c3e50')
LIGHT_GRAY = HexColor('#ecf0f1')
BORDER_GRAY = HexColor('#bdc3c7')

def create_planner(filename='turtle_diaries_planner.pdf'):
    """Create the complete planner PDF"""
    
    # Create the PDF
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )
    
    # Container for all elements
    story = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=TURTLE_GREEN,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    section_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=DARK_GRAY,
        spaceAfter=10,
        spaceBefore=15,
        fontName='Helvetica-Bold',
        leftIndent=10,
        borderPadding=5,
        borderColor=TURTLE_GREEN,
        borderWidth=0,
        leftBorderWidth=4
    )
    
    prompt_style = ParagraphStyle(
        'Prompt',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#555555'),
        spaceAfter=10,
        fontName='Times-Italic',
        backColor=HexColor('#f8f9fa'),
        borderPadding=8
    )
    
    # PAGE 1: YEARLY OUTLOOK
    story.append(Paragraph("🐢 THE TURTLE DIARIES: YEARLY OUTLOOK", title_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("MY EASTWARD GAZE: YEARLY DIRECTION", section_style))
    story.append(Paragraph(
        "The Destination: What is the single most important thing I want to be remembered for this year? (The ship's one destination.)",
        prompt_style
    ))
    story.append(Spacer(1, 1.5*inch))
    
    story.append(Paragraph("THE MUST-BE", section_style))
    story.append(Paragraph(
        "What is one thing I can be that I must be this year (personal growth, skill mastery, etc.)?",
        prompt_style
    ))
    story.append(Spacer(1, 0.8*inch))
    
    story.append(Paragraph("PAY YOURSELF FIRST (A-ZONE COMMITMENT)", section_style))
    story.append(Paragraph(
        "What is the most important personal project (writing, side hustle, health) that I will schedule time for every single day?",
        prompt_style
    ))
    story.append(Spacer(1, 0.8*inch))
    
    story.append(Paragraph("THE NON-AGENDA (WHAT I WILL NOT DO)", section_style))
    story.append(Paragraph(
        "What are three specific things I am going to stop doing to free up time and energy for the Turtle's path?",
        prompt_style
    ))
    
    # Checklist items
    for i in range(3):
        checklist_data = [['☐', '_' * 80]]
        checklist_table = Table(checklist_data, colWidths=[0.3*inch, 6.5*inch])
        checklist_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONTNAME', (0, 0), (0, 0), 'Helvetica'),
            ('FONTSIZE', (0, 0), (0, 0), 16),
        ]))
        story.append(checklist_table)
        story.append(Spacer(1, 0.15*inch))
    
    story.append(PageBreak())
    
    # PAGE 2: QUARTERLY REVIEW
    story.append(Paragraph("🐢 QUARTERLY REVIEW", title_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("QUARTERLY DICE CHECK-IN (EARLY ALARM)", section_style))
    story.append(Paragraph(
        "Review the past 90 days. Rate your primary project/goal on a scale of 1-5 (1=Excellent, 5=Alarm sounding):",
        prompt_style
    ))
    
    # DICE Table
    dice_data = [
        ['Factor', 'Rating (1-5)', 'Notes'],
        ['Duration\nIs the current pace sustainable?', '', ''],
        ['Integrity\nDid I adhere to the plan/routine?', '', ''],
        ['Commitment\nC1: My own belief. C2: Others\' support.', '', ''],
        ['Effort\nIs the required effort burning me out?', '', '']
    ]
    
    dice_table = Table(dice_data, colWidths=[2.2*inch, 0.8*inch, 3.5*inch])
    dice_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), LIGHT_GRAY),
        ('TEXTCOLOR', (0, 0), (-1, -1), DARK_GRAY),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, BORDER_GRAY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(dice_table)
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph("THE SCORECARD", section_style))
    story.append(Paragraph(
        "How did I treat others this quarter? How did I live up to my values in my key relationships?",
        prompt_style
    ))
    story.append(Spacer(1, 1.2*inch))
    
    story.append(Paragraph("RE-TUNING THE COMPASS", section_style))
    story.append(Paragraph(
        "Based on the review, what is one minor adjustment I will make to my Yearly Direction or daily routine for the next quarter?",
        prompt_style
    ))
    story.append(Spacer(1, 0.8*inch))
    
    story.append(PageBreak())
    
    # PAGE 3: MONTHLY PREVIEW
    story.append(Paragraph("🐢 MONTHLY PREVIEW", title_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("MONTHLY CALENDAR GRID", section_style))
    story.append(Paragraph("Month: _____________ Year: _______", ParagraphStyle(
        'MonthYear',
        parent=styles['Normal'],
        fontSize=11,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )))
    story.append(Spacer(1, 0.15*inch))
    
    # Calendar grid
    calendar_headers = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    calendar_data = [calendar_headers]
    for week in range(5):
        calendar_data.append([''] * 7)
    
    calendar_table = Table(calendar_data, colWidths=[0.95*inch] * 7, rowHeights=[0.3*inch] + [0.6*inch] * 5)
    calendar_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TURTLE_GREEN),
        ('TEXTCOLOR', (0, 0), (-1, 0), HexColor('#ffffff')),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, BORDER_GRAY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(calendar_table)
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph("MONTHLY BIG ROCKS", section_style))
    story.append(Paragraph(
        "List 3 major projects or milestones I need to achieve this month to stay on the Yearly Path.",
        prompt_style
    ))
    
    for i in range(3):
        checklist_data = [['☐', '_' * 80]]
        checklist_table = Table(checklist_data, colWidths=[0.3*inch, 6.5*inch])
        checklist_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONTNAME', (0, 0), (0, 0), 'Helvetica'),
            ('FONTSIZE', (0, 0), (0, 0), 16),
        ]))
        story.append(checklist_table)
        story.append(Spacer(1, 0.15*inch))
    
    story.append(PageBreak())
    
    # PAGE 4: WEEKLY PLANNING & REFLECTION
    story.append(Paragraph("🐢 WEEKLY PLANNING & REFLECTION", title_style))
    story.append(Paragraph("Week of: _____________ to _____________", ParagraphStyle(
        'WeekOf',
        parent=styles['Normal'],
        fontSize=11,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("WEEKLY INTENTIONS (FORWARD-LOOKING)", section_style))
    story.append(Paragraph(
        "Call Your Shots: List 5 specific, small actions or tasks I intend to complete this week to move Eastward. (Must be measurable.)",
        prompt_style
    ))
    
    for i in range(5):
        intention_data = [
            ['☐', '_' * 70],
            ['', 'Status: ☐ DONE  ☐ MISSED | Reason if missed: ☐ WON\'T DO  ☐ CAN\'T DO']
        ]
        intention_table = Table(intention_data, colWidths=[0.3*inch, 6.2*inch])
        intention_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONTNAME', (0, 0), (0, 0), 'Helvetica'),
            ('FONTSIZE', (0, 0), (0, 0), 16),
            ('FONTSIZE', (1, 1), (1, 1), 8),
            ('TEXTCOLOR', (1, 1), (1, 1), HexColor('#7f8c8d')),
        ]))
        story.append(intention_table)
        story.append(Spacer(1, 0.1*inch))
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("A-ZONE PROTECTION: BLOCK TIME", section_style))
    story.append(Paragraph(
        "Block out a specific time slot on each day this week for my Pay Yourself First project.",
        prompt_style
    ))
    story.append(Spacer(1, 0.6*inch))
    
    story.append(Paragraph("WEEKLY LEARNING & ADJUSTMENT", section_style))
    story.append(Paragraph(
        "What is the one small adjustment I will make to my routine next week to better align my intentions with my actions?",
        prompt_style
    ))
    story.append(Spacer(1, 0.6*inch))
    
    story.append(PageBreak())
    
    # PAGE 5: DAILY PAGE
    story.append(Paragraph("🐢 DAILY PAGE", title_style))
    story.append(Paragraph("DAY: _____________ DATE: _____________", ParagraphStyle(
        'DayDate',
        parent=styles['Normal'],
        fontSize=14,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )))
    story.append(Spacer(1, 0.25*inch))
    
    story.append(Paragraph("MORNING (START HERE)", section_style))
    story.append(Paragraph(
        "What is the single, deliberate step I will take first thing this morning?",
        prompt_style
    ))
    story.append(Spacer(1, 0.6*inch))
    
    story.append(Paragraph("A-ZONE SCHEDULED BLOCK", section_style))
    story.append(Paragraph(
        "The one major task scheduled for the A-Zone",
        prompt_style
    ))
    story.append(Spacer(1, 0.6*inch))
    
    story.append(Paragraph("MID-DAY EXAMEN (NOON CHECK-IN)", section_style))
    story.append(Paragraph(
        "Check-In: 1. Am I on-track? 2. Am I having fun (getting energy from my work)?",
        prompt_style
    ))
    story.append(Paragraph("On-track: ☐ Yes  ☐ No<br/>Having fun: ☐ Yes  ☐ No", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("B-ZONE/C-ZONE TASKS", section_style))
    for i in range(4):
        checklist_data = [['☐', '_' * 80]]
        checklist_table = Table(checklist_data, colWidths=[0.3*inch, 6.5*inch])
        checklist_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONTNAME', (0, 0), (0, 0), 'Helvetica'),
            ('FONTSIZE', (0, 0), (0, 0), 16),
        ]))
        story.append(checklist_table)
        story.append(Spacer(1, 0.1*inch))
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("EVENING REFLECTION", section_style))
    story.append(Paragraph(
        "1. What small act of love/sacrifice did I practice today? 2. What can I prep today to make tomorrow a better day?",
        prompt_style
    ))
    story.append(Spacer(1, 0.6*inch))
    
    story.append(Paragraph("NOTES & SCRATCHPAD", section_style))
    story.append(Spacer(1, 1.2*inch))
    
    # Build the PDF
    doc.build(story)
    print(f"✅ Planner created successfully: {filename}")
    print(f"📄 The file contains all 5 page templates")
    print(f"🖨️  Print multiple copies as needed:")
    print(f"   • 1x Yearly Outlook")
    print(f"   • 4x Quarterly Review")
    print(f"   • 12x Monthly Preview")
    print(f"   • 52x Weekly Planning")
    print(f"   • 365x Daily Pages (or print weekly)")


if __name__ == '__main__':
    # Generate the planner
    create_planner()
