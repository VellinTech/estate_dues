
import json
from pathlib import Path


DATA_FILE = Path("estate_data.json")


def empty_data():
    """Return an empty estate record."""
    return {
        "next_id": 1,
        "residents": {},
        "payments": []
    }


def load_data():
    """Load saved estate records."""

    if not DATA_FILE.exists():
        return empty_data()

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("Invalid data format.")

        if "next_id" not in data:
            raise ValueError("Missing next_id.")

        if "residents" not in data:
            raise ValueError("Missing residents.")

        if "payments" not in data:
            raise ValueError("Missing payments.")

        return data

    except (json.JSONDecodeError, OSError, ValueError):
        print("\nWARNING: The saved estate data is corrupted or cannot be read.")
        print("The program will start with empty records.\n")

        return empty_data()


def save_data(data):
    """Save estate records to the JSON file."""

    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    except OSError:
        print("WARNING: The estate data could not be saved.")
