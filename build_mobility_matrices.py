"""
Build Matrix 1: Complete mobility matrix with ALL schools (FROM and TO)
This matrix includes ALL boundaries and ALL schools that students attend,
not just the 10 Area 5 schools.

Matrix shows: FROM (boundary) x TO (attending school) = count of students
"""

import pandas as pd
import numpy as np
from collections import defaultdict

# ==============================================================================
# MATRIX 1: ALL SCHOOLS - COMPLETE MOBILITY DATA
# This uses mobility data from all 17 PDF tables
# Shows: Students FROM boundary X who attend school Y (any school, not just Area 5)
# ==============================================================================

# Data extracted from all 17 PDF mobility tables
# Format: (FROM_boundary, TO_school): student_count

matrix1_data = {}

# Cottonwood Elementary - students attending Cottonwood
matrix1_data[('COTTONWOOD', 'Cottonwood')] = 233
matrix1_data[('CRESTVIEW', 'Cottonwood')] = 1
matrix1_data[('DRIGGS', 'Cottonwood')] = 13
matrix1_data[('MORNINGSIDE', 'Cottonwood')] = 2
matrix1_data[('MOSS', 'Cottonwood')] = 5
matrix1_data[('OAKRIDGE', 'Cottonwood')] = 2
matrix1_data[('OAKWOOD', 'Cottonwood')] = 45
matrix1_data[('Out of District', 'Cottonwood')] = 28
matrix1_data[('PENN', 'Cottonwood')] = 4
matrix1_data[('ROSECREST', 'Cottonwood')] = 1
matrix1_data[('UPLAND TERRACE', 'Cottonwood')] = 2
matrix1_data[('ARMSTRONG', 'Cottonwood')] = 1
matrix1_data[('HILLSDALE', 'Cottonwood')] = 1
matrix1_data[('LINCOLN', 'Cottonwood')] = 1
matrix1_data[('OLENE WALKER', 'Cottonwood')] = 1
matrix1_data[('TRUMAN', 'Cottonwood')] = 1
matrix1_data[('WOODSTOCK', 'Cottonwood')] = 1

# Crestview Elementary - students attending Crestview
matrix1_data[('CRESTVIEW', 'Crestview')] = 430
matrix1_data[('DRIGGS', 'Crestview')] = 12
matrix1_data[('FREMONT', 'Crestview')] = 2
matrix1_data[('LINCOLN', 'Crestview')] = 3
matrix1_data[('MOSS', 'Crestview')] = 3
matrix1_data[('OAKWOOD', 'Crestview')] = 1
matrix1_data[('OLENE WALKER', 'Crestview')] = 1
matrix1_data[('Out of District', 'Crestview')] = 7
matrix1_data[('PENN', 'Crestview')] = 11
matrix1_data[('ROSECREST', 'Crestview')] = 2
matrix1_data[('UPLAND TERRACE', 'Crestview')] = 1
matrix1_data[('WOODSTOCK', 'Crestview')] = 1

# Driggs Elementary - students attending Driggs
matrix1_data[('COTTONWOOD', 'Driggs')] = 4
matrix1_data[('CRESTVIEW', 'Driggs')] = 9
matrix1_data[('DRIGGS', 'Driggs')] = 341
matrix1_data[('EASTWOOD', 'Driggs')] = 1
matrix1_data[('JACKLING', 'Driggs')] = 1
matrix1_data[('LINCOLN', 'Driggs')] = 10
matrix1_data[('MORNINGSIDE', 'Driggs')] = 33
matrix1_data[('MOSS', 'Driggs')] = 10
matrix1_data[('OAKWOOD', 'Driggs')] = 9
matrix1_data[('Out of District', 'Driggs')] = 9
matrix1_data[('PENN', 'Driggs')] = 4
matrix1_data[('PLYMOUTH', 'Driggs')] = 1
matrix1_data[('ROSECREST', 'Driggs')] = 1
matrix1_data[('SMITH', 'Driggs')] = 1

