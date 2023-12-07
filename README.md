# Application Setup Guide

## Requirements

- **Operating System:** Windows 10/11
- **Python:** 3.11.0
- **Python Packages:**
    - Flask 3.0.0 (if not installed, use command: `pip install flask`)
    - mysql-connector-python 8.2.0 (if not installed, use command: `pip install mysql-connector-python`)
    - requests `pip install requests`

## Steps

1. Open MySQL command line CLI and create a database named `mydb`.
2. Modify the details in the `Credentials.txt` file to match your database configuration, except for the database name.
3. Run `db.py` to seed the database with mock data. This is the first file that must be executed. Do not proceed without running it.
4. Run `server.py`: `python server.py`.
5. The default port of the server is set to 5000. If this port is unavailable, change the port number on line 4 in `server.py`.
6. If you have changed the port in the above step, update the value of the `PORT` variable in the following files at line number 4:
    - `retrieve.py`
    - `put.py`
    - `post.py`
    - `server.py`

## Viewing Books

- Run `retrieve.py` file: `python retrieve.py`.

## Adding a New Book

1. Open `post.py`.
2. Enter the book name on line 6.
3. Enter the author's name on line 7.
4. Enter the publication year on line 8.
5. Run `post.py`: `python post.py`.
6. Verify the addition by running the `retrieve.py` file.
7. An error will occur if you attempt to add a book that already exists.

## Updating an Existing Book

1. Open `put.py`.
2. Enter the book ID on line 6.
3. Enter the book name on line 7.
4. Enter the author's name on line 8.
5. Enter the publication year on line 9.
6. Run `put.py`: `python put.py`.
7. Verify the modification by running the `retrieve.py` file.
8. An error will occur if you try to modify a book that does not exist.

## Screenshots and Report

Please refer to the provided report that includes output screenshots for better understanding.
