
import logging
import os


class StudentProcessor:
    """Process and analyze student data."""

    def __init__(self, data):
        self.data = data

    def calculate_average(self):
        """Calculate average marks of students."""
        if self.data.empty:
            logging.error("Student data is empty!")
            raise ValueError("Student data is empty!")

        return self.data["Marks"].mean()

    def find_topper(self):
        """Find the student with the highest marks."""
        if self.data.empty:
            logging.error("Student data is empty!")
            raise ValueError("Student data is empty!")

        topper = self.data.loc[
            self.data["Marks"].idxmax()
        ]

        return topper

    def filter_students(self, minimum_marks):
        """Filter students according to minimum marks."""
        if self.data.empty:
            logging.error("Student data is empty!")
            raise ValueError("Student data is empty!")

        result = self.data[
            self.data["Marks"] >= minimum_marks
        ]

        return result

    def count_students(self):
        """Count total number of students."""
        return len(self.data)

    def calculate_total_marks(self):
        """Calculate total marks of all students."""
        return self.data["Marks"].sum()

    def find_minimum_marks(self):
        """Find minimum marks."""
        if self.data.empty:
            raise ValueError("Student data is empty!")

        return self.data["Marks"].min()

    def find_maximum_marks(self):
        """Find maximum marks."""
        if self.data.empty:
            raise ValueError("Student data is empty!")

        return self.data["Marks"].max()

    def sort_students(self, ascending=False):
        """Sort students according to marks."""
        if self.data.empty:
            raise ValueError("Student data is empty!")

        sorted_data = self.data.sort_values(
            by="Marks",
            ascending=ascending
        )

        return sorted_data

    def group_students_by_city(self):
        """Group students according to their city."""
        if self.data.empty:
            raise ValueError("Student data is empty!")

        grouped_data = self.data.groupby("City")

        return grouped_data

    def calculate_grade(self):
        """Calculate grades according to student marks."""
        if self.data.empty:
            raise ValueError("Student data is empty!")

        self.data["Grade"] = self.data["Marks"].apply(
            lambda marks:
                "A" if marks >= 90 else
                "B" if marks >= 80 else
                "C" if marks >= 70 else
                "D"
        )

        return self.data

    def save_output(self, file_path):
        """Save processed student data into a CSV file."""
        try:
            folder = os.path.dirname(file_path)

            if folder:
                os.makedirs(folder, exist_ok=True)

            self.data.to_csv(file_path, index=False)

            logging.info(
                "Output file saved: %s",
                file_path
            )

            print("Output file saved successfully!")

        except OSError:
            logging.exception(
                "Error saving output file: %s",
                file_path
            )

            print("Error saving output file!")

    def generate_summary_report(self):
        """Generate a summary report of student data."""
        if self.data.empty:
            raise ValueError("Student data is empty!")

        average = self.calculate_average()
        total_students = self.count_students()
        total_marks = self.calculate_total_marks()
        minimum_marks = self.find_minimum_marks()
        maximum_marks = self.find_maximum_marks()
        topper = self.find_topper()

        report = f"""
STUDENT DATA SUMMARY REPORT
---------------------------

Total Students: {total_students}
Total Marks: {total_marks}
Average Marks: {average:.2f}
Minimum Marks: {minimum_marks}
Maximum Marks: {maximum_marks}

TOPPER DETAILS
--------------
Name: {topper['Name']}
City: {topper['City']}
Marks: {topper['Marks']}
Grade: {topper['Grade']}
"""

        return report