# Eastwood Elementary - students attending Eastwood
matrix1_data[('ARMSTRONG', 'Eastwood')] = 1
matrix1_data[('BRIDGER', 'Eastwood')] = 1
matrix1_data[('COTTONWOOD', 'Eastwood')] = 1
matrix1_data[('CRESTVIEW', 'Eastwood')] = 3
matrix1_data[('DRIGGS', 'Eastwood')] = 2
matrix1_data[('EASTWOOD', 'Eastwood')] = 125
matrix1_data[('GRANGER', 'Eastwood')] = 2
matrix1_data[('LAKE RIDGE', 'Eastwood')] = 1
matrix1_data[('LINCOLN', 'Eastwood')] = 7
matrix1_data[('MAGNA', 'Eastwood')] = 1
matrix1_data[('MORNINGSIDE', 'Eastwood')] = 29
matrix1_data[('MOSS', 'Eastwood')] = 4
matrix1_data[('OAKRIDGE', 'Eastwood')] = 5
matrix1_data[('OAKWOOD', 'Eastwood')] = 1
matrix1_data[('OLENE WALKER', 'Eastwood')] = 4
matrix1_data[('Out of District', 'Eastwood')] = 30
matrix1_data[('PENN', 'Eastwood')] = 12
matrix1_data[('PLYMOUTH', 'Eastwood')] = 1
matrix1_data[('REDWOOD', 'Eastwood')] = 3
matrix1_data[('ROSECREST', 'Eastwood')] = 10
matrix1_data[('UPLAND TERRACE', 'Eastwood')] = 12
matrix1_data[('WHITTIER', 'Eastwood')] = 1
matrix1_data[('WILSON', 'Eastwood')] = 11

# Morningside Elementary - students attending Morningside (TOTAL enrollment)
matrix1_data[('ACADEMY PARK', 'Morningside')] = 2
matrix1_data[('COTTONWOOD', 'Morningside')] = 18
matrix1_data[('CRESTVIEW', 'Morningside')] = 25
matrix1_data[('DIAMOND RIDGE', 'Morningside')] = 1
matrix1_data[('DRIGGS', 'Morningside')] = 38
matrix1_data[('EASTWOOD', 'Morningside')] = 10
matrix1_data[('FARNSWORTH', 'Morningside')] = 2
matrix1_data[('FREMONT', 'Morningside')] = 2
matrix1_data[('GRANGER', 'Morningside')] = 1
matrix1_data[('LINCOLN', 'Morningside')] = 16
matrix1_data[('MORNINGSIDE', 'Morningside')] = 189
matrix1_data[('MOSS', 'Morningside')] = 12
matrix1_data[('OAKRIDGE', 'Morningside')] = 36
matrix1_data[('OAKWOOD', 'Morningside')] = 9
matrix1_data[('OLENE WALKER', 'Morningside')] = 2
matrix1_data[('ORCHARD', 'Morningside')] = 2
matrix1_data[('Out of District', 'Morningside')] = 73
matrix1_data[('PENN', 'Morningside')] = 16
matrix1_data[('ROSECREST', 'Morningside')] = 29
matrix1_data[('SILVER HILLS', 'Morningside')] = 2
matrix1_data[('SOUTH KEARNS', 'Morningside')] = 1
matrix1_data[('TAYLORSVILLE', 'Morningside')] = 3
matrix1_data[('TRUMAN', 'Morningside')] = 1
matrix1_data[('UPLAND TERRACE', 'Morningside')] = 42
matrix1_data[('VALLEY CREST', 'Morningside')] = 3
matrix1_data[('VISTA', 'Morningside')] = 1
matrix1_data[('WILSON', 'Morningside')] = 11
matrix1_data[('WOODSTOCK', 'Morningside')] = 14

