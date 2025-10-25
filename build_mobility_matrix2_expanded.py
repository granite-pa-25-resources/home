"""
Build Matrix 2 with program breakouts:
- Morningside ALC (separate column)
- Morningside DLI (separate column)
- Morningside Traditional (Total - ALC - DLI)
- Oakwood DLI (separate column)
- Oakwood Traditional (Total - DLI)
- Penn DLI (separate column)
- Penn Traditional (Total - DLI)
- All other schools remain as single columns
"""

import pandas as pd
import numpy as np
from collections import defaultdict

# Start with Matrix 1 data (basic schools)
matrix2_data = {}

# First, let's extract the specialty program data

# ==============================================================================
# MORNINGSIDE ALC - Students attending Morningside ALC by boundary
# ==============================================================================
morningside_alc = {
    'COTTONWOOD': 14,
    'CRESTVIEW': 9,
    'DRIGGS': 9,
    'EASTWOOD': 5,
    'LINCOLN': 1,
    'MORNINGSIDE': 24,
    'MOSS': 1,
    'OAKRIDGE': 17,
    'OAKWOOD': 3,
    'OLENE WALKER': 1,
    'Out of District': 14,
    'PENN': 9,
    'ROSECREST': 13,
    'STANSBURY': 1,
    'UPLAND TERRACE': 20,
    'WILSON': 1,
    'WOODSTOCK': 2
}

# ==============================================================================
# MORNINGSIDE DLI - Students attending Morningside DLI by boundary
# ==============================================================================
morningside_dli = {
    'ACADEMY PARK': 2,
    'COTTONWOOD': 2,
    'CRESTVIEW': 9,
    'DIAMOND RIDGE': 1,
    'DRIGGS': 22,
    'EASTWOOD': 4,
    'FREMONT': 1,
    'LINCOLN': 7,
    'MORNINGSIDE': 86,
    'MOSS': 8,
    'OAKRIDGE': 14,
    'OAKWOOD': 6,
    'Out of District': 56,
    'PENN': 1,
    'ROSECREST': 12,
    'SILVER HILLS': 1,
    'SOUTH KEARNS': 1,
    'TAYLORSVILLE': 3,
    'TRUMAN': 1,
    'UPLAND TERRACE': 11,
    'VISTA': 1,
    'WILSON': 7,
    'WOODSTOCK': 11
}

# ==============================================================================
# OAKWOOD DLI - Students attending Oakwood DLI by boundary
# ==============================================================================
oakwood_dli = {
    'ARCADIA': 1,
    'ARMSTRONG': 1,
    'COTTONWOOD': 1,
    'CRESTVIEW': 3,
    'DRIGGS': 2,
    'FREMONT': 2,
    'LINCOLN': 1,
    'MOSS': 15,
    'OAKRIDGE': 2,
    'OAKWOOD': 70,
    'OLENE WALKER': 1,
    'ORCHARD': 1,
    'Out of District': 32,
    'PENN': 3,
    'PLYMOUTH': 1,
    'ROSECREST': 2,
    'SMITH': 3,
    'TAYLORSVILLE': 1,
    'TRUMAN': 1,
    'VISTA': 1,
    'WILSON': 6,
    'WOODSTOCK': 10
}

# ==============================================================================
# PENN DLI - Students attending Penn DLI by boundary
# ==============================================================================
penn_dli = {
    'ARCADIA': 2,
    'BACCHUS': 1,
    'COTTONWOOD': 7,
    'CRESTVIEW': 18,
    'DRIGGS': 9,
    'EASTWOOD': 2,
    'FREMONT': 2,
    'FROST': 1,
    'GRANGER': 1,
    'LINCOLN': 47,
    'MORNINGSIDE': 6,
    'MOSS': 38,
    'OAKRIDGE': 1,
    'OAKWOOD': 8,
    'OLENE WALKER': 11,
    'Out of District': 44,
    'PENN': 181,
    'ROSECREST': 30,
    'STANSBURY': 1,
    'TRUMAN': 2,
    'UPLAND TERRACE': 10,
    'WEST VALLEY': 1,
    'WILSON': 12,
    'WOODSTOCK': 6
}

# ==============================================================================
# Now calculate TRADITIONAL tracks by subtracting specialty programs from totals
# ==============================================================================

