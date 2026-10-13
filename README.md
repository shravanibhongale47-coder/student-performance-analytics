# Student Performance Analytics System

A beginner-friendly Python data-analysis project built for the EWB Courses Python with AI assignment.

## Technologies
- Python
- Pandas
- NumPy
- Matplotlib

## Features
- Loads student records from CSV using Pandas
- Calculates total and average marks for four subjects
- Assigns grades using a defined rule
- Determines pass/fail status
- Reports class average, highest/lowest average, pass count and pass percentage
- Identifies the top five students
- Compares subject averages
- Saves three charts: subject averages, grade distribution, and attendance vs average marks
- Exports processed results to CSV

## Dataset
The sample dataset has 30 fictional student records. Marks and attendance are illustrative, not real student information.

## Grading rule
- A: average >= 90
- B: average >= 80 and < 90
- C: average >= 70 and < 80
- D: average >= 60 and < 70
- F: average < 60

A student passes when they score at least 35 marks in every subject.

## Run the project
1. Install Python 3.
2. Open a terminal in this project folder.
3. Install dependencies:
   `python -m pip install pandas numpy matplotlib`
4. Run:
   `python main.py`

The program saves processed data and chart images inside the `outputs` folder.

## Project files
- `main.py` — main program and chart creation
- `functions.py` — reusable calculations
- `data/students.csv` — sample dataset
- `outputs/` — generated results and charts after running
- `README.md` — project documentation


