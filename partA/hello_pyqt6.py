
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QMessageBox
)

from PyQt6.QtCore import Qt


class HelloWorldApp(QWidget):

    def __init__(self):
        super().__init__()

        # Main window
        self.setWindowTitle("PyQt6 - Karma Yangchen")
        self.resize(500, 350)

        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Main heading
        heading = QLabel("Hello World!")
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)

        heading.setStyleSheet("""
            color: #4169E1;
            font-size: 26px;
            font-weight: bold;
        """)

        # Welcome message
        message = QLabel("My First PyQt6 GUI Application")
        message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Interactive button
        button = QPushButton("Click Me")
        button.clicked.connect(self.show_message)

        button.setStyleSheet("""
            QPushButton {
                background-color: #4169E1;
                color: white;
                padding: 12px;
                border-radius: 6px;
                font-size: 14px;
            }

            QPushButton:hover {
                background-color: #3154C8;
            }
        """)

        # Student information
        student_info = QLabel(
            "Karma Yangchen | Student ID: 08230137\n"
            "IT A | Roll No: 6"
        )

        student_info.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        student_info.setStyleSheet("""
            color: #263238;
            font-size: 12px;
        """)

        # Add widgets to layout
        layout.addWidget(heading)
        layout.addWidget(message)
        layout.addWidget(button)
        layout.addWidget(student_info)

        self.setLayout(layout)

    # Function to handle button click
    def show_message(self):
        QMessageBox.information(
            self,
            "Welcome",
            "Hello! Welcome to PyQt6."
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = HelloWorldApp()
    window.show()

    sys.exit(app.exec())