# Oakridge Elementary - students attending Oakridge
matrix1_data[('COTTONWOOD', 'Oakridge')] = 1
matrix1_data[('CRESTVIEW', 'Oakridge')] = 3
matrix1_data[('DRIGGS', 'Oakridge')] = 3
matrix1_data[('EASTWOOD', 'Oakridge')] = 26
matrix1_data[('MORNINGSIDE', 'Oakridge')] = 25
matrix1_data[('MOSS', 'Oakridge')] = 1
matrix1_data[('OAKRIDGE', 'Oakridge')] = 181
matrix1_data[('OAKWOOD', 'Oakridge')] = 2
matrix1_data[('OLENE WALKER', 'Oakridge')] = 6
matrix1_data[('Out of District', 'Oakridge')] = 17
matrix1_data[('REDWOOD', 'Oakridge')] = 1
matrix1_data[('ROLLING MEADOWS', 'Oakridge')] = 2
matrix1_data[('ROSECREST', 'Oakridge')] = 1
matrix1_data[('UPLAND TERRACE', 'Oakridge')] = 3
matrix1_data[('WILSON', 'Oakridge')] = 2
matrix1_data[('WOODSTOCK', 'Oakridge')] = 3

# Oakwood Elementary - students attending Oakwood (TOTAL enrollment)
matrix1_data[('COTTONWOOD', 'Oakwood')] = 3
matrix1_data[('CRESTVIEW', 'Oakwood')] = 9
matrix1_data[('DRIGGS', 'Oakwood')] = 2
matrix1_data[('EASTWOOD', 'Oakwood')] = 1
matrix1_data[('FREMONT', 'Oakwood')] = 3
matrix1_data[('LINCOLN', 'Oakwood')] = 8
matrix1_data[('MORNINGSIDE', 'Oakwood')] = 1
matrix1_data[('MOSS', 'Oakwood')] = 31
matrix1_data[('OAKRIDGE', 'Oakwood')] = 2
matrix1_data[('OAKWOOD', 'Oakwood')] = 329
matrix1_data[('OLENE WALKER', 'Oakwood')] = 5
matrix1_data[('ORCHARD', 'Oakwood')] = 1
matrix1_data[('Out of District', 'Oakwood')] = 84
matrix1_data[('PENN', 'Oakwood')] = 7
matrix1_data[('PLYMOUTH', 'Oakwood')] = 1
matrix1_data[('ROSECREST', 'Oakwood')] = 2
matrix1_data[('SMITH', 'Oakwood')] = 2
matrix1_data[('TAYLORSVILLE', 'Oakwood')] = 1
matrix1_data[('TRUMAN', 'Oakwood')] = 1
matrix1_data[('VISTA', 'Oakwood')] = 1
matrix1_data[('WILSON', 'Oakwood')] = 9
matrix1_data[('WOODSTOCK', 'Oakwood')] = 30

# Penn Elementary - students attending Penn (TOTAL enrollment)
matrix1_data[('ARCADIA', 'Penn')] = 2
matrix1_data[('BACCHUS', 'Penn')] = 1
matrix1_data[('COTTONWOOD', 'Penn')] = 11
matrix1_data[('CRESTVIEW', 'Penn')] = 26
matrix1_data[('DRIGGS', 'Penn')] = 11
matrix1_data[('EASTWOOD', 'Penn')] = 2
matrix1_data[('FREMONT', 'Penn')] = 3
matrix1_data[('FROST', 'Penn')] = 1
matrix1_data[('GRANGER', 'Penn')] = 1
matrix1_data[('LINCOLN', 'Penn')] = 70
matrix1_data[('MORNINGSIDE', 'Penn')] = 6
matrix1_data[('MOSS', 'Penn')] = 48
matrix1_data[('OAKRIDGE', 'Penn')] = 1
matrix1_data[('OAKWOOD', 'Penn')] = 10
matrix1_data[('OLENE WALKER', 'Penn')] = 13
matrix1_data[('Out of District', 'Penn')] = 50
matrix1_data[('PENN', 'Penn')] = 273
matrix1_data[('PLYMOUTH', 'Penn')] = 1
matrix1_data[('ROSECREST', 'Penn')] = 31
matrix1_data[('STANSBURY', 'Penn')] = 1
matrix1_data[('TAYLORSVILLE', 'Penn')] = 4
matrix1_data[('TRUMAN', 'Penn')] = 2
matrix1_data[('UPLAND TERRACE', 'Penn')] = 12
matrix1_data[('WILSON', 'Penn')] = 20
matrix1_data[('WOODSTOCK', 'Penn')] = 6

