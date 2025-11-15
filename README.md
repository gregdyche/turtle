# 🐢 Turtle Practice

*A slow, steady, and deliberate approach to personal productivity and goal achievement*

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

A personal productivity planner based on the **turtle practice** - emphasizing consistent, deliberate progress toward meaningful goals through regular reflection and intentional planning.

Unlike typical productivity systems that focus on speed and efficiency, the turtle practice embraces:
- 🎯 **Clear Direction**: Setting an "Eastward Gaze" - your true destination
- 🔄 **Regular Reflection**: Daily, weekly, quarterly, and yearly review cycles
- ⚡ **A-Zone Protection**: Safeguarding time for your most important work
- 🚫 **Intentional Elimination**: Deliberately choosing what NOT to do
- 💚 **Sustainable Pace**: Building habits that last through consistent small actions

## Features

✅ **Five Integrated Page Templates**
- 📅 **Yearly Outlook**: Set your direction and annual commitments
- 🔍 **Quarterly Review**: DICE framework assessment and course correction
- 🗓️ **Monthly Preview**: Calendar grid and major milestone planning
- 📋 **Weekly Planning**: Specific intentions and time blocking
- 📝 **Daily Page**: Morning start, midday check-in, evening reflection

✅ **Multiple Format Options**
- **HTML Version**: Type directly in browser, print as needed
- **Professional PDF Output**: Clean, printable design for physical planning
- **GitHub Pages Hosting**: Access from anywhere via web browser
- **Turtle-themed styling** with consistent design across all formats

✅ **Proven Frameworks**
- **Turtle Assessment**: Direction, Consistency, Balance, Energy evaluation
- **A/B/C Zone Prioritization**: Clear task categorization
- **Pay Yourself First**: Protected time for personal growth projects

## Installation & Usage

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation
1. Clone this repository:
```bash
git clone https://github.com/gregdyche/turtle.git
cd turtle
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Use the Planner

**Option 1: HTML Version (Recommended)**
Access the web-based planner directly in your browser:
- Visit: **https://gregdyche.github.io/turtle/**
- Click "🐢 View Turtle Planner" to access the planner
- Type directly into the forms and print as needed
- Perfect for immediate use and printing

**Option 2: Download PDF Version**
- **Direct Download**: Click "📄 Download PDF Planner" on the website
- **GitHub Release**: Download from the latest release
- **Auto-Generated**: PDF is automatically updated when code changes

**Option 3: Generate PDF Yourself**
```bash
python turtleplanner.py
```

This creates `turtle_diaries_planner.pdf` with all five page templates ready for printing.

**GitHub Pages Access**
When hosted on GitHub Pages, access the planner at:
`https://gregdyche.github.io/turtle/`

### Recommended Printing
- **1x** Yearly Outlook (print once per year)
- **4x** Quarterly Review (one per quarter)
- **12x** Monthly Preview (one per month)
- **52x** Weekly Planning (one per week)
- **365x** Daily Pages (or print weekly batches)

## The Five Page Templates

### 🎯 Yearly Outlook
Set your annual direction with four key sections:
- **Eastward Gaze**: Your single most important destination this year
- **The Must-Be**: Personal growth commitment
- **Pay Yourself First**: Daily personal project commitment
- **The Non-Agenda**: Three specific things you'll stop doing

### 🔍 Quarterly Review
Assess your progress using the turtle practice framework:
- **Direction**: Are you moving steadily toward your Eastward Gaze?
- **Consistency**: Are you maintaining sustainable progress and working habits?
- **Balance**: Are you protecting A-Zone time while maintaining relationships?
- **Energy**: Do you feel energized by your work without burning out?

### 🗓️ Monthly Preview
Plan your month strategically:
- **Calendar Grid**: Visual month layout for key dates
- **Monthly Big Rocks**: Three major milestones to achieve

### 📋 Weekly Planning & Reflection
Bridge the gap between strategy and daily action:
- **Weekly Intentions**: Five specific, measurable weekly actions
- **A-Zone Protection**: Time blocking for priority work
- **Learning & Adjustment**: Weekly process improvements

### 📝 Daily Page
Your daily navigation tool:
- **Morning Start**: First deliberate action
- **A-Zone Block**: Protected time for major work
- **Midday Examen**: Quick check-in (on-track? having fun?)
- **B/C-Zone Tasks**: Secondary task checklist
- **Evening Reflection**: Acts of love and tomorrow's preparation

## The Turtle Methodology

### Core Principles

1. **🧭 Eastward Direction**: Like migrating turtles, maintain clear directional movement toward your true destination
2. **🏃‍♂️ A-Zone First**: Protect time for your most important work before everything else
3. **🔄 Regular Reflection**: Build in systematic review cycles to stay on course
4. **⚖️ Intentional Balance**: Deliberately choose what to pursue and what to eliminate
5. **🌱 Sustainable Growth**: Focus on consistency over intensity for lasting change

### Zone System
- **A-Zone**: Your most important work that moves you toward your Eastward Gaze
- **B-Zone**: Important but secondary tasks
- **C-Zone**: Low-priority activities that can wait or be eliminated

## Technical Details

### Dependencies
- `reportlab`: PDF generation and layout
- Python 3.x standard libraries

### File Structure
```
turtletalk/
├── README.md                      # This file
├── index.html                     # Landing page and entry point
├── turtle-planner.html            # Interactive web-based planner
├── requirements.txt               # Python dependencies
├── turtleplanner.py              # PDF planner generation script
├── CLAUDE.md                     # Development memory/notes
├── Turtle talk Greg Dyche.pptx   # Presentation materials
└── turtle_diaries_planner.pdf    # Generated planner output
```

### Design System
- **Primary Color**: Turtle Green (#16a085)
- **Typography**: Helvetica-based hierarchy
- **Layout**: Responsive design for web, professional print layout for PDF
- **Styling**: Clean, minimalist design focused on functionality
- **Interactive Elements**: Form inputs, checkboxes, and date fields in HTML version

## Contributing

Contributions are welcome! Here are some ways you can help:

### Current Enhancement Ideas
- [ ] Add command-line arguments for custom dates/years
- [ ] Create individual page type generators
- [ ] Add configuration file for custom colors and styling
- [ ] Implement digital form fields for PDF completion
- [ ] Create a web interface for planner generation
- [ ] Add multiple language support

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## Philosophy & Inspiration

The turtle practice draws inspiration from the deliberate, purposeful movement of sea turtles during migration. Despite their slow pace, turtles navigate thousands of miles with remarkable precision to reach their destinations.

Similarly, this planner system encourages:
- **Deliberate movement** over frantic activity
- **Clear direction** over busy work
- **Consistent progress** over sporadic bursts
- **Regular course correction** over hoping for the best

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created by Greg Dyche

---

*Remember: The turtle wins the race not through speed, but through persistence and direction. 🐢*