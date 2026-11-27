
import json

import pandas as pd

from file_reader import (
    read_csv_file,
    read_json_file,
    read_multiple_files
)


# Test 1: Read multiple CSV and JSON files
def test_read_multiple_files():
    files = [
        "data/students.csv",
        "data/students.json"
    ]

    data = read_multiple_files(files)

    assert data is not None
    assert len(data) == 40
    assert "Name" in data.columns
    assert "Marks" in data.columns


# Test 2: Read CSV file successfully
def test_read_csv_file(tmp_path):
    file_path = tmp_path / "students.csv"

    data = pd.DataFrame({
        "Name": ["Amit"],
        "Age": [23],
        "City": ["Surat"],
        "Marks": [85]
    })

    data.to_csv(file_path, index=False)

    result = read_csv_file(str(file_path))

    assert result is not None
    assert len(result) == 1
    assert result.iloc[0]["Name"] == "Amit"


# Test 3: Check CSV file not found
def test_csv_file_not_found(tmp_path):
    file_path = tmp_path / "missing.csv"

    result = read_csv_file(str(file_path))

    assert result is None


# Test 4: Read JSON file successfully
def test_read_json_file(tmp_path):
    file_path = tmp_path / "students.json"

    data = [
        {
            "Name": "Priya",
            "Age": 24,
            "City": "Surat",
            "Marks": 90
        }
    ]

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file)

    result = read_json_file(str(file_path))

    assert result is not None
    assert len(result) == 1
    assert result.iloc[0]["Name"] == "Priya"


# Test 5: Check JSON file not found
def test_json_file_not_found(tmp_path):
    file_path = tmp_path / "missing.json"

    result = read_json_file(str(file_path))

    assert result is None


# Test 6: Check unsupported file format
def test_unsupported_file_format():
    result = read_multiple_files(["students.txt"])

    assert result is None


# Test 7: Read multiple CSV files
def test_multiple_csv_files(tmp_path):
    file1 = tmp_path / "students1.csv"
    file2 = tmp_path / "students2.csv"

    pd.DataFrame({
        "Name": ["Amit"],
        "Age": [23],
        "City": ["Surat"],
        "Marks": [85]
    }).to_csv(file1, index=False)

    pd.DataFrame({
        "Name": ["Priya"],
        "Age": [24],
        "City": ["Baroda"],
        "Marks": [90]
    }).to_csv(file2, index=False)

    result = read_multiple_files([
        str(file1),
        str(file2)
    ])

    assert result is not None
    assert len(result) == 2


# Test 8: Check combined column names
def test_combined_file_columns():
    files = [
        "data/students.csv",
        "data/students.json"
    ]

    result = read_multiple_files(files)

    assert list(result.columns) == [
        "Name", "Age", "City", "Marks"
    ]


# Test 9: Check empty CSV file
def test_empty_csv_file(tmp_path):
    file_path = tmp_path / "empty.csv"
    file_path.write_text("")

    result = read_csv_file(str(file_path))

    assert result is None


# Test 10: Check invalid JSON file
def test_invalid_json_file(tmp_path):
    file_path = tmp_path / "invalid.json"
    file_path.write_text("{invalid json}")

    result = read_json_file(str(file_path))

    assert result is None


# Test 11: Check empty file list
def test_read_multiple_files_empty_list():
    result = read_multiple_files([])

    assert result is None
