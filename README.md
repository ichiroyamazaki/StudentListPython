# StudentListPython

**StudentListPython** is a simple Python console application that demonstrates how to manage student records using a dictionary. It collects student numbers and first names, displays the student list, removes a record, and allows the user to add their own student information.

This project is intended for beginners learning Python dictionaries, user input, loops, and basic data management.

## Features

- Collects three student records.
- Stores student numbers as dictionary keys.
- Stores student first names as dictionary values.
- Displays the student list.
- Removes a student record using the `pop()` method.
- Accepts the user's student number and first name.
- Adds the user's information to the dictionary.
- Displays the updated student list.

## Requirements

- Python 3
- A Python-compatible IDE or code editor, or a terminal

## Project Structure

```text
StudentListPython/
├── student_list.py
└── README.md
```

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/ichiroyamazaki/StudentListPython.git
```

### 2. Open the Project Directory

```bash
cd StudentListPython
```

### 3. Run the Program

```bash
python student_list.py
```

Depending on your system, you may need to use:

```bash
python3 student_list.py
```

## How It Works

1. The program creates an empty dictionary named `students`.
2. It asks the user to enter three student numbers and first names.
3. Each student number is used as a dictionary key, with the corresponding first name as its value.
4. The program displays the collected student records.
5. It removes the last entered student record using `students.pop(id)`.
6. The program asks the user to enter their own student number and first name.
7. It adds the new record and displays the updated list.

## Example

```text
Enter student number 1: 1001
Enter first name 1: Alex
Enter student number 2: 1002
Enter first name 2: Jamie
Enter student number 3: 1003
Enter first name 3: Taylor

Student List:
1001 Alex
1002 Jamie
1003 Taylor

Enter your student number: 1004
Enter your first name: Chris

Student List:
1001 Alex
1002 Jamie
1004 Chris
```

In this example, the third record is removed before the new record is added. The displayed result therefore contains the first two original records and the new record.

## Concepts Demonstrated

- **Dictionaries:** Store student numbers and first names as key-value pairs.
- **Loops:** Collect multiple records and display dictionary contents.
- **User Input:** Uses `input()` to collect student details.
- **Dictionary Assignment:** Adds or updates a record using `students[id] = name`.
- **Dictionary Removal:** Uses `students.pop(id)` to remove a record.
- **Formatted Strings:** Uses f-strings to display numbered input prompts.

## Limitations

- The program collects a fixed number of three initial student records.
- It stores only student numbers and first names.
- Data is stored in memory and is not saved after the program exits.
- If a student number is repeated, the existing dictionary entry is overwritten.
- The program removes the last entered student record rather than asking which record to delete.
- Input validation is not implemented.

## Author

**Ichiro Yamazaki**

## License

No license is specified in this repository. Check the repository for licensing information before redistributing or modifying the project.
