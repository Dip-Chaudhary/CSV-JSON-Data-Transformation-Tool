
import pandas as pd
import pytest

from data_processor import StudentProcessor


@pytest.fixture
def sample_data():
    """Create sample student data for testing."""
    return pd.DataFrame({
        "Name": ["Amit", "Priya", "Neha"],
        "Age": [23, 24, 22],
        "City": ["Baroda", "Surat", "Rajkot"],
        "Marks": [85, 90, 78]
    })


@pytest.fixture
def processor(sample_data):
    """Create StudentProcessor object for testing."""
    return StudentProcessor(sample_data)


# Test 1: Check class creation
def test_processor_creation(processor):
    assert isinstance(processor, StudentProcessor)


# Test 2: Check average marks
def test_calculate_average(processor):
    assert processor.calculate_average() == pytest.approx(
        84.33,
        rel=0.01
    )


# Test 3: Check topper name
def test_find_topper_name(processor):
    assert processor.find_topper()["Name"] == "Priya"


# Test 4: Check topper marks
def test_find_topper_marks(processor):
    assert processor.find_topper()["Marks"] == 90


# Test 5: Check filtering students
def test_filter_students(processor):
    result = processor.filter_students(85)

    assert len(result) == 2


# Test 6: Check filtered student names
def test_filter_student_names(processor):
    result = processor.filter_students(85)

    assert list(result["Name"]) == ["Amit", "Priya"]


# Test 7: Check filter with high marks
def test_filter_high_marks(processor):
    result = processor.filter_students(95)

    assert len(result) == 0


# Test 8: Check filter with low marks
def test_filter_low_marks(processor):
    result = processor.filter_students(70)

    assert len(result) == 3


# Test 9: Check CSV output creation
def test_save_output(processor, tmp_path):
    file_path = tmp_path / "students.csv"

    processor.save_output(str(file_path))

    assert file_path.exists()


# Test 10: Check saved CSV data
def test_saved_output_data(processor, tmp_path):
    file_path = tmp_path / "students.csv"

    processor.save_output(str(file_path))

    saved_data = pd.read_csv(file_path)

    assert len(saved_data) == 3


# Test 11: Check empty data average exception
def test_empty_data_average():
    empty_data = pd.DataFrame(
        columns=["Name", "Age", "City", "Marks"]
    )

    processor = StudentProcessor(empty_data)

    with pytest.raises(ValueError):
        processor.calculate_average()


# Test 12: Check empty data topper exception
def test_empty_data_topper():
    empty_data = pd.DataFrame(
        columns=["Name", "Age", "City", "Marks"]
    )

    processor = StudentProcessor(empty_data)

    with pytest.raises(ValueError):
        processor.find_topper()


# Test 13: Check total students
def test_count_students(processor):
    assert processor.count_students() == 3


# Test 14: Check total marks
def test_calculate_total_marks(processor):
    assert processor.calculate_total_marks() == 253


# Test 15: Check minimum marks
def test_find_minimum_marks(processor):
    assert processor.find_minimum_marks() == 78


# Test 16: Check maximum marks
def test_find_maximum_marks(processor):
    assert processor.find_maximum_marks() == 90


# Test 17: Check sorting students
def test_sort_students(processor):
    result = processor.sort_students()

    assert list(result["Marks"]) == [90, 85, 78]


# Test 18: Check grouping students by city
def test_group_students_by_city(processor):
    result = processor.group_students_by_city()

    assert len(result) == 3
    assert "Surat" in result.groups


# Test 19: Check grade calculation
def test_calculate_grade(processor):
    result = processor.calculate_grade()

    assert list(result["Grade"]) == ["B", "A", "C"]


# Test 20: Check summary report
def test_generate_summary_report(processor):
    processor.calculate_grade()

    report = processor.generate_summary_report()

    assert "STUDENT DATA SUMMARY REPORT" in report
    assert "Total Students: 3" in report
    assert "Name: Priya" in report
