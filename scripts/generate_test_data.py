"""
Generate synthetic test patient data for QA testing
Creates 5 test cases per disease: 2 Low, 1 Medium, 2 High risk
"""

import pandas as pd
from pathlib import Path

# Create output directory
output_dir = Path('data/sample')
output_dir.mkdir(parents=True, exist_ok=True)

# Diabetes test patients
diabetes_test = pd.DataFrame({
    'Pregnancies':  [0, 1, 3, 8, 5],
    'Glucose':      [85, 92, 130, 195, 148],
    'BloodPressure':[70, 72, 80,  90,  85],
    'SkinThickness':[20, 23, 29,  35,  30],
    'Insulin':      [80, 85, 120, 200, 140],
    'BMI':          [22.0, 24.1, 31.2, 41.5, 35.3],
    'DiabetesPedigreeFunction': [0.2, 0.3, 0.5, 0.8, 0.6],
    'Age':          [25, 30, 38, 55, 44]
})
diabetes_test.to_csv(output_dir / 'diabetes_test.csv', index=False)
print(f'✓ Created diabetes_test.csv with {len(diabetes_test)} patients')

# Heart disease test patients
heart_test = pd.DataFrame({
    'age':     [35, 42, 50, 62, 58],
    'sex':     [1, 0, 1, 1, 0],
    'cp':      [0, 1, 2, 3, 2],
    'trestbps':[110, 120, 135, 150, 140],
    'chol':    [180, 200, 240, 280, 260],
    'fbs':     [0, 0, 1, 1, 1],
    'restecg': [0, 1, 0, 1, 0],
    'thalach': [170, 160, 145, 120, 130],
    'exang':   [0, 0, 1, 1, 1],
    'oldpeak': [0.5, 1.0, 1.5, 3.0, 2.5],
    'slope':   [2, 2, 1, 0, 1],
    'ca':      [0, 0, 1, 2, 2],
    'thal':    [2, 2, 3, 3, 3]
})
heart_test.to_csv(output_dir / 'heart_test.csv', index=False)
print(f'✓ Created heart_test.csv with {len(heart_test)} patients')

# CKD test patients
ckd_test = pd.DataFrame({
    'age':   [28, 45, 55, 65, 60],
    'bp':    [70, 80, 90, 100, 95],
    'sg':    [1.020, 1.015, 1.010, 1.005, 1.008],
    'al':    [0, 1, 2, 4, 3],
    'su':    [0, 0, 1, 2, 1],
    'bgr':   [95, 110, 140, 180, 160],
    'bu':    [25, 35, 50, 80, 65],
    'sc':    [0.8, 1.0, 1.5, 3.5, 2.5],
    'sod':   [140, 138, 135, 130, 132],
    'pot':   [4.2, 4.0, 3.8, 3.2, 3.5],
    'hemo':  [15.5, 14.0, 12.0, 9.5, 10.5],
    'pcv':   [45, 42, 38, 30, 32],
    'wbcc':  [8000, 9000, 11000, 15000, 13000],
    'rbcc':  [5.2, 4.8, 4.2, 3.5, 3.8],
    'htn':   [0, 0, 1, 1, 1],
    'dm':    [0, 0, 1, 1, 1],
    'cad':   [0, 0, 0, 1, 0],
    'appet': [1, 1, 0, 0, 0],
    'pe':    [0, 0, 1, 1, 1],
    'ane':   [0, 0, 1, 1, 1]
})
ckd_test.to_csv(output_dir / 'ckd_test.csv', index=False)
print(f'✓ Created ckd_test.csv with {len(ckd_test)} patients')

print('\n✅ All test datasets generated successfully!')
print(f'Location: {output_dir.absolute()}')
