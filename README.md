# Granite School District Area 5 Study — Project Overview

A comprehensive, independent analysis of Granite School District’s Area 5: examining enrollment trends, school mobility, community feedback, and closure proposals. This project brings together official data and interactive visualizations to inform public understanding and discussion about the 2025-2026 decision process.

---

## 📌 Where to Start

- **Home / Project Index:** Open [`index.html`](index.html)  
  This is the single best starting point, with navigation to all major resources and a summary of findings.

- **Enrollment Trends:** See [`enrollment-trends.html`](enrollment-trends.html)  
  Interactive 21-year and 5-year trend visualizations for every Area 5 elementary, with confidence bands and school-by-school breakdowns.

- **Student Mobility Matrices:** View cross-boundary enrollment flows in [`mobility-matrices.html`](mobility-matrices.html)  
  Explore how students move between boundaries and schools; includes three detailed matrix visualizations and summary cards.

- **Morningside Scenario Study:** See [`morningside-study.html`](morningside-study.html)  
  In-depth breakdown of traditional, Dual Immersion, ALC students and the actual number requiring reassignment.

All files work offline. No build required—open in any modern browser.

---

## 🧭 File Structure

```
PAC_Study/
├── index.html                # Home/index: overview, navigation, summary, links
├── enrollment-trends.html    # Interactive school-level and district trends, forecast bands
├── mobility-matrices.html    # Resident/attender matrices + key findings for 2024-25
├── morningside-study.html    # Morningside pathways, DLI, ALC scenario analysis
├── style.css                 # Dark theme and layout styles
├── utils.js                  # Chart/data helpers
├── tables/                   # Official data (PDF/CSV extracts)
└── README.md                 # This file
```

---

## 🚦 Highlights from the Analysis (`index.html`)

### Key Takeaways

- **Enrollment Drop:** Area 5 lost 24% enrollment (2003–2024), but with sharp differences: Penn, Oakwood, and Morningside are nearly full; others have significant excess capacity.
- **High “Choice” Dependence:** Morningside (66%), Penn (51%), and Eastwood (47%) enroll mainly out-of-boundary students—while Crestview, Rosecrest, and Upland retain most neighborhood students.
- **Boundary vs. Total Discrepancy:** Many “under-enrolled” schools are only so by boundary counts; total enrollment is much higher due to district-wide transfers.
- **School Size:** After the Eastwood/Oakridge merger, most schools remain under the 500-student target (466–486).
- **Morningside Scenario:** Only ~75 traditional students require reassignment, not all boundary students.
- **Transparent Process:** District provided public data, interactive tables, and extensive documentation; process rated highly for openness.

See the home page or linked sections for full details, data, and interactive charts.

---

## 🔎 Linked Page Summaries

### `enrollment-trends.html`:  
- 21-year and 5-year enrollment trend charts for each school and Area 5 total
- Compare total vs. in-boundary enrollment side-by-side
- Projected trends to 2029 with confidence bands and capacity benchmarks

### `mobility-matrices.html`:  
- 2024-25 cross-boundary “mobility” data for Area 5 schools/residents
- Interactive matrix: where students who live in each boundary actually attend
- Key stats: 75.8% of Area 5 residents attend their boundary school; 20% of Area 5 school enrollment is from outside the area

### `morningside-study.html`:  
- Deep dive: Morningside's traditional, DLI-French, and ALC programs
- Charts and scenarios for admissions, impact if traditional pathway closes, who actually needs reassignment

---

## 📈 Data Sources

Analysis uses only official GSD and consultant data, including:
- [Area 5 Study Documents & Presentations](https://www.graniteschools.org/planning/2025-population-analysis-studies-amp-data/)
- District enrollment, mobility, and capacity tables
- Public meeting videos and slide decks (Spring-Fall 2025)
- [MGT/Davis Demographics Forecasts](https://drive.google.com/file/d/1yQWOwKZYxyzEkG3-YZqcYyZzqUxBYGzN/view)

Raw PDF/CSV files for each school are stored in `/tables`.

---

## 💡 Top Community Questions

1. **Why is there a gap between boundary counts and actual enrollment?**  
   See `mobility-matrices.html` for matrix details and explanation.

2. **How will the Eastwood/Oakridge merger affect students and staff?**  
   See `index.html` and `enrollment-trends.html` for projections and performance comparison.

3. **How many students must actually move if Morningside’s traditional closes?**  
   See `morningside-study.html` for up-to-date analysis and summary tables.

4. **What will be the impact on remaining schools’ sizes and demographics?**  
   See the enrollment trends and matrix pages for school-by-school breakdowns.

---

## 🤝 Contributing & Feedback

This project is for public use and critical review by the Area 5 community.  
If you spot data issues or have improvement suggestions:

1. Compare with official sources linked above
2. Open a GitHub issue or pull request with supporting links
3. Feedback welcome via `boundaries@graniteschools.org`

---

## ⚠️ Disclaimer

This is an **independent, unofficial analysis** prepared for transparency, educational, and civic engagement purposes.  
Not affiliated with or endorsed by the Granite School District, Board of Education, or the State of Utah.  
All findings reflect only the data publicly released by GSD and the best effort analysis of the authors.

---

_Last updated: January 2025_  
_See each HTML page for the latest data, charts, and discussion._
