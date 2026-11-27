
import os

from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


# Project configuration settings
PROJECT_NAME = os.getenv(
    "PROJECT_NAME",
    "CSV JSON Data Transformation Tool"
)

OUTPUT_FOLDER = os.getenv(
    "OUTPUT_FOLDER",
    "output"
)
