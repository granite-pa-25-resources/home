"""
Build Matrix 3 with geographic portion breakouts:
- For boundaries with geographic portions, show:
  - "Morningside" (the main portion, minus North portion)
  - "Morningside North Portion" (separate)
  - "Oakwood Southeast Portion" (in Area 5)
  - "Oakwood West Portion" (not in Area 5)
  - "Oakwood" (the remainder after subtracting portions)

For ATTENDING schools, we keep all 10 schools as columns.
The geographic portions affect the FROM boundary rows, not the TO school columns.
"""

import pandas as pd
import numpy as np

# Import Matrix 1 as starting point
matrix1 = pd.read_csv('C:/PAC_Study/tables/student_mobility2_matrices/matrix1_basic_10_schools.csv', index_col=0)

# ==============================================================================
# MORNINGSIDE NORTH PORTION
# Where students from Morningside North Portion GO (47 total students)
# ==============================================================================
morningside_north_destination = {
    'Alternative 3-A Elementary': 2,  # Not in our 10 schools
    'Eastwood': 14,
    'Morningside': 22,
    'Rosecrest': 4,
    'Upland Terrace': 4,
    'Penn': 1  # Not in our 10 schools
}

# Map to our school columns (only the 10 Area 5 schools)
morningside_north_to_schools = {
    'Eastwood': 14,
    'Morningside': 22,
    'Rosecrest': 4,
    'Upland Terrace': 4
}

# ==============================================================================
# OAKWOOD SOUTHEAST PORTION (K-12, but we only care about K-5)
# From the table, only 1 K-5 student attending Oakwood
# ==============================================================================
oakwood_southeast_to_schools = {
    'Oakwood': 1
}

# ==============================================================================
# OAKWOOD WEST PORTION
# Where students from Oakwood West Portion GO (463 total K-5 students)
# ==============================================================================
oakwood_west_to_schools = {
    'Cottonwood': 41,
    'Crestview': 1,
    'Driggs': 8,
    'Eastwood': 1,
    'Morningside': 8,
    'Oakridge': 1,
    'Oakwood': 328,
    'Penn': 10,
    'Upland Terrace': 3,
    'Woodstock': 44
}

# Note: Now including ALL schools, not just Area 5

# ==============================================================================
# Now we need to SUBTRACT these portions from the main boundary totals
# ==============================================================================

# Create Matrix 3
matrix3 = matrix1.copy()

# Add new rows for the geographic portions
matrix3.loc['Morningside North Portion'] = 0
matrix3.loc['Oakwood Southeast Portion'] = 0
matrix3.loc['Oakwood West Portion'] = 0

# Fill in the values for these new boundary rows
for school, count in morningside_north_to_schools.items():
    if school in matrix3.columns:
        matrix3.loc['Morningside North Portion', school] = count

for school, count in oakwood_southeast_to_schools.items():
    if school in matrix3.columns:
        matrix3.loc['Oakwood Southeast Portion', school] = count

for school, count in oakwood_west_to_schools.items():
    if school in matrix3.columns:
        matrix3.loc['Oakwood West Portion', school] = count

# SUBTRACT the portions from the main boundaries
# Morningside boundary: Total 309 students, subtract North Portion (47)
# The Morningside North students who go to Morningside are already in the total
# We need to subtract them from the MORNINGSIDE boundary row

# From the Morningside boundary row, subtract what goes through North Portion
if 'MORNINGSIDE' in matrix3.index:
    # Morningside North sends: 14 to Eastwood, 22 to Morningside, 4 to Rosecrest, 4 to Upland Terrace
    # These are part of the Morningside boundary total
    # So we subtract them from MORNINGSIDE boundary's attendance at each school
    for school, count in morningside_north_to_schools.items():
        if school in matrix3.columns:
            matrix3.loc['MORNINGSIDE', school] = max(0, matrix3.loc['MORNINGSIDE', school] - count)

# From Oakwood boundary row, subtract the Southeast and West portions
if 'OAKWOOD' in matrix3.index:
    # Oakwood Southeast portion (only 1 student to Oakwood)
    for school, count in oakwood_southeast_to_schools.items():
        if school in matrix3.columns:
            matrix3.loc['OAKWOOD', school] = max(0, matrix3.loc['OAKWOOD', school] - count)

    # Oakwood West portion
    for school, count in oakwood_west_to_schools.items():
        if school in matrix3.columns:
            matrix3.loc['OAKWOOD', school] = max(0, matrix3.loc['OAKWOOD', school] - count)