# Import Matrix 1 as starting point (now includes ALL schools)
import pandas as pd
matrix1 = pd.read_csv('C:/PAC_Study/tables/student_mobility2_matrices/matrix1_basic_10_schools.csv', index_col=0)

# Extract Morningside Total from Matrix 1 CSV
morningside_total = {}
if 'Morningside' in matrix1.columns:
    for boundary in matrix1.index:
        count = matrix1.loc[boundary, 'Morningside']
        if count > 0:
            morningside_total[boundary] = int(count)

# Calculate Morningside Traditional
morningside_trad = {}
all_boundaries = set(list(morningside_total.keys()) + list(morningside_alc.keys()) + list(morningside_dli.keys()))
for boundary in all_boundaries:
    total = morningside_total.get(boundary, 0)
    alc = morningside_alc.get(boundary, 0)
    dli = morningside_dli.get(boundary, 0)
    trad = total - alc - dli
    if trad > 0:
        morningside_trad[boundary] = trad

# Extract Oakwood Total from Matrix 1 CSV
oakwood_total = {}
if 'Oakwood' in matrix1.columns:
    for boundary in matrix1.index:
        count = matrix1.loc[boundary, 'Oakwood']
        if count > 0:
            oakwood_total[boundary] = int(count)

# Calculate Oakwood Traditional
oakwood_trad = {}
all_boundaries_oakwood = set(list(oakwood_total.keys()) + list(oakwood_dli.keys()))
for boundary in all_boundaries_oakwood:
    total = oakwood_total.get(boundary, 0)
    dli = oakwood_dli.get(boundary, 0)
    trad = total - dli
    if trad > 0:
        oakwood_trad[boundary] = trad

# Extract Penn Total from Matrix 1 CSV
penn_total = {}
if 'Penn' in matrix1.columns:
    for boundary in matrix1.index:
        count = matrix1.loc[boundary, 'Penn']
        if count > 0:
            penn_total[boundary] = int(count)

# Calculate Penn Traditional
penn_trad = {}
all_boundaries_penn = set(list(penn_total.keys()) + list(penn_dli.keys()))
for boundary in all_boundaries_penn:
    total = penn_total.get(boundary, 0)
    dli = penn_dli.get(boundary, 0)
    trad = total - dli
    if trad > 0:
        penn_trad[boundary] = trad

# ==============================================================================
# Build Matrix 2 with all school columns (including program breakouts)
# ==============================================================================

# Create new matrix with additional columns for programs
# Matrix 2 will have ALL schools from Matrix 1, but with Morningside, Oakwood, and Penn split into program-specific columns

matrix2 = matrix1.copy()

# Drop the combined columns we're splitting
if 'Morningside' in matrix2.columns:
    matrix2 = matrix2.drop(columns=['Morningside'])
if 'Oakwood' in matrix2.columns:
    matrix2 = matrix2.drop(columns=['Oakwood'])
if 'Penn' in matrix2.columns:
    matrix2 = matrix2.drop(columns=['Penn'])

# Add Morningside breakout columns
matrix2['Morningside_ALC'] = 0
matrix2['Morningside_DLI'] = 0
matrix2['Morningside_Traditional'] = 0

for boundary, count in morningside_alc.items():
    if boundary in matrix2.index:
        matrix2.loc[boundary, 'Morningside_ALC'] = count

for boundary, count in morningside_dli.items():
    if boundary in matrix2.index:
        matrix2.loc[boundary, 'Morningside_DLI'] = count

for boundary, count in morningside_trad.items():
    if boundary in matrix2.index:
        matrix2.loc[boundary, 'Morningside_Traditional'] = count

# Add Oakwood breakout columns
matrix2['Oakwood_DLI'] = 0
matrix2['Oakwood_Traditional'] = 0

for boundary, count in oakwood_dli.items():
    if boundary in matrix2.index:
        matrix2.loc[boundary, 'Oakwood_DLI'] = count

for boundary, count in oakwood_trad.items():
    if boundary in matrix2.index:
        matrix2.loc[boundary, 'Oakwood_Traditional'] = count

# Add Penn breakout columns
matrix2['Penn_DLI'] = 0
matrix2['Penn_Traditional'] = 0

for boundary, count in penn_dli.items():
    if boundary in matrix2.index:
        matrix2.loc[boundary, 'Penn_DLI'] = count

