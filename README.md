Practical Programming Assignment

Introduction to Programming IY499

Student Id: P444218
Student Name: Bora Bayrakci
Tutor: Marzieh Farahani

Table of Contents

	Introduction	1
	Requirements	2
	Design Flowchart Diagram	3
	Appendix A (Code listing)	8
	Appendix B (ReadMe file)	12

Introduction

The Grouped Data Analysis program is a Python application designed to help users input a series of continuous numerical data values and analyze them by grouping them into equal-width classes. The program guides users through data input, performs frequency grouping, calculates key descriptive statistics (mean, median, mode, variance, standard deviation), and visualizes the data as a histogram. Results are saved in CSV format for persistence and further analysis.

This application incorporates fundamental programming concepts, including structured programming (through modular functions), robust user input validation, and error handling. It also demonstrates use of Python’s standard and external libraries (`statistics`, `pandas`, `numpy`, and `matplotlib`) to carry out data manipulation and visualization tasks.

Requirements

Functional requirements of the program include:

- **User Data Input:** The user is prompted to enter continuous numeric values (e.g., scores or measurements).
- **Saving Data to CSV:** User-entered data is saved into a file named `data.csv`.
- **Loading Data from CSV:** Users can reload data from `data.csv` for future analysis.
- **Grouping Data into Classes:** Data is grouped into intervals based on a user-defined class width. The program validates that this width is a positive number.
- **Visual Histogram:** A histogram is generated from the grouped data and displayed using matplotlib.
- **Descriptive Statistics:** The program computes and displays the mean, median, mode(s), modal class, variance, and standard deviation.

Enhancements implemented:

- The filename `raw_data.csv` was corrected to `data.csv` throughout the code and documentation.
- Input validation for class width was added.
- Error messages for missing `data.csv` were improved to be user-friendly.

Appendix B (ReadMe file)

Identifying Information:
Name: Bora Bayrakci  
Student ID (P-Number): P444218  
Course: Introduction to Programming (IY499)  
GitHub Repository: https://github.com/borabek/IY499-Python-Project  

Declaration of Own Work:
I hereby declare that this assignment submission is my own work and has not been plagiarized. All code and content have been written by me, and any sources used (if any) have been properly cited. This work complies with the university’s academic integrity policies.

Project Description:
This Python program performs Grouped Data Analysis. Users input numeric data manually or load it from a CSV file (`data.csv`). The program groups the data into intervals of equal width, computes descriptive statistics (mean, median, mode, modal class, variance, standard deviation), displays a frequency distribution table, and draws a histogram of the results.

Key functionalities:
- Menu-driven interface
- File persistence using CSV
- Data grouping via numpy
- Descriptive statistics with the statistics module
- Histogram visualization with matplotlib

Required Libraries:
- `pandas` – for reading and writing CSVs.
- `numpy` – for generating bin ranges and histogram data.
- `matplotlib` – for visualizing data.
- `statistics` – for computing descriptive statistics.

Installation & Execution Instructions:

**Prerequisites:** Python 3.x

**Install libraries:**
```bash
pip install pandas numpy matplotlib
```

(The statistics module is part of Python’s standard library.)

**To run the program:**
```bash
python dataCollector.py
```

**Using the Program:**
- Choose “1. Enter Data” to input a new dataset manually.
- Or choose “2. Load Data from CSV” to reuse saved data.
- Enter a class width (must be a positive number).
- View the frequency table and statistics.
- A histogram is also displayed.
- Files saved: `data.csv`, `grouped_data.csv`, `statistics.csv`

**Troubleshooting:**
- If `data.csv` is missing, the program shows a clear error and suggests entering data manually first.
- Ensure class width is a valid positive number to avoid errors.

---

This update aligns both code and documentation with the requirements, increases robustness, and improves user experience.