# Reorder columns: Area 5 schools first, then other schools alphabetically
area5_schools = ['Cottonwood', 'Crestview', 'Driggs', 'Eastwood', 'Morningside',
                 'Oakridge', 'Oakwood', 'Penn', 'Rosecrest', 'Upland Terrace']
other_schools = sorted([col for col in matrix3.columns if col not in area5_schools])
column_order = area5_schools + other_schools
matrix3 = matrix3[column_order]

# Reorder rows: Area 5 boundaries first, then geographic portions, then other boundaries alphabetically
area5_boundaries = ['COTTONWOOD', 'CRESTVIEW', 'DRIGGS', 'EASTWOOD', 'MORNINGSIDE',
                    'OAKRIDGE', 'OAKWOOD', 'PENN', 'ROSECREST', 'UPLAND TERRACE']
geographic_portions = ['Morningside North Portion', 'Oakwood Southeast Portion', 'Oakwood West Portion']
other_boundaries = sorted([idx for idx in matrix3.index
                          if idx not in area5_boundaries and idx not in geographic_portions])
row_order = area5_boundaries + geographic_portions + other_boundaries
matrix3 = matrix3.reindex(row_order)

# Save Matrix 3
matrix3.to_csv('C:/PAC_Study/tables/student_mobility2_matrices/matrix3_with_geographic_portions.csv')

print("="*80)
print("MATRIX 3 WITH GEOGRAPHIC PORTIONS COMPLETED")
print("="*80)
print(f"\nMatrix 3 shape: {matrix3.shape[0]} boundaries x {matrix3.shape[1]} schools")
print(f"Matrix 3 total students: {matrix3.sum().sum()}")

# Verification
print("\n" + "="*80)
print("VERIFICATION - Geographic portion accounting:")
print("="*80)

# Morningside boundary check
if 'MORNINGSIDE' in matrix3.index:
    morningside_main = matrix3.loc['MORNINGSIDE'].sum()
    morningside_north = matrix3.loc['Morningside North Portion'].sum()
    morningside_combined = morningside_main + morningside_north
    morningside_matrix1 = matrix1.loc['MORNINGSIDE'].sum()

    print(f"Morningside (Matrix 1 original): {morningside_matrix1}")
    print(f"Morningside main portion (Matrix 3): {morningside_main}")
    print(f"Morningside North Portion (Matrix 3): {morningside_north}")
    print(f"Sum of portions: {morningside_combined}")
    print(f"Note: North Portion is a subset, so combined should equal original")

# Oakwood boundary check
if 'OAKWOOD' in matrix3.index:
    oakwood_main = matrix3.loc['OAKWOOD'].sum()
    oakwood_southeast = matrix3.loc['Oakwood Southeast Portion'].sum()
    oakwood_west = matrix3.loc['Oakwood West Portion'].sum()
    oakwood_combined = oakwood_main + oakwood_southeast + oakwood_west
    oakwood_matrix1 = matrix1.loc['OAKWOOD'].sum()

    print(f"\nOakwood (Matrix 1 original): {oakwood_matrix1}")
    print(f"Oakwood main portion (Matrix 3): {oakwood_main}")
    print(f"Oakwood Southeast Portion (Matrix 3): {oakwood_southeast}")
    print(f"Oakwood West Portion (Matrix 3): {oakwood_west}")
    print(f"Sum of portions: {oakwood_combined}")
    print(f"Note: Portions are subsets, so combined should equal original")

# Show the new rows
print("\n" + "="*80)
print("NEW GEOGRAPHIC PORTION ROWS:")
print("="*80)
print("\nMorningside North Portion:")
print(matrix3.loc['Morningside North Portion'])
print("\nOakwood Southeast Portion:")
print(matrix3.loc['Oakwood Southeast Portion'])
print("\nOakwood West Portion:")
print(matrix3.loc['Oakwood West Portion'])

# Show adjusted main boundaries
print("\n" + "="*80)
print("ADJUSTED MAIN BOUNDARIES (after subtracting portions):")
print("="*80)
print("\nMORNINGSIDE (main, minus North Portion):")
print(matrix3.loc['MORNINGSIDE'])
print("\nOAKWOOD (main, minus Southeast and West Portions):")
print(matrix3.loc['OAKWOOD'])

print("\n" + "="*80)
print("Matrix 3 saved to: C:/PAC_Study/tables/student_mobility2_matrices/matrix3_with_geographic_portions.csv")
print("="*80)
