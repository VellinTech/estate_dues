
ESTATE UNION DUES TRACKER
=========================

DESCRIPTION
-----------

The Estate Union Dues Tracker is a Python package-based application
for managing residents and their monthly estate dues.

The system allows the chairman to:

1. Register residents
2. View the resident directory
3. Record monthly dues
4. View a resident's payment statement
5. Check residents with outstanding dues
6. Check residents who are fully paid up

The system stores information permanently so that data remains
available after the program is closed and opened again.


PROJECT STRUCTURE
-----------------

estate_dues_tracker/
|
|-- main.py
|-- README.txt
|
|-- estate_tracker/
|   |-- __init__.py
|   |-- registry.py
|   |-- dues.py
|   |-- database.py
|   |-- activity.py
|
|-- estate_data.json
|-- estate_activity.txt


MODULES
-------

main.py
-------
Contains the menu and coordinates the functions in the package.
It is the only file that should be run directly.

registry.py
-----------
Handles resident registration, resident IDs, searching for
residents, and retrieving the resident directory.

dues.py
-------
Handles monthly dues payments, payment history, outstanding
payments, and paid-up residents.

database.py
-----------
Handles permanent storage using JSON. It loads existing data,
creates empty records on the first run, saves changes, and
handles corrupted data safely.

activity.py
-----------
Maintains a plain-text activity diary. New activities are added
to the end of the file with a date and time.


DATA STORAGE
------------

The program stores permanent records in:

estate_data.json

The first time the program is run, the file may not exist.
The program automatically starts with empty records.

If the data file is corrupted or cannot be read, the program
reports the problem and starts safely with empty records.


ACTIVITY DIARY
--------------

The program records important activities in:

estate_activity.txt

The diary is a plain-text file that can be opened with Notepad
or another text editor.

New events are appended to the end of the file.


MONTHLY DUES
------------

The monthly estate dues are set to ₦5,000.

A resident who pays less than ₦5,000 for a month still has an
outstanding balance.

A resident who pays ₦5,000 or more is considered paid up for
that month.


IMPORT STYLES
-------------

The project demonstrates more than one Python import style.

For example, the registry module is imported as a module:

    from estate_tracker import registry

Specific functions are imported directly from other modules:

    from estate_tracker.database import load_data, save_data

The different styles make the source of functions clear while
also demonstrating Python package imports.


HOW TO RUN
----------

Open a terminal inside the estate_dues_tracker folder.

Run:

    python main.py


REQUIREMENTS
------------

Python 3 is required.

No external Python packages are required.

