
# College Student Record Management System

## 1. Project Overview

The College Student Record Management System is a desktop application developed using Python and PyQt6 as part of the Unit V assignment, Exploring GUI Frameworks.

The application is designed to manage college student records through a simple graphical user interface. It allows users to add, view, search, update and delete student information.

This project demonstrates the use of GUI widgets, layout managers, event handling, input validation, message boxes, styling and file handling in Python.

## 2. Project Objectives

The main objectives of this project are:

- To develop a working desktop application using PyQt6.
- To apply basic concepts of graphical user interface development.
- To use different widgets and layouts to organise the interface.
- To handle user actions through signals and slots.
- To validate student information before saving.
- To store student records for future use.
- To separate the graphical interface from data management functions.

## 3. Main Features

### Add Student
Users can enter student details and add new records to the system. The application checks for missing information and duplicate student IDs.

### View Student Records
All saved student records are displayed in a table for easy viewing.

### Update Student
Users can select an existing record and modify student information.

### Delete Student
Users can delete student records after confirming the action.

### Search Student
The search feature allows users to find student records using information such as student ID, name, programme, year or semester.

### Input Validation
The application checks user input and displays appropriate messages when information is missing or invalid.

### Data Storage
Student records are stored in a JSON file. Saved information remains available when the application is closed and opened again.

## 4. Technologies Used

- Programming language: Python 3.10 or later
- GUI framework: PyQt6
- Data storage: JSON
- Development environment: Visual Studio Code
- Operating system used for development: Windows

## 5. GUI Frameworks Explored

As part of the Unit V assignment, different Python GUI frameworks were studied and compared.

The framework study covers:

1. PyQt6
2. PySide6
3. Tkinter
4. Kivy

Three simple Hello World applications were also developed using:

- Tkinter
- PyQt6
- Kivy

Each demonstration includes a graphical window, a message and a button that responds to user interaction.

PyQt6 was selected for the main application because it provides useful widgets, layout managers, signals and slots, and styling options for developing desktop applications.

## 6. Project Files

The project contains the following files:

- main.py
  Contains the main graphical user interface, including the student form, table, buttons, menus and event handling.

- student_data.py
  Contains functions for adding, updating, deleting, searching, saving and loading student records.

- college_students.json
  Stores the student information in JSON format.

- requirements.txt
  Lists the Python packages required to run the project.

- README.md
  Provides information about the project, installation and usage instructions.

- partA/hello_tkinter.py
  Demonstrates a simple GUI application using Tkinter.

- partA/hello_pyqt6.py
  Demonstrates a simple GUI application using PyQt6.

- partA/hello_kivy.py
  Demonstrates a simple GUI application using Kivy.

## 7. System Requirements

The following software is required:

- Python 3.10 or later
- Visual Studio Code or another Python editor
- PyQt6
- Kivy for the Kivy demonstration
- A computer that supports Python desktop applications

Tkinter is included with most standard Python installations.

## 8. Installation Instructions

### Step 1: Install Python

Install Python 3.10 or later and ensure Python is available from the terminal.

Check the installed version using:

    python --version

### Step 2: Open the Project

Extract the submitted ZIP file and open the project folder in Visual Studio Code.

### Step 3: Create a Virtual Environment

Open the VS Code terminal and run:

    python -m venv .venv

### Step 4: Activate the Virtual Environment

For Windows PowerShell, run:

    .\.venv\Scripts\Activate.ps1

### Step 5: Install Required Packages

Install the required Python packages using:

    python -m pip install -r requirements.txt

## 9. Running the Main Application

After installing the required packages, open the terminal in the project folder.

Run:

    python main.py

The College Student Record Management System window will open.

## 10. How to Use the Application

1. Open the application.
2. Enter the student ID and name.
3. Select the programme, year and semester.
4. Enter the student's marks.
5. Tick the confirmation checkbox.
6. Click the Add button to save the record.
7. Select a record from the table to update or delete it.
8. Use the search field to find a particular student.
9. Use the Clear button to reset the input fields.

The application displays messages to guide users when entering or managing student information.

## 11. Running the Hello World Demonstrations

The three demonstration programs are stored in the partA folder.

To run the Tkinter demonstration:

    python partA/hello_tkinter.py

To run the PyQt6 demonstration:

    python partA/hello_pyqt6.py

To run the Kivy demonstration:

    python partA/hello_kivy.py

Each program demonstrates basic GUI components and button event handling.

## 12. Data Management

The application uses a JSON file named college_students.json to store student records.

Each student record contains:

- Student ID
- Student name
- Programme
- Year
- Semester
- Marks

The application reads existing records when it starts and saves changes made through the system.

The JSON file is included with the project so that sample records can be viewed during testing.

## 13. Testing

The application was tested to check its main functions.

The tests included:

- Opening the application
- Adding a valid student record
- Preventing duplicate student IDs
- Checking missing student information
- Checking invalid semester information
- Searching for student records
- Updating existing records
- Deleting records with confirmation
- Saving student information
- Loading saved records after restarting the application

The detailed test cases and results are presented in the assignment report.

## 14. Project Structure

The project separates the user interface from the data management functions.

The main.py file manages the graphical interface and user interactions.

The student_data.py file handles student record operations and JSON file management.

This separation makes the program easier to understand, maintain and modify.

## 15. Limitations

The current application is intended for basic student record management on a local computer.

It uses a JSON file rather than an online database and does not include user accounts or online access.

## 16. Conclusion

The College Student Record Management System demonstrates the practical use of Python and PyQt6 in developing a desktop application.

Through this project, I gained experience in creating graphical interfaces, connecting buttons to functions, validating user input, organising code and storing data.

The project also helped me understand the differences between Python GUI frameworks and how to select a suitable framework for a particular application.
