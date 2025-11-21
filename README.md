# 🐢 Turtle Practice

*A slow, steady, and deliberate approach to personal leadership and an ordinary day*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

A personal leadership planner based on the **turtle practice** - emphasizing consistent, deliberate progress to a meaningful life through regular, ordinay days using reflection and intentional planning.

🐢 **Turtle Talk**: [gregdyche.github.io/turtle](https://gregdyche.github.io/turtle/turtle_talk_slides.html)

🐢 **Turtle Journal**: [gregdyche.github.io/turtle](https://gregdyche.github.io/turtle)

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
