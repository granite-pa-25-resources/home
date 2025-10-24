# Student Mobility Matrices - Area 5 Study

This folder contains three mobility matrices showing student flow patterns between boundaries and schools.

## Matrix Files

### **Matrix 1: Basic 10 Schools Only**
**File:** `matrix1_basic_10_schools.csv`

- **Dimensions:** 44 boundary schools (rows) × 10 Area 5 schools (columns)
- **Total Students:** 4,222
- **Description:** Shows count of students FROM each boundary TO each of the 10 schools under study
- **Columns (TO schools):**
  - Cottonwood
  - Crestview
  - Driggs
  - Eastwood
  - Morningside
  - Oakridge
  - Oakwood
  - Penn
  - Rosecrest
  - Upland Terrace

- **Rows (FROM boundaries):** 44 total, including the 10 Area 5 schools plus schools outside the study area (Lincoln, Moss, Woodstock, etc.) and "Out of District"

### **Matrix 2: With Program Breakouts**
**File:** `matrix2_with_programs.csv`

- **Dimensions:** 44 boundary schools (rows) × 14 schools/programs (columns)
- **Total Students:** 4,226
- **Description:** Separates DLI and ALC programs into distinct columns to show program-specific enrollment
- **Columns (TO schools/programs):**
  - Cottonwood
  - Crestview
  - Driggs
  - Eastwood
  - **Morningside_ALC** (144 students)
  - **Morningside_DLI** (267 students)
  - **Morningside_Traditional** (150 students)
  - Oakridge
  - **Oakwood_DLI** (160 students)
  - **Oakwood_Traditional** (373 students)
  - **Penn_DLI** (441 students)
  - **Penn_Traditional** (165 students)
  - Rosecrest
  - Upland Terrace

- **Key Features:**
  - No double counting: Traditional = Total - ALC - DLI for each school
  - Allows analysis of program-specific enrollment patterns
  - Shows which boundaries feed into specialty programs

### **Matrix 3: With Geographic Portions**
**File:** `matrix3_with_geographic_portions.csv`

- **Dimensions:** 47 boundary schools/portions (rows) × 10 Area 5 schools (columns)
- **Total Students:** 4,222
- **Description:** Breaks out geographic sub-portions of school boundaries as separate rows
- **New Boundary Rows:**
  - **Morningside North Portion** (44 students)
    - Subset of Morningside boundary
    - Shows where North Portion students attend
  - **Oakwood Southeast Portion** (1 K-5 student)
    - Subset of Oakwood boundary
    - IN Area 5 study
  - **Oakwood West Portion** (401 students)
    - Subset of Oakwood boundary
    - NOT in Area 5 study

- **Adjusted Main Boundaries:**
  - **MORNINGSIDE** row: Main portion only (260 students) = Original minus North Portion
  - **OAKWOOD** row: Remainder only (7 students) = Original minus Southeast minus West

- **Key Features:**
  - No double counting: Geographic portions subtracted from main boundary totals
  - Sum of portions equals original boundary total
  - Allows analysis of sub-geographic enrollment patterns

## How to Read the Matrices

Each matrix is structured as:
- **Rows:** Boundary school where students LIVE
- **Columns:** School where students ATTEND
- **Values:** Count of students in that FROM→TO pair

**Example:** In Matrix 1, the cell at row "DRIGGS" and column "Morningside" = 38, meaning 38 students who live in the Driggs boundary attend Morningside Elementary.

## Data Sources

All data extracted from official Granite School District mobility tables:
- `C:\PAC_Study\tables\student_mobility2\`
- 17 PDF files with 2024-2025 school year enrollment data
- Data date: February/April 2025 (varies by school)

## Verification

### Matrix 2 Verification (Program Breakouts)
- Morningside Total: 561 students
  - ALC: 144
  - DLI: 267
  - Traditional: 150
  - **Sum: 561 ✓**

- Oakwood Total: 533 students
  - DLI: 160
  - Traditional: 373
  - **Sum: 533 ✓**

- Penn Total: 606 students
  - DLI: 441
  - Traditional: 165
  - **Sum: 606 ✓**

### Matrix 3 Verification (Geographic Portions)
- Morningside Boundary: 304 students
  - Main portion: 260
  - North Portion: 44
  - **Sum: 304 ✓**

- Oakwood Boundary: 409 students
  - Main portion: 7
  - Southeast Portion: 1
  - West Portion: 401
  - **Sum: 409 ✓**

## Notes

1. **Out of District:** Includes students from outside Granite School District boundaries
2. **Alternative 3-A Elementary:** Not one of the 10 Area 5 schools, so students going there are excluded from matrices
3. **Double Counting Eliminated:**
   - Matrix 2: Traditional tracks calculated as (Total - ALC - DLI)
   - Matrix 3: Portions subtracted from main boundary totals
4. **Oakwood West Portion:** NOT in Area 5 study area, but included for completeness
5. **Small Discrepancies:** Minor differences (1-3 students) between original totals and breakouts due to data collection timing or categorization differences

## Generated

- **Date:** October 23, 2025
- **Scripts:**
  - `build_mobility_matrices.py` (Matrix 1)
  - `build_mobility_matrix2_expanded.py` (Matrix 2)
  - `build_mobility_matrix3_geographic.py` (Matrix 3)
