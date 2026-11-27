# CSV/JSON Data Transformation Tool

 1. Project Description

The CSV/JSON Data Transformation Tool is a Python-based application developed to read, clean, validate, process, and transform student data stored in CSV and JSON files.

The project uses Pandas to perform data operations such as removing duplicate records, handling missing values, calculating average marks, finding the topper, filtering students, and generating summary reports.

It also supports reading multiple files, merging datasets, and saving processed data in CSV and JSON formats.

 2. Features

 Read student data from CSV files.
 Read student data from JSON files.
 Read multiple CSV and JSON files.
 Remove duplicate records.
 Remove rows containing missing values.
 Validate student data and required columns.
 Calculate average and total marks.
 Find the highest and lowest marks.
 Identify the top-performing student.
 Filter students based on minimum marks.
 Sort students according to marks.
 Group students by city.
 Calculate student grades.
 Generate a student summary report.
 Merge CSV and JSON data.
 Save processed data in CSV and JSON formats.
 Handle errors using exception handling.
 Maintain logs for project activities.
 Use environment-based configuration.

 3. Technologies Used

 Python 3.10+
 Pandas
 JSON
 pytest
 python-dotenv

 4. Project Structure


CSV_JSON_Project
│
├── data
│   ├── students.csv
│   └── students.json
│
├── output
│   ├── cleaned_students.csv
│   ├── merged_students.csv
│   ├── merged_students.json
│   ├── student_summary.txt
│   └── project.log
│
├── tests
│   ├── test_data_processor.py
│   ├── test_data_validator.py
│   └── test_file_reader.py
│
├── main.py
├── file_reader.py
├── data_cleaner.py
├── data_processor.py
├── data_validator.py
├── config.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md


Note: Output files are generated when the project runs.

 5. Installation

Make sure Python 3.10 or later is installed.

Open the project folder in VS Code or PowerShell.

Install the required libraries:

bash
py -m pip install -r requirements.txt


Create a local .env file using the settings provided in .env.example.

 6. How to Run the Project

Run the main program:

bash
py main.py


To process specific CSV and JSON files:

bash
py main.py --files data/students.csv data/students.json


To filter students based on minimum marks:

bash
py main.py --minimum-marks 80


To select the output format:

bash
py main.py --output-format csv


Available output formats:

 csv
 json
 both

To see all available command-line options:

bash
py main.py --help


 7. How to Run Tests

Run the complete automated test suite:

bash
py -m pytest -v


The project contains 43 automated tests covering:

 Student data processing.
 Data validation.
 CSV file reading.
 JSON file reading.
 Multiple file reading.
 Error handling.
 Output file creation.
 Empty and invalid file handling.

All 43 automated tests passed successfully during the latest testing.

 8. Main Class

The project contains a class named StudentProcessor.

Important methods include:

 calculate_average() – Calculates average student marks.
 find_topper() – Finds the student with the highest marks.
 filter_students() – Filters students based on minimum marks.
 count_students() – Counts the total number of students.
 calculate_total_marks() – Calculates total marks.
 find_minimum_marks() – Finds the minimum marks.
 find_maximum_marks() – Finds the maximum marks.
 sort_students() – Sorts students according to marks.
 group_students_by_city() – Groups students by city.
 calculate_grade() – Calculates student grades.
 save_output() – Saves processed data into a CSV file.
 generate_summary_report() – Generates a student summary report.

 9. Error Handling and Logging

The project uses exception handling to manage errors such as:

 Missing files.
 Invalid CSV and JSON formats.
 Empty files.
 Permission-related errors.
 Invalid data structures.
 Unexpected file-reading errors.

Logging is used to record important project activities and errors in:

output/project.log

 10. Output

The project generates processed output files, including:

 cleaned_students.csv
 merged_students.csv
 merged_students.json
 student_summary.txt
 project.log


 11. Configuration

The project uses the python-dotenv library to load configuration settings from a local .env file.

The .env file contains project configuration values such as:

 Project name.
 Output folder.

The .gitignore file excludes the local .env file and unnecessary Python cache files from Git tracking.

An .env.example file is provided as a template for configuration.

 12. Conclusion

The CSV/JSON Data Transformation Tool demonstrates the use of Python programming, Pandas, file handling, data cleaning, validation, object-oriented programming, exception handling, logging, and automated testing.

It provides a simple and effective way to process student records from CSV and JSON files and generate useful reports and output files.