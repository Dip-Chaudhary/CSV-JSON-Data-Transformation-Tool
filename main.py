
import argparse
import logging
import os

import pandas as pd

from config import PROJECT_NAME, OUTPUT_FOLDER
from data_cleaner import clean_data
from data_processor import StudentProcessor
from data_validator import validate_dataframe
from file_reader import (
    read_csv_file,
    read_json_file,
    read_multiple_files
)


def main():

    # Create command-line argument parser
    parser = argparse.ArgumentParser(
        description="CSV JSON Data Transformation Tool"
    )

    # CSV input path
    parser.add_argument(
        "--csv",
        default="data/students.csv",
        help="Path of CSV input file"
    )

    # JSON input path
    parser.add_argument(
        "--json",
        default="data/students.json",
        help="Path of JSON input file"
    )

    # Minimum marks filter
    parser.add_argument(
        "--minimum-marks",
        type=float,
        default=85,
        help="Minimum marks for filtering students"
    )

    # Output format selection
    parser.add_argument(
        "--output-format",
        choices=["csv", "json", "both"],
        default="both",
        help="Select output format: csv, json or both"
    )

    # Multiple input files
    parser.add_argument(
        "--files",
        nargs="+",
        help="Paths of multiple CSV and JSON input files"
    )

    args = parser.parse_args()

    try:
        print("Project:", PROJECT_NAME)

        # Initialize data variables
        cleaned_data = None
        json_data = None

        # Read multiple files if provided
        if args.files:
            data = read_multiple_files(args.files)

        else:
            # Read single CSV file
            data = read_csv_file(args.csv)

        if data is not None:

            # Clean data
            cleaned_data = clean_data(data)

            # Validate data
            validate_dataframe(cleaned_data)

            print("\nData validation successful!")

            # Create object
            processor = StudentProcessor(cleaned_data)

            # Calculate student grades
            processor.calculate_grade()

            # Calculate average
            average = processor.calculate_average()

            # Calculate aggregation values
            total_students = processor.count_students()
            total_marks = processor.calculate_total_marks()
            minimum_marks = processor.find_minimum_marks()
            maximum_marks = processor.find_maximum_marks()

            # Find topper
            topper = processor.find_topper()

            # Filter students
            filtered_students = processor.filter_students(
                args.minimum_marks
            )

            # Sort students by marks
            sorted_students = processor.sort_students()

            # Group students by city
            grouped_students = processor.group_students_by_city()

            print("\nStudent Data:")
            print(cleaned_data)

            print("\nAverage Marks:", average)

            print("\nTotal Students:", total_students)
            print("Total Marks:", total_marks)
            print("Minimum Marks:", minimum_marks)
            print("Maximum Marks:", maximum_marks)

            print("\nTopper:")
            print(topper)

            # Display filtered students
            print("\nFiltered Students:")
            print(filtered_students)

            # Display sorted students
            print("\nStudents Sorted by Marks (Highest to Lowest):")
            print(sorted_students)

            # Display students grouped by city
            print("\nStudents Grouped by City:")

            for city, students in grouped_students:
                print("\nCity:", city)
                print(students)

            # Save cleaned data
            processor.save_output(
                os.path.join(
                    OUTPUT_FOLDER,
                    "cleaned_students.csv"
                )
            )

            # Generate summary report
            summary_report = processor.generate_summary_report()

            # Save summary report
            report_path = os.path.join(
                OUTPUT_FOLDER,
                "student_summary.txt"
            )

            with open(
                report_path,
                "w",
                encoding="utf-8"
            ) as file:
                file.write(summary_report)

            print("\nSummary report saved successfully!")

        # Read separate JSON file only in normal mode
        if not args.files:

            json_data = read_json_file(args.json)

            if json_data is not None:

                # Clean JSON data
                json_data = clean_data(json_data)

                # Validate JSON data
                validate_dataframe(json_data)

                # Calculate grades for JSON data
                json_processor = StudentProcessor(json_data)
                json_processor.calculate_grade()

                print("\nJSON data validation successful!")

                print("\nStudent Data from JSON:")
                print(json_data)

        # Combine available datasets
        datasets = [
            dataset
            for dataset in [cleaned_data, json_data]
            if dataset is not None
        ]

        if datasets:

            merged_data = pd.concat(
                datasets,
                ignore_index=True
            )

            # Remove duplicate rows
            merged_data = merged_data.drop_duplicates()

            print("\nMerged Student Data:")
            print(merged_data)

            # Save output based on selected format

            if args.output_format in ["csv", "both"]:

                merged_data.to_csv(
                    os.path.join(
                        OUTPUT_FOLDER,
                        "merged_students.csv"
                    ),
                    index=False
                )

                print("\nMerged CSV data saved successfully!")

            if args.output_format in ["json", "both"]:

                merged_data.to_json(
                    os.path.join(
                        OUTPUT_FOLDER,
                        "merged_students.json"
                    ),
                    orient="records",
                    indent=4
                )

                print("Merged JSON data saved successfully!")

    except Exception:
        logging.exception(
            "An error occurred while running the project"
        )

        print(
            "An unexpected error occurred. "
            "Check output/project.log"
        )


if __name__ == "__main__":
    main()