# Rosecrest Elementary - students attending Rosecrest
matrix1_data[('COTTONWOOD', 'Rosecrest')] = 1
matrix1_data[('CRESTVIEW', 'Rosecrest')] = 1
matrix1_data[('LINCOLN', 'Rosecrest')] = 9
matrix1_data[('MORNINGSIDE', 'Rosecrest')] = 4
matrix1_data[('MOSS', 'Rosecrest')] = 4
matrix1_data[('OLENE WALKER', 'Rosecrest')] = 1
matrix1_data[('Out of District', 'Rosecrest')] = 15
matrix1_data[('PENN', 'Rosecrest')] = 7
matrix1_data[('PLYMOUTH', 'Rosecrest')] = 2
matrix1_data[('REDWOOD', 'Rosecrest')] = 3
matrix1_data[('ROSECREST', 'Rosecrest')] = 237
matrix1_data[('SMITH', 'Rosecrest')] = 1
matrix1_data[('UPLAND TERRACE', 'Rosecrest')] = 1
matrix1_data[('WILSON', 'Rosecrest')] = 5

# Upland Terrace Elementary - students attending Upland Terrace
matrix1_data[('COTTONWOOD', 'Upland Terrace')] = 1
matrix1_data[('CRESTVIEW', 'Upland Terrace')] = 6
matrix1_data[('DRIGGS', 'Upland Terrace')] = 6
matrix1_data[('EASTWOOD', 'Upland Terrace')] = 5
matrix1_data[('LINCOLN', 'Upland Terrace')] = 22
matrix1_data[('MORNINGSIDE', 'Upland Terrace')] = 15
matrix1_data[('MOSS', 'Upland Terrace')] = 12
matrix1_data[('OAKRIDGE', 'Upland Terrace')] = 3
matrix1_data[('OAKWOOD', 'Upland Terrace')] = 3
matrix1_data[('OLENE WALKER', 'Upland Terrace')] = 1
matrix1_data[('Out of District', 'Upland Terrace')] = 10
matrix1_data[('PENN', 'Upland Terrace')] = 6
matrix1_data[('PIONEER', 'Upland Terrace')] = 1
matrix1_data[('ROSECREST', 'Upland Terrace')] = 5
matrix1_data[('TRUMAN', 'Upland Terrace')] = 1
matrix1_data[('UPLAND TERRACE', 'Upland Terrace')] = 322
matrix1_data[('WHITTIER', 'Upland Terrace')] = 1
matrix1_data[('WILSON', 'Upland Terrace')] = 16
matrix1_data[('WOODSTOCK', 'Upland Terrace')] = 5

# ==============================================================================
# OTHER SCHOOLS - Where students FROM Area 5 boundaries GO TO other schools
# ==============================================================================

# COTTONWOOD boundary - students attending other schools (not in Area 5)
matrix1_data[('COTTONWOOD', 'Alternative 3-A Elementary')] = 3
matrix1_data[('COTTONWOOD', 'Hartvigsen School')] = 2
matrix1_data[('COTTONWOOD', 'Woodstock Elementary')] = 1

# CRESTVIEW boundary - students attending other schools (not in Area 5)
matrix1_data[('CRESTVIEW', 'Alternative 3-A Elementary')] = 15
matrix1_data[('CRESTVIEW', 'Granger Elementary')] = 1
matrix1_data[('CRESTVIEW', 'Vista Elementary')] = 2
matrix1_data[('CRESTVIEW', 'Woodstock Elementary')] = 5

# DRIGGS boundary - students attending other schools (not in Area 5)
matrix1_data[('DRIGGS', 'Alternative 3-A Elementary')] = 8
matrix1_data[('DRIGGS', 'Yess Salt Lake County Youth Services')] = 1

# EASTWOOD boundary - students attending other schools (not in Area 5)
matrix1_data[('EASTWOOD', 'Alternative 3-A Elementary')] = 1

