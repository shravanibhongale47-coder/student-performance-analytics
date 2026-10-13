"""Student Performance Analytics System."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from functions import SUBJECTS, calculate_student_results, get_summary

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "students.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def create_charts(results):
    # 1. Average marks by subject
    subject_averages = results[SUBJECTS].mean().sort_values(ascending=False)
    plt.figure(figsize=(9, 5))
    subject_averages.plot(kind="bar")
    plt.title("Average Marks by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Marks (out of 100)")
    plt.ylim(0, 100)
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "subject_averages.png", dpi=150)
    plt.close()

    # 2. Grade distribution
    grade_order = ["A", "B", "C", "D", "F"]
    grade_counts = results["Grade"].value_counts().reindex(grade_order, fill_value=0)
    plt.figure(figsize=(7, 5))
    grade_counts.plot(kind="bar")
    plt.title("Student Grade Distribution")
    plt.xlabel("Grade")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "grade_distribution.png", dpi=150)
    plt.close()

    # 3. Attendance versus average marks
    plt.figure(figsize=(8, 5))
    plt.scatter(results["Attendance_Percent"], results["Average_Marks"])
    plt.title("Attendance vs Average Marks")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Average Marks")
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "attendance_vs_marks.png", dpi=150)
    plt.close()

def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    students = pd.read_csv(DATA_PATH)
    print("\n=== DATASET OVERVIEW ===")
    print(f"Rows: {students.shape[0]} | Columns: {students.shape[1]}")
    print(students.head())
    print("\nMissing values by column:\n", students.isnull().sum())

    results = calculate_student_results(students)
    summary = get_summary(results)

    print("\n=== CLASS SUMMARY ===")
    for key, value in summary.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

    print("\n=== TOP 5 STUDENTS ===")
    print(results.nlargest(5, "Average_Marks")[["Student_ID", "Name", "Average_Marks", "Grade"]].to_string(index=False))

    print("\n=== SUBJECT AVERAGES ===")
    print(results[SUBJECTS].mean().round(2).sort_values(ascending=False).to_string())

    print("\n=== RESULT COUNTS ===")
    print(results["Result"].value_counts().to_string())

    results.to_csv(OUTPUT_DIR / "student_analysis_results.csv", index=False)
    create_charts(results)
    print(f"\nProcessed results and charts saved in: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
