
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("college_students.json")


def load_students():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        students = json.load(file)

    if not isinstance(students, list):
        raise ValueError("Invalid student data format.")

    required = {
        "id", "name", "programme",
        "year", "semester", "marks"
    }

    for student in students:
        if (
            not isinstance(student, dict)
            or not required.issubset(student)
        ):
            raise ValueError("A student record is incomplete.")

    return students


def save_students(students):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            students,
            file,
            indent=4,
            ensure_ascii=False
        )


def add_student(students, new_student):
    if any(s["id"] == new_student["id"] for s in students):
        raise ValueError("Student ID already exists.")

    updated = students.copy()
    updated.append(new_student)
    save_students(updated)
    return updated


def update_student(students, selected_id, new_student):
    if any(
        s["id"] == new_student["id"]
        and s["id"] != selected_id
        for s in students
    ):
        raise ValueError("Another student already uses this ID.")

    updated = students.copy()

    for index, student in enumerate(updated):
        if student["id"] == selected_id:
            updated[index] = new_student
            save_students(updated)
            return updated

    raise ValueError("Student record not found.")


def delete_student(students, student_id):
    updated = [
        s for s in students
        if s["id"] != student_id
    ]

    if len(updated) == len(students):
        raise ValueError("Student record not found.")

    save_students(updated)
    return updated


def search_students(students, keyword):
    keyword = keyword.lower().strip()

    return [
        student for student in students
        if any(
            keyword in str(student[field]).lower()
            for field in (
                "id", "name", "programme",
                "year", "semester"
            )
        )
    ]