# MORNINGSIDE boundary - students attending other schools (not in Area 5)
matrix1_data[('MORNINGSIDE', 'Alternative 3-A Elementary')] = 4
matrix1_data[('MORNINGSIDE', 'Woodstock Elementary')] = 1

# OAKRIDGE boundary - students attending other schools (not in Area 5)
matrix1_data[('OAKRIDGE', 'Alternative 3-A Elementary')] = 4
matrix1_data[('OAKRIDGE', 'Woodstock Elementary')] = 3

# OAKWOOD boundary - students attending other schools (not in Area 5)
matrix1_data[('OAKWOOD', 'Academy Park Elementary')] = 1
matrix1_data[('OAKWOOD', 'Alternative 3-A Elementary')] = 13
matrix1_data[('OAKWOOD', 'Arcadia Elementary')] = 1
matrix1_data[('OAKWOOD', 'Granger Elementary')] = 1
matrix1_data[('OAKWOOD', 'Hartvigsen School')] = 1
matrix1_data[('OAKWOOD', 'Woodstock Elementary')] = 44

# PENN boundary - students attending other schools (not in Area 5)
matrix1_data[('PENN', 'Alternative 3-A Elementary')] = 3
matrix1_data[('PENN', 'Woodstock Elementary')] = 3

# ROSECREST boundary - students attending other schools (not in Area 5)
matrix1_data[('ROSECREST', 'Alternative 3-A Elementary')] = 8
matrix1_data[('ROSECREST', 'Neil Armstrong Academy')] = 1
matrix1_data[('ROSECREST', 'Woodrow Wilson Elementary')] = 1
matrix1_data[('ROSECREST', 'Woodstock Elementary')] = 1

# UPLAND TERRACE boundary - students attending other schools (not in Area 5)
matrix1_data[('UPLAND TERRACE', 'Alternative 3-A Elementary')] = 6
matrix1_data[('UPLAND TERRACE', 'Calvin S Smith Elementary')] = 1
matrix1_data[('UPLAND TERRACE', 'Woodstock Elementary')] = 4

print("Matrix 1 data extracted - ALL schools (Area 5 and others)")
print(f"Total pairs in Matrix 1: {len(matrix1_data)}")

# Convert to DataFrame
df1 = pd.DataFrame([(from_boundary, to_school, count)
                     for (from_boundary, to_school), count in matrix1_data.items()],
                    columns=['From_Boundary', 'To_School', 'Count'])

# Pivot to create matrix
matrix1 = df1.pivot_table(index='From_Boundary', columns='To_School',
                           values='Count', fill_value=0, aggfunc='sum')

# Reorder columns: Area 5 schools first, then other schools alphabetically
area5_schools = ['Cottonwood', 'Crestview', 'Driggs', 'Eastwood', 'Morningside',
                 'Oakridge', 'Oakwood', 'Penn', 'Rosecrest', 'Upland Terrace']
other_schools = sorted([col for col in matrix1.columns if col not in area5_schools])
column_order = area5_schools + other_schools
matrix1 = matrix1[column_order]

# Reorder rows: Area 5 boundaries first (uppercase), then other boundaries alphabetically
area5_boundaries = ['COTTONWOOD', 'CRESTVIEW', 'DRIGGS', 'EASTWOOD', 'MORNINGSIDE',
                    'OAKRIDGE', 'OAKWOOD', 'PENN', 'ROSECREST', 'UPLAND TERRACE']
other_boundaries = sorted([idx for idx in matrix1.index if idx not in area5_boundaries])
row_order = area5_boundaries + other_boundaries
matrix1 = matrix1.reindex(row_order)

# Save Matrix 1
matrix1.to_csv('C:/PAC_Study/tables/student_mobility2_matrices/matrix1_basic_10_schools.csv')

print("\n" + "="*80)
print("MATRIX 1 COMPLETED")
print("="*80)
print(f"Matrix 1 shape: {matrix1.shape[0]} boundaries x {matrix1.shape[1]} schools")
print(f"Matrix 1 total students: {matrix1.sum().sum()}")
print(f"\nMatrix 1 saved to: C:/PAC_Study/tables/student_mobility2_matrices/matrix1_basic_10_schools.csv")
