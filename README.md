Identifying Information:
Name: Bora Byrakci
Student ID : P444218
Course: Introduction to Programming (IY499)
GitHub Repository: https://github.com/borabek/IY4101-OOP-Java-Project Declaration of Own Work:
I hereby declare that this assignment submission is my own work and has not been plagiarized. All code and content have been written by me, and any sources used (if any) have been properly cited. This work complies with the university’s academic integrity policies. Project Description:
This project is a Python program for Grouped Data Analysis, which allows users to input a collection of numerical data and analyze its distribution. The program groups the continuous data into classes of equal width (bins) as specified by the user, and then computes a set of descriptive statistics. After the user enters data (or loads existing data from a file), they are prompted to choose a class width for grouping. The program outputs a frequency distribution table that includes each class interval, the frequency of data points in that interval, and the midpoint of the interval. It also calculates key statistics such as the mean, median, mode, and identifies the modal class (the interval with the highest frequency), as well as variance and standard deviation of the dataset. Additionally, the program generates a histogram to visually represent the frequency distribution of the data. All results are displayed in the console for immediate feedback and saved to CSV files (data.csv for raw data, grouped_data.csv for the grouped frequency table, and statistics.csv for the summary statistics) for record-keeping or further analysis. The user interacts with the program through a simple text-based menu system, making it easy to enter new data, load existing data, view results, and exit the application. Required Libraries:
pandas – for handling data structures (DataFrames) and reading/writing CSV files.
NumPy – for numeric operations, specifically to create intervals and compute histograms.
matplotlib – for plotting the histogram of the grouped data.
statistics – (Python built-in module) for calculating mean, median, mode, variance, and standard deviation.
Installation & Execution Instructions:
Prerequisites: Ensure that Python 3.x is installed on your system. If not, download and install the latest version of Python from the official website.
Library Installation: Install the required libraries using pip. Open a terminal and run:
![image](https://github.com/user-attachments/assets/9364b5a0-35fd-45a4-bbfe-1784e92fe4a9)

pip install pandas numpy matplotlib
(The statistics module is included in Python’s standard library, so no separate installation is needed for it.)
Obtain the Program: Download or clone the repository containing the program. Make sure the file dataCollector.py is present, along with any accompanying files.
Running the Program: Navigate to the directory containing dataCollector.py in your terminal. Execute the program by running:
![image](https://github.com/user-attachments/assets/46983100-7dd0-4c79-a4a9-af4d1660cc06)

python dataCollector.py
This will launch the program and display the main menu.
Using the Program: Follow the on-screen menu prompts. Choose “1. Enter Data” to input a new dataset manually (the program will guide you to enter numbers separated by spaces or commas). Alternatively, if you have previously saved data, choose “2. Load Data from CSV” to import it from the data.csv file. After data is entered or loaded, input a desired class width when prompted. The program will then display the frequency distribution table and descriptive statistics. A histogram window will also appear showing the data distribution graphically.
Viewing Output Files: After running an analysis, you can find the output files in the same directory. Open data.csv to see the raw data you entered, grouped_data.csv to review the grouped frequency table, and statistics.csv to see the list of statistical measures computed. These files are saved automatically each time the program runs an analysis.
Exit: To exit the program, use the menu option “3. Exit”. The program will terminate, and you can close the terminal if done.
