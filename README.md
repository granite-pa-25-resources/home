# Granite School District Area 5 Study - Independent Analysis

An independent, data-driven analysis of the Granite School District's Area 5 Population Analysis Study and proposed school closures for the 2025-2026 school year.

## 📊 Live Analysis

Open `granite_district_area5_analysis_dark.html` in any modern web browser to view the complete interactive analysis.

## 🎯 Key Findings

### Critical Methodological Flaw
The study uses **in-boundary resident population forecasts** to justify closures, but schools actually operate on **total enrollment** (which includes choice-based, out-of-boundary students). This creates a 50-80% discrepancy at several schools:

- **Morningside:** 309 boundary residents vs 561 total students (+82%)
- **Penn:** 344 boundary residents vs 606 total students (+76%)
- **Eastwood:** 173 boundary residents vs 267 total students (+54%)

### Goal Misalignment
The district's stated goal is to achieve **500-550 students per school**. The PAC recommendations result in only **466 students per school** - falling short by 34-84 students.

### Transparency Excellence
The district earns an **A+** for transparency:
- 11+ video recordings of public meetings on YouTube
- Individual student mobility data tables for each school
- 40-member community subcommittee
- AI-summarized community feedback
- Multiple feedback mechanisms

### Overall Assessment: **B-** (Good Process, Flawed Methodology)

## 📁 Project Structure

```
PAC_Study/
├── granite_district_area5_analysis_dark.html  # Main analysis (dark theme with charts)
├── granite_district_area5_analysis.html       # Original analysis (light theme)
├── README.md                                   # This file
├── LICENSE                                     # MIT License
└── .gitignore                                  # Git ignore rules
```

## 🔧 Features

### Interactive Visualizations (Plotly.js)
- District-wide enrollment trends (2004-2029)
- In-boundary vs total enrollment comparison
- Facility Condition Index (FCI) analysis
- Normalized enrollment trends (2021-2025)
- School-by-school performance comparison

### Comprehensive Analysis Sections
1. **Executive Summary** - Goal alignment analysis
2. **Enrollment Trends** - District-wide and school-specific data
3. **Schools Under Review** - Detailed profiles of 10 elementary schools
4. **Video Documentation** - Links to all public meetings
5. **Study Methodology** - How the study was conducted
6. **Data Sources** - MGT forecasts, Davis Demographics, district data
7. **Critical Flaws** - In-boundary vs total enrollment discrepancy
8. **Financial Impact** - Cost-benefit considerations
9. **PAC Recommendations** - Assessment of proposed closures
10. **Alternative Scenarios** - Options not considered
11. **Unanswered Questions** - Critical gaps in the analysis
12. **Community Input** - Feedback mechanisms and responses
13. **Final Assessment** - Graded evaluation across 8 criteria
14. **Recommendations** - Suggestions for improvement
15. **Conclusion** - Summary and action items

## 🎨 Design

- **Dark Theme:** Professional color scheme optimized for readability
- **Responsive:** Works on desktop, tablet, and mobile devices
- **Accessible:** High contrast, clear typography, semantic HTML
- **Interactive Charts:** Hover tooltips, zoom, pan capabilities
- **Navigation:** Hamburger menu with smooth scroll to sections

## 📈 Data Sources

All data sourced from official Granite School District publications:
- [2025 Population Analysis Study](https://www.graniteschools.org/planning/2025-population-analysis-studies-amp-data/)
- [MGT Population Forecast 2024-2030](https://drive.google.com/file/d/1yQWOwKZYxyzEkG3-YZqcYyZzqUxBYGzN/view)
- [Student Mobility and Population Tables](https://www.graniteschools.org/planning/student-mobility-and-population-tables/)
- Public meeting presentations (March-October 2025)

## 🚀 How to Use

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd PAC_Study
   ```

2. **Open the analysis:**
   - Simply open `granite_district_area5_analysis_dark.html` in your web browser
   - No build process or dependencies required
   - Works completely offline

3. **Navigate:**
   - Use the hamburger menu (☰) in the top-left corner
   - Click any section to jump directly to it
   - Scroll through for linear reading

## 📊 Key Visualizations

### 1. Normalized Total Enrollment (2021 = 100%)
Shows how actual enrollment changed 2021-2025:
- Penn grew to 106% (gaining students)
- Oakridge fell to 73% (losing students rapidly)
- Morningside stable at 99-100%

### 2. Normalized In-Boundary Population (2021 = 100%)
Shows how boundary populations changed:
- Cottonwood fell to 80% (steepest decline)
- Most schools declining 10-20%
- Eastwood had volatile swings

### 3. Total vs Boundary Comparison
Overlays both metrics for key schools, revealing the massive gap between what the district measures (boundary) and what matters (total enrollment).

## ❓ Questions for Public Hearings

Key questions community members should ask (Nov 18, Dec 2 at 7:00 PM):

1. Why is there such a large gap between in-boundary population and total enrollment? Where are out-of-boundary students coming from?

2. What analysis predicts whether Eastwood's 94 out-of-boundary students will transfer to Oakridge or leave the district?

3. Morningside has 561 students—why is it treated as underenrolled?

4. Why not close Cottonwood (steepest decline -42%) instead of Eastwood?

5. How much does closing one school save annually? What are one-time closure costs?

## 🤝 Contributing

This is an independent analysis for educational and civic engagement purposes. If you find errors in the data or analysis:

1. Verify against [official district sources](https://www.graniteschools.org/planning/2025-population-analysis-studies-amp-data/)
2. Open an issue describing the discrepancy
3. Include links to official source documents

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This is an **independent analysis** and is not affiliated with, endorsed by, or representative of the Granite School District, the Utah State Board of Education, or any official governmental entity.

All data is sourced from publicly available documents published by the Granite School District. Analysis, conclusions, and recommendations are those of the author(s) and are provided for educational and civic engagement purposes.

## 🔗 Official Resources

- **District Website:** [graniteschools.org/planning](https://www.graniteschools.org/planning/)
- **Study Data:** [2025 Population Analysis](https://www.graniteschools.org/planning/2025-population-analysis-studies-amp-data/)
- **Feedback Form:** [forms.gle/7X1KgLqTVowhvKFf7](https://forms.gle/7X1KgLqTVowhvKFf7)
- **Contact:** boundaries@graniteschools.org | (385) 646-4123

## 📅 Timeline

- **September-October 2025:** Public meetings and community feedback
- **November 18, 2025:** First public hearing (7:00 PM)
- **December 2, 2025:** Second public hearing (7:00 PM)
- **December 2025:** Board of Education final decision
- **Fall 2026:** Implementation (if approved)

---

**Last Updated:** January 2025
**Analysis Version:** 2.0 (Dark Theme with Plotly Charts)
