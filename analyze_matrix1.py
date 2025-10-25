"""
Analyze Matrix 1 statistics to show interesting patterns in student mobility
"""
import pandas as pd
import numpy as np

# Read Matrix 1
matrix1 = pd.read_csv('C:/PAC_Study/tables/student_mobility2_matrices/matrix1_basic_10_schools.csv', index_col=0)

print("="*80)
print("MATRIX 1 INTERESTING STATISTICS")
print("="*80)

# Basic dimensions
print(f"\nMatrix dimensions: {matrix1.shape[0]} boundaries × {matrix1.shape[1]} schools")
print(f"Total students: {matrix1.sum().sum():.0f}")

# Area 5 schools and boundaries
area5_schools = ['Cottonwood', 'Crestview', 'Driggs', 'Eastwood', 'Morningside',
                 'Oakridge', 'Oakwood', 'Penn', 'Rosecrest', 'Upland Terrace']
area5_boundaries = ['COTTONWOOD', 'CRESTVIEW', 'DRIGGS', 'EASTWOOD', 'MORNINGSIDE',
                    'OAKRIDGE', 'OAKWOOD', 'PENN', 'ROSECREST', 'UPLAND TERRACE']

print("\n" + "="*80)
print("1. SCHOOL ENROLLMENTS (Total students attending each school)")
print("="*80)
school_totals = matrix1.sum(axis=0).sort_values(ascending=False)
for school, count in school_totals.head(15).items():
    print(f"{school:40s} {count:5.0f} students")

print("\n" + "="*80)
print("2. BOUNDARY RETENTION RATES (Students staying in their home school)")
print("="*80)
for boundary in area5_boundaries:
    school = boundary.title()
    if boundary in matrix1.index and school in matrix1.columns:
        total_from_boundary = matrix1.loc[boundary].sum()
        staying_home = matrix1.loc[boundary, school]
        retention_rate = (staying_home / total_from_boundary * 100) if total_from_boundary > 0 else 0
        print(f"{boundary:20s} -> {school:20s} {staying_home:4.0f}/{total_from_boundary:4.0f} = {retention_rate:5.1f}%")

print("\n" + "="*80)
print("3. STUDENT OUTFLOW (Students FROM Area 5 boundaries going elsewhere)")
print("="*80)
for boundary in area5_boundaries:
    if boundary in matrix1.index:
        school = boundary.title()
        total_from_boundary = matrix1.loc[boundary].sum()
        staying_home = matrix1.loc[boundary, school] if school in matrix1.columns else 0
        leaving = total_from_boundary - staying_home
        leaving_pct = (leaving / total_from_boundary * 100) if total_from_boundary > 0 else 0
        print(f"{boundary:20s} {leaving:4.0f}/{total_from_boundary:4.0f} leaving ({leaving_pct:5.1f}%)")

print("\n" + "="*80)
print("4. STUDENT INFLOW (Students TO Area 5 schools from other boundaries)")
print("="*80)
for school in area5_schools:
    if school in matrix1.columns:
        boundary = school.upper()
        total_attending = matrix1[school].sum()
        from_home = matrix1.loc[boundary, school] if boundary in matrix1.index else 0
        from_elsewhere = total_attending - from_home
        from_elsewhere_pct = (from_elsewhere / total_attending * 100) if total_attending > 0 else 0
        print(f"{school:20s} {from_elsewhere:4.0f}/{total_attending:4.0f} from elsewhere ({from_elsewhere_pct:5.1f}%)")

print("\n" + "="*80)
print("5. TOP MOBILITY FLOWS (Area 5 boundary -> Area 5 school, excluding home)")
print("="*80)
flows = []
for boundary in area5_boundaries:
    if boundary in matrix1.index:
        for school in area5_schools:
            if school in matrix1.columns:
                # Skip home school
                if boundary.upper() != school.upper():
                    count = matrix1.loc[boundary, school]
                    if count > 0:
                        flows.append((boundary, school, count))

flows_sorted = sorted(flows, key=lambda x: x[2], reverse=True)
for i, (boundary, school, count) in enumerate(flows_sorted[:15], 1):
    print(f"{i:2d}. {boundary:20s} -> {school:20s} {count:4.0f} students")

print("\n" + "="*80)
print("6. ALTERNATIVE/SPECIALTY SCHOOLS (Non-Area 5 destinations)")
print("="*80)
other_schools = [col for col in matrix1.columns if col not in area5_schools]
other_totals = {}
for school in other_schools:
    # Count only from Area 5 boundaries
    total = sum(matrix1.loc[boundary, school] for boundary in area5_boundaries if boundary in matrix1.index)
    if total > 0:
        other_totals[school] = total

for school, count in sorted(other_totals.items(), key=lambda x: x[1], reverse=True):
    print(f"{school:45s} {count:4.0f} students from Area 5")

print("\n" + "="*80)
print("7. MOST DISPERSED BOUNDARIES (Students spread across many schools)")
print("="*80)
for boundary in area5_boundaries:
    if boundary in matrix1.index:
        # Count how many different schools students attend
        schools_attended = (matrix1.loc[boundary] > 0).sum()
        total_students = matrix1.loc[boundary].sum()
        print(f"{boundary:20s} {total_students:4.0f} students -> {schools_attended:2.0f} different schools")

print("\n" + "="*80)
print("8. OUT OF DISTRICT STUDENTS")
print("="*80)
if 'Out of District' in matrix1.index:
    ood_totals = matrix1.loc['Out of District'].sort_values(ascending=False)
    print("Out of District students attending Area 5 schools:")
    for school, count in ood_totals[ood_totals > 0].items():
        if school in area5_schools:
            print(f"  {school:30s} {count:4.0f} students")
    area5_ood_total = sum(ood_totals[school] for school in area5_schools if school in ood_totals.index)
    print(f"\nTotal Out of District students in Area 5 schools: {area5_ood_total:.0f}")
