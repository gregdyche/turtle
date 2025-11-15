# TurtleTalk Project Memory

## Project Overview
**TurtleTalk** is a personal productivity planner system based on "turtle methodology" - a slow, steady, and deliberate approach to goal achievement and personal development. The project generates a comprehensive PDF planner with five distinct page templates.

## Project Structure
```
turtletalk/
├── CLAUDE.md                      # This memory file
├── requirements.txt                # Python dependencies
├── turtleplanner.py               # Main planner generation script
├── Turtle talk  Greg Dyche.pptx   # Presentation file
└── turtle_diaries_planner.pdf     # Generated planner output
```

## Core Files

### `turtleplanner.py` (Main Script)
- **Purpose**: Generates a 5-page PDF planner using ReportLab
- **Dependencies**: ReportLab (reportlab library)
- **Output**: `turtle_diaries_planner.pdf`
- **Key Features**:
  - Custom turtle-themed styling with green color scheme
  - Five distinct page templates for different time horizons
  - Professional PDF layout with tables, checklists, and structured sections

### `requirements.txt`
- Contains: `google-genai>=0.1.0` (though not used in main script)
- Missing: `reportlab` dependency (should be added)

## The Five Page Templates

### 1. Yearly Outlook (`turtleplanner.py:75-118`)
- **Eastward Gaze**: Single most important yearly goal
- **The Must-Be**: Personal growth commitment
- **Pay Yourself First**: Daily personal project commitment
- **The Non-Agenda**: Three things to stop doing

### 2. Quarterly Review (`turtleplanner.py:120-168`)
- **DICE Framework**: Duration, Integrity, Commitment, Effort ratings (1-5 scale)
- **The Scorecard**: Relationship and values reflection
- **Re-tuning the Compass**: Quarterly adjustments

### 3. Monthly Preview (`turtleplanner.py:170-220`)
- **Calendar Grid**: Visual month layout
- **Monthly Big Rocks**: Three major monthly milestones

### 4. Weekly Planning & Reflection (`turtleplanner.py:222-270`)
- **Weekly Intentions**: Five specific weekly actions
- **A-Zone Protection**: Time blocking for priorities
- **Learning & Adjustment**: Weekly process improvements

### 5. Daily Page (`turtleplanner.py:272-327`)
- **Morning Start**: First deliberate action
- **A-Zone Block**: Major scheduled task
- **Mid-day Examen**: Noon check-in (on-track/having fun)
- **B/C-Zone Tasks**: Secondary task checklist
- **Evening Reflection**: Love/sacrifice acts and tomorrow prep
- **Notes & Scratchpad**: Free-form space

## Design System (`turtleplanner.py:14-73`)

### Color Palette
- **TURTLE_GREEN**: `#16a085` (primary brand color)
- **DARK_GRAY**: `#2c3e50` (text)
- **LIGHT_GRAY**: `#ecf0f1` (backgrounds)
- **BORDER_GRAY**: `#bdc3c7` (borders)

### Typography Styles
- **Title Style**: 20pt Helvetica-Bold, turtle green, centered
- **Section Style**: 13pt Helvetica-Bold, dark gray, left border accent
- **Prompt Style**: 10pt Times-Italic, background highlight

## Turtle Methodology Philosophy
Based on the code content and structure, the "turtle methodology" emphasizes:

1. **Slow & Steady Progress**: Focus on consistent daily actions
2. **Eastward Direction**: Clear directional goals (like turtle migration)
3. **A-Zone Prioritization**: Protecting time for most important work
4. **Regular Reflection**: Daily, weekly, quarterly, and yearly reviews
5. **Intentional Living**: Deliberate choices about what to do and not do

## Technical Notes

### Dependencies to Install
```bash
pip install reportlab
```

### Usage
```bash
python turtleplanner.py
```

### File Output
- Generates `turtle_diaries_planner.pdf` in current directory
- Recommended printing quantities displayed in terminal output

## Development Notes
- Code is well-structured with clear separation of page templates
- Uses ReportLab's Platypus for document layout
- All styling is centralized and consistent
- No obvious security concerns - generates static PDF content only

## Potential Enhancements
- Add date/year parameters for customized planners
- Create CLI interface for different template combinations
- Add configuration file for custom colors/styles
- Generate individual page types separately
- Add digital form fields for PDF completion

## Git Status
- Current branch: `main`
- Repository is clean with recent commits including initial setup
- Ready for collaborative development