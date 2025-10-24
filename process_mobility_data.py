"""
Process student mobility data from PDFs and create three matrices:
1. Basic 10 schools only
2. Basic + DLI/ALC (with adjustments to avoid double counting)
3. Basic + geographic portions (with adjustments to avoid double counting)
"""

import pandas as pd
import numpy as np
from collections import defaultdict

# Matrix 1: Basic 10 schools - attending school data (left tables)
# This shows: students FROM boundary X attending school Y

matrix1_data = {
    # Cottonwood - students who attend Cottonwood and where they come from
    ('COTTONWOOD', 'Cottonwood'): 233,
    ('CRESTVIEW', 'Cottonwood'): 1,
    ('DRIGGS', 'Cottonwood'): 10,
    ('MORNINGSIDE', 'Cottonwood'): 2,
    ('MOSS', 'Cottonwood'): 5,
    ('OAKRIDGE', 'Cottonwood'): 2,
    ('OAKWOOD', 'Cottonwood'): 45,
    ('Out of District', 'Cottonwood'): 28,
    ('PENN', 'Cottonwood'): 4,
    ('ROSECREST', 'Cottonwood'): 1,
    ('UPLAND TERRACE', 'Cottonwood'): 2,

    # Crestview - students who attend Crestview and where they come from
    ('CRESTVIEW', 'Crestview'): 430,
    ('DRIGGS', 'Crestview'): 12,
    ('LINCOLN', 'Crestview'): 3,
    ('MOSS', 'Crestview'): 3,
    ('OAKWOOD', 'Crestview'): 1,
    ('Out of District', 'Crestview'): 7,
    ('PENN', 'Crestview'): 11,
    ('ROSECREST', 'Crestview'): 2,
    ('UPLAND TERRACE', 'Crestview'): 1,

    # Driggs - students who attend Driggs and where they come from
    ('COTTONWOOD', 'Driggs'): 4,
    ('CRESTVIEW', 'Driggs'): 9,
    ('DRIGGS', 'Driggs'): 341,
    ('EASTWOOD', 'Driggs'): 1,
    ('LINCOLN', 'Driggs'): 10,
    ('MORNINGSIDE', 'Driggs'): 33,
    ('MOSS', 'Driggs'): 10,
    ('OAKWOOD', 'Driggs'): 9,
    ('Out of District', 'Driggs'): 8,
    ('PENN', 'Driggs'): 4,
    ('ROSECREST', 'Driggs'): 1,

    # Eastwood - students who attend Eastwood and where they come from
    ('COTTONWOOD', 'Eastwood'): 1,
    ('CRESTVIEW', 'Eastwood'): 3,
    ('DRIGGS', 'Eastwood'): 2,
    ('EASTWOOD', 'Eastwood'): 125,
    ('LINCOLN', 'Eastwood'): 7,
    ('MORNINGSIDE', 'Eastwood'): 29,
    ('MOSS', 'Eastwood'): 4,
    ('OAKRIDGE', 'Eastwood'): 5,
    ('OAKWOOD', 'Eastwood'): 1,
    ('Out of District', 'Eastwood'): 30,
    ('PENN', 'Eastwood'): 12,
    ('ROSECREST', 'Eastwood'): 10,
    ('UPLAND TERRACE', 'Eastwood'): 12,

    # Morningside - students who attend Morningside and where they come from
    ('COTTONWOOD', 'Morningside'): 18,
    ('CRESTVIEW', 'Morningside'): 25,
    ('DRIGGS', 'Morningside'): 38,
    ('EASTWOOD', 'Morningside'): 10,
    ('LINCOLN', 'Morningside'): 16,
    ('MORNINGSIDE', 'Morningside'): 189,
    ('MOSS', 'Morningside'): 12,
    ('OAKRIDGE', 'Morningside'): 36,
    ('OAKWOOD', 'Morningside'): 9,
    ('Out of District', 'Morningside'): 73,
    ('PENN', 'Morningside'): 16,
    ('ROSECREST', 'Morningside'): 29,
    ('UPLAND TERRACE', 'Morningside'): 42,
}

# Need to continue with remaining schools...
# Let me read the remaining PDFs first

print("Script created - need to extract data from remaining PDFs")
print("Schools remaining: Oakridge, Oakwood, Penn, Rosecrest, Upland Terrace")
