
import pandas as pd


def validate_dataframe(data):
    """
    Validate student DataFrame.

    Checks data type, empty data, required columns,
    missing values, numeric values, age, and marks.
    """

    # Check whether data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise TypeError(
            "Invalid data format. DataFrame required."
        )

    # Check empty data
    if data.empty:
        raise ValueError("Student data is empty!")

    # Check duplicate column names
    if data.columns.duplicated().any():
        raise ValueError("Duplicate column names found!")

    # Define required columns
    required_columns = [
        "Name",
        "Age",
        "City",
        "Marks"
    ]

    # Find missing columns
    missing_columns = [
        column
        for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Check missing values
    if data[required_columns].isnull().any().any():
        raise ValueError(
            "Missing values found in student data!"
        )

    # Check empty names and cities
    if data["Name"].astype(str).str.strip().eq("").any():
        raise ValueError("Student name cannot be empty!")

    if data["City"].astype(str).str.strip().eq("").any():
        raise ValueError("City cannot be empty!")

    # Convert Age and Marks into numeric values
    age = pd.to_numeric(
        data["Age"],
        errors="coerce"
    )

    marks = pd.to_numeric(
        data["Marks"],
        errors="coerce"
    )

    # Check numeric values
    if age.isnull().any():
        raise ValueError(
            "Age must contain numeric values!"
        )

    if marks.isnull().any():
        raise ValueError(
            "Marks must contain numeric values!"
        )

    # Check valid age
    if (age <= 0).any():
        raise ValueError(
            "Age must be greater than zero!"
        )

    # Check valid marks
    if ((marks < 0) | (marks > 100)).any():
        raise ValueError(
            "Marks must be between 0 and 100!"
        )

    return True