for boundary, count in penn_trad.items():
    if boundary in matrix2.index:
        matrix2.loc[boundary, 'Penn_Traditional'] = count

# Reorder columns: Area 5 schools first (with program breakouts), then other schools alphabetically
area5_schools = [
    'Cottonwood', 'Crestview', 'Driggs', 'Eastwood',
    'Morningside_ALC', 'Morningside_DLI', 'Morningside_Traditional',
    'Oakridge',
    'Oakwood_DLI', 'Oakwood_Traditional',
    'Penn_DLI', 'Penn_Traditional',
    'Rosecrest', 'Upland Terrace'
]

# Get other schools (not in Area 5)
other_schools = sorted([col for col in matrix2.columns if col not in area5_schools])

# Combine: Area 5 schools first, then other schools
column_order = area5_schools + other_schools

# Only include columns that actually exist
column_order = [col for col in column_order if col in matrix2.columns]

matrix2 = matrix2[column_order]

# Reorder rows: Area 5 boundaries first (uppercase), then other boundaries alphabetically
area5_boundaries = ['COTTONWOOD', 'CRESTVIEW', 'DRIGGS', 'EASTWOOD', 'MORNINGSIDE',
                    'OAKRIDGE', 'OAKWOOD', 'PENN', 'ROSECREST', 'UPLAND TERRACE']
other_boundaries = sorted([idx for idx in matrix2.index if idx not in area5_boundaries])
row_order = area5_boundaries + other_boundaries
matrix2 = matrix2.reindex(row_order)

# Save Matrix 2
matrix2.to_csv('C:/PAC_Study/tables/student_mobility2_matrices/matrix2_with_programs.csv')

print("="*80)
print("MATRIX 2 WITH PROGRAM BREAKOUTS COMPLETED")
print("="*80)
print(f"\nMatrix 2 shape: {matrix2.shape[0]} boundaries x {matrix2.shape[1]} schools/programs")
print(f"Matrix 2 total students: {matrix2.sum().sum()}")
print(f"\nColumns: {list(matrix2.columns)}")

# Verification
print("\n" + "="*80)
print("VERIFICATION - Check totals match original:")
print("="*80)
if 'Morningside' in matrix1.columns:
    print(f"Morningside Total (Matrix 1): {matrix1['Morningside'].sum()}")
    print(f"Morningside ALC + DLI + Trad (Matrix 2): {matrix2['Morningside_ALC'].sum() + matrix2['Morningside_DLI'].sum() + matrix2['Morningside_Traditional'].sum()}")
else:
    print(f"Morningside ALC + DLI + Trad (Matrix 2): {matrix2['Morningside_ALC'].sum() + matrix2['Morningside_DLI'].sum() + matrix2['Morningside_Traditional'].sum()}")

if 'Oakwood' in matrix1.columns:
    print(f"Oakwood Total (Matrix 1): {matrix1['Oakwood'].sum()}")
    print(f"Oakwood DLI + Trad (Matrix 2): {matrix2['Oakwood_DLI'].sum() + matrix2['Oakwood_Traditional'].sum()}")
else:
    print(f"Oakwood DLI + Trad (Matrix 2): {matrix2['Oakwood_DLI'].sum() + matrix2['Oakwood_Traditional'].sum()}")

if 'Penn' in matrix1.columns:
    print(f"Penn Total (Matrix 1): {matrix1['Penn'].sum()}")
    print(f"Penn DLI + Trad (Matrix 2): {matrix2['Penn_DLI'].sum() + matrix2['Penn_Traditional'].sum()}")
else:
    print(f"Penn DLI + Trad (Matrix 2): {matrix2['Penn_DLI'].sum() + matrix2['Penn_Traditional'].sum()}")

# Show sample rows
print("\n" + "="*80)
print("SAMPLE DATA - First 10 boundaries with Morningside students:")
print("="*80)
morningside_cols = ['Morningside_ALC', 'Morningside_DLI', 'Morningside_Traditional']
sample = matrix2[morningside_cols][matrix2[morningside_cols].sum(axis=1) > 0].head(10)
print(sample)

print("\nMatrix 2 saved to: C:/PAC_Study/tables/student_mobility2_matrices/matrix2_with_programs.csv")
