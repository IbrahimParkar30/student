import pytest
from student_grades import StudentGrades

def test_add_grade():
    student = StudentGrades("John Doe")
    student.add_grade(90)
    student.add_grade(80)
    assert student.get_grades() == [90, 80]

def test_get_average():
    student = StudentGrades("Jane Doe")
    student.add_grade(85)
    student.add_grade(95)
    student.add_grade(75)
    assert student.get_average() == 85

def test_get_grades():
    student = StudentGrades("Mark Smith")
    student.add_grade(88)
    student.add_grade(92)
    assert student.get_grades() == [88, 92]

def test_display_grades(capsys):
    student = StudentGrades("Alice Brown")
    student.add_grade(78)
    student.add_grade(85)
    student.display_grades()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Grades for Alice Brown: 78, 85"

def test_empty_grades():
    student = StudentGrades("Tom Lee")
    assert student.get_average() == 0
    assert student.get_grades() == []
