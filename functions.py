"""Reusable functions for the Student Performance Analytics System."""
import numpy as np
import pandas as pd

SUBJECTS = ["Mathematics", "Science", "English", "Computer_Science"]

def calculate_student_results(df):
    """Return a copy of the data with totals, averages, grades, and pass/fail."""
    result = df.copy()
    result["Total_Marks"] = result[SUBJECTS].sum(axis=1)
    result["Average_Marks"] = result[SUBJECTS].mean(axis=1).round(2)

    def assign_grade(average):
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    result["Grade"] = result["Average_Marks"].apply(assign_grade)
    # A student passes if they score at least 35 in every subject.
    result["Result"] = np.where((result[SUBJECTS] >= 35).all(axis=1), "Pass", "Fail")
    return result

def get_summary(df):
    """Calculate headline statistics from processed student data."""
    return {
        "student_count": int(len(df)),
        "class_average": round(float(df["Average_Marks"].mean()), 2),
        "highest_average": round(float(df["Average_Marks"].max()), 2),
        "lowest_average": round(float(df["Average_Marks"].min()), 2),
        "pass_count": int((df["Result"] == "Pass").sum()),
        "fail_count": int((df["Result"] == "Fail").sum()),
        "pass_percentage": round(float((df["Result"] == "Pass").mean() * 100), 2),
    }
