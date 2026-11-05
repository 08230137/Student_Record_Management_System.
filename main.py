
import sys
import re
import student_data

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QSpinBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QGroupBox,
    QMessageBox,
    QCheckBox,
    QHeaderView,
    QScrollArea,
    QFrame,
    QAbstractItemView,
    QSizePolicy
)


class StudentManagementSystem(QMainWindow):

    def __init__(self):
        super().__init__()

        self.students = []
        self.selected_id = None

        self.setWindowTitle(
            "College Student Record Management System "
            "- Karma Yangchen | Roll No. 6"
        )

        self.resize(1150, 750)
        self.setMinimumSize(650, 450)

        self.create_interface()
        self.apply_style()
        self.load_students()

    # CREATE APPLICATION INTERFACE
    def create_interface(self):

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(
            QFrame.Shape.NoFrame
        )

        central_widget = QWidget()
        central_widget.setObjectName("contentWidget")

        self.scroll_area.setWidget(central_widget)
        self.setCentralWidget(self.scroll_area)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # MAIN TITLE - NO ANIMATION
        title = QLabel(
            "COLLEGE STUDENT RECORD MANAGEMENT SYSTEM"
        )
        title.setObjectName("mainTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setWordWrap(True)

        subtitle = QLabel(
            "Manage college student information "
            "and academic records"
        )
        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setWordWrap(True)

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        # STUDENT INFORMATION FORM
        form_group = QGroupBox("Student Information")
        form_layout = QGridLayout()
        form_layout.setSpacing(12)

        self.student_id = QLineEdit()
        self.student_id.setPlaceholderText(
            "Enter student ID (numbers only)"
        )

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText(
            "Enter student name (letters only)"
        )

        # PROGRAMME
        self.programme = QComboBox()
        self.programme.addItems([
            "Select Programme",
            "BEd IT",
            "BEd English/His",
            "BEd English/Geo",
            "BEd Bio/Chem",
            "BEd Phy/Math",
            "MEd English",
            "MEd Math"
        ])

        # YEAR - NUMBERS ONLY
        self.year = QComboBox()
        self.year.addItems([
            "Select Year",
            "1",
            "2",
            "3",
            "4"
        ])

        # SEMESTER
        self.semester = QComboBox()
        self.semester.addItems([
            "Select Semester",
            "Semester 1",
            "Semester 2",
            "Semester 3",
            "Semester 4",
            "Semester 5",
            "Semester 6",
            "Semester 7",
            "Semester 8"
        ])

        # MARKS
        self.marks = QSpinBox()
        self.marks.setRange(0, 100)
        self.marks.setSuffix(" / 100")

        # CONFIRMATION
        self.confirm_checkbox = QCheckBox(
            "I confirm that the student "
            "information is correct"
        )

        # ADD FORM WIDGETS
        form_layout.addWidget(
            QLabel("Student ID:"), 0, 0
        )
        form_layout.addWidget(
            self.student_id, 0, 1
        )

        form_layout.addWidget(
            QLabel("Student Name:"), 0, 2
        )
        form_layout.addWidget(
            self.student_name, 0, 3
        )

        form_layout.addWidget(
            QLabel("Programme:"), 1, 0
        )
        form_layout.addWidget(
            self.programme, 1, 1
        )

        form_layout.addWidget(
            QLabel("Year:"), 1, 2
        )
        form_layout.addWidget(
            self.year, 1, 3
        )

        form_layout.addWidget(
            QLabel("Semester:"), 2, 0
        )
        form_layout.addWidget(
            self.semester, 2, 1
        )

        form_layout.addWidget(
            QLabel("Marks:"), 2, 2
        )
        form_layout.addWidget(
            self.marks, 2, 3
        )

        form_layout.addWidget(
            self.confirm_checkbox, 3, 0, 1, 4
        )

        form_layout.setColumnStretch(1, 1)
        form_layout.setColumnStretch(3, 1)

        form_group.setLayout(form_layout)
        main_layout.addWidget(form_group)

        # ACTION BUTTONS
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        self.add_button = QPushButton("Add Student")
        self.update_button = QPushButton("Update Student")
        self.delete_button = QPushButton("Delete Student")
        self.clear_button = QPushButton("Clear Fields")

        self.delete_button.setObjectName("deleteButton")
        self.clear_button.setObjectName("clearButton")

        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.clear_button)

        main_layout.addLayout(button_layout)

        # SEARCH SECTION
        search_layout = QHBoxLayout()

        search_label = QLabel("Search Student:")

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(
            "Search by ID, name, programme, "
            "year or semester..."
        )

        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)

        main_layout.addLayout(search_layout)

        # STUDENT RECORDS TABLE
        table_title = QLabel("COLLEGE STUDENT RECORDS")
        table_title.setObjectName("sectionTitle")
        main_layout.addWidget(table_title)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setMinimumHeight(450)

        self.table.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )

        self.table.setHorizontalHeaderLabels([
            "Student ID",
            "Student Name",
            "Programme",
            "Year",
            "Semester",
            "Marks"
        ])

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        self.table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        self.table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        self.table.setAlternatingRowColors(True)

        main_layout.addWidget(self.table)

        # MENU BAR
        file_menu = self.menuBar().addMenu("File")

        save_action = file_menu.addAction("Save Records")
        exit_action = file_menu.addAction("Exit")

        help_menu = self.menuBar().addMenu("Help")
        about_action = help_menu.addAction("About System")

        self.statusBar().showMessage("System ready")

        # CONNECT BUTTONS AND EVENTS
        self.add_button.clicked.connect(self.add_student)
        self.update_button.clicked.connect(self.update_student)
        self.delete_button.clicked.connect(self.delete_student)
        self.clear_button.clicked.connect(self.clear_fields)

        self.search_input.textChanged.connect(
            self.display_students
        )

        self.table.cellClicked.connect(self.select_student)

        save_action.triggered.connect(
            lambda: self.save_students()
        )

        exit_action.triggered.connect(self.close)
        about_action.triggered.connect(self.show_about)

        # VALIDATE WHEN USER FINISHES ENTERING
        self.student_id.editingFinished.connect(
            self.validate_student_id
        )

        self.student_name.editingFinished.connect(
            self.validate_student_name
        )

        self.year.currentIndexChanged.connect(
            self.update_semester_options
        )

    # STUDENT ID VALIDATION
    def validate_student_id(self):

        student_id = self.student_id.text().strip()

        if not student_id:
            return False

        if not re.fullmatch(r"[0-9]+", student_id):

            QMessageBox.warning(
                self,
                "Invalid Student ID",
                "Student ID must contain numbers only.\n\n"
                "Example: 08230137"
            )

            return False

        return True

    # STUDENT NAME VALIDATION
    def validate_student_name(self):

        name = self.student_name.text().strip()

        if not name:
            return False

        # ACCEPT LETTERS AND SPACES
        if not all(
            character.isalpha() or character.isspace()
            for character in name
        ):

            QMessageBox.warning(
                self,
                "Invalid Student Name",
                "Student name must contain letters "
                "and spaces only.\n\n"
                "Numbers and special symbols are not allowed.\n\n"
                "Example: Karma Yangchen"
            )

            return False

        return True

    # UPDATE SEMESTER BASED ON YEAR
    def update_semester_options(self):

        year_number = self.year.currentIndex()

        self.semester.clear()
        self.semester.addItem("Select Semester")

        if year_number == 0:
            return

        first_semester = year_number * 2 - 1
        second_semester = year_number * 2

        self.semester.addItems([
            f"Semester {first_semester}",
            f"Semester {second_semester}"
        ])

    # VALIDATE ALL STUDENT INFORMATION
    def get_student_details(self):

        student_id = self.student_id.text().strip()
        name = self.student_name.text().strip()

        programme = self.programme.currentText()
        year = self.year.currentText()
        semester = self.semester.currentText()
        marks = self.marks.value()

        # CHECK STUDENT ID
        if not student_id:

            QMessageBox.warning(
                self,
                "Missing Student ID",
                "Please enter a student ID."
            )

            return None

        if not re.fullmatch(r"[0-9]+", student_id):

            QMessageBox.warning(
                self,
                "Invalid Student ID",
                "Student ID must contain numbers only."
            )

            return None

        # CHECK STUDENT NAME
        if not name:

            QMessageBox.warning(
                self,
                "Missing Student Name",
                "Please enter the student's name."
            )

            return None

        if not all(
            character.isalpha() or character.isspace()
            for character in name
        ):

            QMessageBox.warning(
                self,
                "Invalid Student Name",
                "Student name must contain letters "
                "and spaces only."
            )

            return None

        # CHECK PROGRAMME
        if self.programme.currentIndex() == 0:

            QMessageBox.warning(
                self,
                "Programme Required",
                "Please select a programme."
            )

            return None

        # CHECK YEAR
        if self.year.currentIndex() == 0:

            QMessageBox.warning(
                self,
                "Year Required",
                "Please select a year from 1 to 4."
            )

            return None

        year_number = int(year)

        if year_number not in [1, 2, 3, 4]:

            QMessageBox.warning(
                self,
                "Invalid Year",
                "Year must be a number from 1 to 4."
            )

            return None

        # CHECK SEMESTER
        if self.semester.currentIndex() == 0:

            QMessageBox.warning(
                self,
                "Semester Required",
                "Please select a semester."
            )

            return None

        valid_semesters = [
            f"Semester {year_number * 2 - 1}",
            f"Semester {year_number * 2}"
        ]

        if semester not in valid_semesters:

            QMessageBox.warning(
                self,
                "Invalid Semester",
                "The selected semester does not "
                "match the year of study."
            )

            return None

        # CHECK CONFIRMATION
        if not self.confirm_checkbox.isChecked():

            QMessageBox.warning(
                self,
                "Confirmation Required",
                "Please confirm that the student "
                "information is correct."
            )

            return None

        return {
            "id": student_id,
            "name": name,
            "programme": programme,
            "year": year,
            "semester": semester,
            "marks": marks
        }

    # ADD STUDENT
    def add_student(self):

        student = self.get_student_details()

        if student is None:
            return

        try:
            result = student_data.add_student(
                self.students, student
            )

            if result is not None:
                self.students = result

        except (ValueError, TypeError) as error:

            QMessageBox.warning(
                self,
                "Invalid Record",
                str(error)
            )
            return

        except OSError as error:

            QMessageBox.critical(
                self,
                "Save Error",
                str(error)
            )
            return

        self.display_students()
        self.clear_fields()

        QMessageBox.information(
            self,
            "Success",
            "Student record added successfully!"
        )

    # UPDATE STUDENT
    def update_student(self):

        if self.selected_id is None:

            QMessageBox.warning(
                self,
                "No Student Selected",
                "Please select a student from the table."
            )

            return

        student = self.get_student_details()

        if student is None:
            return

        try:
            result = student_data.update_student(
                self.students,
                self.selected_id,
                student
            )

            if result is not None:
                self.students = result

        except (ValueError, TypeError) as error:

            QMessageBox.warning(
                self,
                "Update Error",
                str(error)
            )
            return

        except OSError as error:

            QMessageBox.critical(
                self,
                "Save Error",
                str(error)
            )
            return

        self.display_students()
        self.clear_fields()

        QMessageBox.information(
            self,
            "Updated",
            "Student record updated successfully!"
        )

    # DELETE STUDENT
    def delete_student(self):

        if self.selected_id is None:

            QMessageBox.warning(
                self,
                "No Student Selected",
                "Please select a student to delete."
            )

            return

        answer = QMessageBox.question(
            self,
            "Confirm Deletion",
            "Are you sure you want to delete this student?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        if answer != QMessageBox.StandardButton.Yes:
            return

        try:
            result = student_data.delete_student(
                self.students,
                self.selected_id
            )

            if result is not None:
                self.students = result

        except (ValueError, TypeError) as error:

            QMessageBox.warning(
                self,
                "Delete Error",
                str(error)
            )
            return

        except OSError as error:

            QMessageBox.critical(
                self,
                "Save Error",
                str(error)
            )
            return

        self.display_students()
        self.clear_fields()

        QMessageBox.information(
            self,
            "Deleted",
            "Student record deleted successfully."
        )

    # DISPLAY AND SEARCH STUDENTS
    def display_students(self, *args):

        filtered_students = student_data.search_students(
            self.students,
            self.search_input.text()
        )

        self.table.setRowCount(len(filtered_students))

        for row, student in enumerate(filtered_students):

            values = [
                student["id"],
                student["name"],
                student["programme"],
                student["year"],
                student["semester"],
                student["marks"]
            ]

            for column, value in enumerate(values):

                item = QTableWidgetItem(str(value))

                item.setTextAlignment(
                    Qt.AlignmentFlag.AlignCenter
                )

                self.table.setItem(row, column, item)

        self.statusBar().showMessage(
            f"Showing {len(filtered_students)} of "
            f"{len(self.students)} student records"
        )

    # SELECT STUDENT FROM TABLE
    def select_student(self, row, column):

        item = self.table.item(row, 0)

        if item is None:
            return

        student_id = item.text()

        for student in self.students:

            if str(student["id"]) == student_id:

                self.selected_id = student["id"]

                self.student_id.setText(
                    str(student["id"])
                )

                self.student_name.setText(
                    student["name"]
                )

                self.programme.setCurrentText(
                    student["programme"]
                )

                # SUPPORT PREVIOUS YEAR FORMATS
                saved_year = str(student["year"])

                year_mapping = {
                    "1st Year": "1",
                    "2nd Year": "2",
                    "3rd Year": "3",
                    "4th Year": "4"
                }

                saved_year = year_mapping.get(
                    saved_year, saved_year
                )

                self.year.setCurrentText(saved_year)

                self.semester.setCurrentText(
                    student["semester"]
                )

                self.marks.setValue(
                    int(student["marks"])
                )

                self.confirm_checkbox.setChecked(False)
                break

    # CLEAR INPUT FIELDS
    def clear_fields(self):

        self.student_id.clear()
        self.student_name.clear()

        self.programme.setCurrentIndex(0)
        self.year.setCurrentIndex(0)
        self.semester.setCurrentIndex(0)

        self.marks.setValue(0)
        self.confirm_checkbox.setChecked(False)

        self.selected_id = None
        self.table.clearSelection()

    # SAVE STUDENT RECORDS
    def save_students(self, show_message=True):

        try:
            student_data.save_students(self.students)

            if show_message:

                QMessageBox.information(
                    self,
                    "Saved",
                    "Student records saved successfully."
                )

            return True

        except OSError as error:

            QMessageBox.critical(
                self,
                "Save Error",
                f"Unable to save records:\n{error}"
            )

            return False

    # LOAD STUDENT RECORDS
    def load_students(self):

        try:
            self.students = student_data.load_students()
            self.display_students()

        except (OSError, ValueError, TypeError) as error:

            QMessageBox.critical(
                self,
                "Load Error",
                f"Unable to load student records:\n{error}"
            )

    # ABOUT DIALOG
    def show_about(self):

        QMessageBox.information(
            self,
            "About System",
            "COLLEGE STUDENT RECORD MANAGEMENT SYSTEM\n\n"
            "Developed by: Karma Yangchen\n"
            "Student ID: 08230137\n"
            "Section: IT A\n"
            "Roll Number: 6\n\n"
            "Developed using Python and PyQt6\n"
            "Features:\n"
            "Add, Update, Delete, Search and Save Records"
        )

    # APPLICATION STYLING
    def apply_style(self):

        self.setStyleSheet("""
            QMainWindow {
                background-color: #FFFFFF;
            }

            QWidget {
                font-family: Arial;
                font-size: 13px;
                color: #263238;
            }

            QWidget#contentWidget {
                background-color: #FFFFFF;
            }

            QScrollArea {
                background-color: #FFFFFF;
                border: none;
            }

            QLabel#mainTitle {
                background-color: #4169E1;
                color: white;
                font-size: 22px;
                font-weight: bold;
                padding: 22px;
                border-radius: 8px;
                border-bottom: 5px solid #DC2626;
            }

            QLabel#subtitle {
                color: #4169E1;
                font-size: 13px;
                padding: 5px;
            }

            QLabel#sectionTitle {
                color: #4169E1;
                font-size: 16px;
                font-weight: bold;
                padding: 5px;
            }

            QGroupBox {
                background-color: white;
                border: 2px solid #4169E1;
                border-radius: 8px;
                margin-top: 15px;
                padding: 15px;
                font-weight: bold;
                color: #4169E1;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                left: 12px;
                padding: 0 5px;
                background-color: white;
            }

            QLineEdit, QComboBox, QSpinBox {
                background-color: white;
                border: 1px solid #B6C5F5;
                border-radius: 5px;
                padding: 9px;
                color: #263238;
            }

            QLineEdit:focus,
            QComboBox:focus,
            QSpinBox:focus {
                border: 2px solid #4169E1;
            }

            QPushButton {
                background-color: #4169E1;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 12px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #3154C8;
            }

            QPushButton:pressed {
                background-color: #2444A8;
            }

            QPushButton#deleteButton {
                background-color: #DC2626;
                color: white;
            }

            QPushButton#deleteButton:hover {
                background-color: #B91C1C;
            }

            QPushButton#clearButton {
                background-color: white;
                color: #4169E1;
                border: 2px solid #4169E1;
            }

            QPushButton#clearButton:hover {
                background-color: #EEF2FF;
            }

            QTableWidget {
                background-color: white;
                alternate-background-color: #EEF2FF;
                gridline-color: #D6DEFA;
                border: 1px solid #B6C5F5;
                border-radius: 5px;
                selection-background-color: #4169E1;
                selection-color: white;
            }

            QHeaderView::section {
                background-color: #4169E1;
                color: white;
                padding: 10px;
                font-weight: bold;
                border: 1px solid white;
            }

            QCheckBox {
                color: #4169E1;
                background-color: transparent;
            }

            QMenuBar {
                background-color: #4169E1;
                color: white;
                padding: 5px;
            }

            QMenuBar::item:selected {
                background-color: #3154C8;
            }

            QMenu {
                background-color: white;
                color: #263238;
            }

            QMenu::item:selected {
                background-color: #4169E1;
                color: white;
            }

            QStatusBar {
                background-color: #4169E1;
                color: white;
                padding: 4px;
            }

            QScrollBar:vertical {
                background-color: #EEF2FF;
                width: 14px;
                border: none;
            }

            QScrollBar::handle:vertical {
                background-color: #4169E1;
                border-radius: 5px;
                min-height: 30px;
            }

            QScrollBar::handle:vertical:hover {
                background-color: #3154C8;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)


# START APPLICATION
if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = StudentManagementSystem()
    window.show()

    sys.exit(app.exec())
