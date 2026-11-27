
import pandas as pd
import pytest

from data_validator import validate_dataframe


@pytest.fixture
def valid_data():
    """Create valid student data for testing."""
    return pd.DataFrame({
        "Name": ["Amit", "Priya"],
        "Age": [23, 24],
        "City": ["Surat", "Baroda"],
        "Marks": [85, 90]
    })


# Test 1: Check valid student data
def test_valid_dataframe(valid_data):
    assert validate_dataframe(valid_data) is True


# Test 2: Check invalid data type
def test_invalid_data_type():
    with pytest.raises(TypeError):
        validate_dataframe(["Amit", "Priya"])


# Test 3: Check empty DataFrame
def test_empty_dataframe():
    data = pd.DataFrame(
        columns=["Name", "Age", "City", "Marks"]
    )

    with pytest.raises(ValueError):
        validate_dataframe(data)


# Test 4: Check missing required column
def test_missing_column():
    data = pd.DataFrame({
        "Name": ["Amit"],
        "Age": [23],
        "City": ["Surat"]
    })

    with pytest.raises(ValueError):
        validate_dataframe(data)


# Test 5: Check missing values
def test_missing_values(valid_data):
    valid_data.loc[0, "Marks"] = None

    with pytest.raises(ValueError):
        validate_dataframe(valid_data)


# Test 6: Check empty student name
def test_empty_student_name(valid_data):
    valid_data.loc[0, "Name"] = " "

    with pytest.raises(ValueError):
        validate_dataframe(valid_data)


# Test 7: Check empty city
def test_empty_city(valid_data):
    valid_data.loc[0, "City"] = " "

    with pytest.raises(ValueError):
        validate_dataframe(valid_data)


# Test 8: Check invalid age
def test_invalid_age(valid_data):
    valid_data["Age"] = valid_data["Age"].astype(object)
    valid_data.loc[0, "Age"] = "abc"

    with pytest.raises(ValueError):
        validate_dataframe(valid_data)


# Test 9: Check age greater than zero
def test_zero_age(valid_data):
    valid_data.loc[0, "Age"] = 0

    with pytest.raises(ValueError):
        validate_dataframe(valid_data)


# Test 10: Check invalid marks
def test_invalid_marks(valid_data):
    valid_data["Marks"] = valid_data["Marks"].astype(object)
    valid_data.loc[0, "Marks"] = "abc"

    with pytest.raises(ValueError):
        validate_dataframe(valid_data)


# Test 11: Check marks greater than 100
def test_marks_above_100(valid_data):
    valid_data.loc[0, "Marks"] = 105

    with pytest.raises(ValueError):
        validate_dataframe(valid_data)


# Test 12: Check negative marks
def test_negative_marks(valid_data):
    valid_data.loc[0, "Marks"] = -5

    with pytest.raises(ValueError):
        validate_dataframe(valid_data)
