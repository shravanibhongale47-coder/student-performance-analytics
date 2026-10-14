# Project Documentation: Student Performance Analytics System
Student Name = Shravani Vikram Bhongale
Mail Id = shravanibhongale47@gmail.com
Contact = 7498602353

## 1. Project Title
Student Performance Analytics System

## 2. Objective
To analyze student marks and attendance using Python and present clear summaries of academic performance.

## 3. Technologies Used
Python, Pandas, NumPy, Matplotlib.

## 4. Dataset Description
The project uses a sample CSV dataset with 30 fictional student records. Fields include Student ID, Name, Department, marks in four subjects, and Attendance Percentage.

## 5. Implementation
1. Read the CSV file with Pandas.
2. Inspect the row/column count, first rows, and missing values.
3. Calculate total marks and average marks across four subjects.
4. Assign grades using the grading thresholds described in README.md.
5. Mark a student Pass when each subject mark is at least 35; otherwise mark Fail.
6. Calculate class-level summary metrics and list the top five students.
7. Compare subject averages and save charts.
8. Export processed student results to a CSV file.

## 6. Key Features
- Total and average marks
- Grade assignment
- Pass/fail classification
- Class summary and pass percentage
- Top-five student listing
- Subject average comparison
- Grade distribution chart
- Attendance versus average marks scatter plot

## 7. Output / Screenshots
After running the program, add screenshots of:
- Terminal output showing class summary and top-five students
- `subject_averages.png`
- `grade_distribution.png`
- `attendance_vs_marks.png`

## 8. Final Outcome
The program turns raw student records into a structured performance summary and visual charts. Replace this paragraph with observations from your own run.

## 9. Challenges & Learning

During the development of the Student Performance Analytics System, I encountered a few challenges and learned how to solve them.

- **File Path Issues:** Initially, the program could not locate the `students.csv` dataset because it was stored in a different folder. I resolved this by identifying the correct file location and copying the dataset into the required `data` folder.
- **Python Execution:** I learned to run the Python program from the correct project directory using the terminal.
- **Library Usage:** I used Pandas to load and analyze the dataset and Matplotlib to create charts for visualizing student performance.
- **Calculating Statistics:** I learned how to calculate class averages, subject-wise averages, pass percentages, and identify the top-performing students.
- **Saving Visualizations:** I worked on saving the generated charts in the `outputs` folder and resolving file path issues.
- **Debugging:** By reading error messages and testing commands in PowerShell, I improved my ability to identify and resolve common Python execution and file management problems.
- **GitHub Version Control:** I learned how to initialize a Git repository, stage files, create commits, and push a project to GitHub.

This project improved my practical understanding of Python, data analysis, data visualization, debugging, and project documentation.

## 10. GitHub Repository

**Public Repository URL:**  
https://github.com/shravanibhongale47-coder/student-performance-analytics

The repository contains the Python source code, dataset, generated visualizations, and project documentation.
