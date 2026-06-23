# generate_skyline_data.py
# Lesson 1.2: Types of Data and Where to Find It
# Author: Paola Paguaga
# Date: June 22, 2026
#
# Generates a synthetic dataset of 100 fictional course enrollment records.
# illustrating the four scales of measurement (nominal, ordinal, interval,
# ratio). Saves the result as skyline_enrollments.csv.

import random
import numpy as np
import pandas as pd
from datetime import date

random.seed(123)
np.random.seed(123)

n_students = 100

# Course Names (nominal scale: categorical with no order)
course_name = np.random.choice(
    ["Intro to Analytics", "Python for Beginners", "SQL Basics", "Tableau Fundamentals", "Statistics 101"],
    size=n_students,
    p=[0.20, 0.20, 0.20, 0.20, 0.20],
)

#Enrollment year (Interval scale)

enrollment_year = np.random.randint(2022, 2026, size=n_students)

#Final grade (Ordinal scale)
final_grade = np.random.choice(
    ["F", "D", "C", "B", "A"],
    size=n_students,
    p=[0.05, 0.10, 0.20, 0.35, 0.30]
)

# Hours studied (Ratio scale)
hours_studied = np.random.poisson(lam=30, size=n_students)

# completion status (nominal scale)
completion_status = np.random.choice(
    ["Completed", "Dropped", "In Progress"],
    size=n_students,
    p=[0.4, 0.25, 0.35],
)

# Enrollment ID (nominal scale: categorical with no order)
enrollment_ids = [f"ENR-{random.randint(100000, 999999)}" for _ in range(n_students)]

skyline_students = pd.DataFrame({
    "enrollment_id": enrollment_ids,
    "course_name": course_name,
    "enrollment_year": enrollment_year,
    "final_grade": final_grade,
    "hours_studied": hours_studied,
    "completion_status": completion_status,
})

print(skyline_students.head(10))
print(f"\nShape: {skyline_students.shape}")
print(f"\nColumn types:\n{skyline_students.dtypes}")

output_path = "skyline_enrollments.csv"
skyline_students.to_csv(output_path, index=False)
print(f"\nDataset saved to {output_path}")