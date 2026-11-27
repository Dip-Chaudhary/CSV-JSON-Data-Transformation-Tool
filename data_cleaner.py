
import pandas as pd


def clean_data(data):
    """
    Clean student data by removing extra spaces,
    converting numeric columns, and removing duplicates
    and missing values.
    """

    # Check if data is empty
    if data is None or data.empty:
        return data

    # Remove extra spaces from text columns
    text_columns = data.select_dtypes(
        include="object"
    ).columns

    for column in text_columns:
        data[column] = data[column].str.strip()

    # Convert Age and Marks into numeric values
    if "Age" in data.columns:
        data["Age"] = pd.to_numeric(
            data["Age"],
            errors="coerce"
        )

    if "Marks" in data.columns:
        data["Marks"] = pd.to_numeric(
            data["Marks"],
            errors="coerce"
        )

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Remove rows with missing values
    data = data.dropna()

    # Reset index
    data = data.reset_index(drop=True)

    return data
