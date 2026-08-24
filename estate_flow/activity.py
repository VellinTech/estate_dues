
from datetime import datetime
from pathlib import Path


ACTIVITY_FILE = Path("estate_activity.txt")


def log_activity(message):
    """Add a timestamped activity to the diary."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with ACTIVITY_FILE.open("a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] {message}\n")

    except OSError:
        print("WARNING: The activity diary could not be updated.")

