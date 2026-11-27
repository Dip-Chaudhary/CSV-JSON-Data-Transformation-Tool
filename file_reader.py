
import pandas as pd
import json
import logging
import os

# Create output folder if it does not exist
os.makedirs("output", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="output/project.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


def read_csv_file(file_path):
    try:
        data = pd.read_csv(file_path)
        logging.info("CSV file read successfully: %s", file_path)
        return data

    except FileNotFoundError:
        logging.error("CSV file not found: %s", file_path)
        print("Error: CSV file not found!")

    except PermissionError:
        logging.error("Permission denied for CSV file: %s", file_path)
        print("Error: Permission denied!")

    except pd.errors.EmptyDataError:
        logging.error("CSV file is empty: %s", file_path)
        print("Error: CSV file is empty!")

    except pd.errors.ParserError as e:
        logging.error("Invalid CSV format: %s", e)
        print("Error: Invalid CSV format!")

    except UnicodeDecodeError:
        logging.error("CSV encoding error: %s", file_path)
        print("Error: Unable to read CSV encoding!")

    except OSError as e:
        logging.error("CSV file system error: %s", e)
        print("Error: Unable to access CSV file!")

    except Exception:
        logging.exception("Unexpected CSV reading error: %s", file_path)
        print("Error: Unexpected problem while reading CSV!")

    return None


def read_json_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        result = pd.DataFrame(data)
        logging.info("JSON file read successfully: %s", file_path)
        return result

    except FileNotFoundError:
        logging.error("JSON file not found: %s", file_path)
        print("Error: JSON file not found!")

    except PermissionError:
        logging.error("Permission denied for JSON file: %s", file_path)
        print("Error: Permission denied!")

    except json.JSONDecodeError as e:
        logging.error("Invalid JSON format: %s", e)
        print("Error: Invalid JSON format!")

    except UnicodeDecodeError:
        logging.error("JSON encoding error: %s", file_path)
        print("Error: Unable to read JSON encoding!")

    except ValueError as e:
        logging.error("Invalid JSON data structure: %s", e)
        print("Error: Invalid JSON data structure!")

    except OSError as e:
        logging.error("JSON file system error: %s", e)
        print("Error: Unable to access JSON file!")

    except Exception:
        logging.exception("Unexpected JSON reading error: %s", file_path)
        print("Error: Unexpected problem while reading JSON!")

    return None


# Read multiple CSV and JSON files
def read_multiple_files(file_paths):

    if not file_paths:
        logging.warning("No input files provided!")
        print("Error: No input files provided!")
        return None

    all_data = []

    for file_path in file_paths:

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".csv":
            data = read_csv_file(file_path)

        elif extension == ".json":
            data = read_json_file(file_path)

        else:
            logging.warning("Unsupported file format: %s", file_path)
            print("Unsupported file format:", file_path)
            continue

        if data is not None:
            all_data.append(data)

    if not all_data:
        logging.warning("No valid files were found!")
        return None

    # Combine all files into one DataFrame
    combined_data = pd.concat(
        all_data,
        ignore_index=True
    )

    return combined_data
