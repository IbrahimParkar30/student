class StudentGrades:
    def __init__(self, student_name):
        self.student_name = student_name
        self.grades = []

    def add_grade(self, grade):
        """Add a grade to the student's grade list."""
        self.grades.append(grade)

    def get_average(self):
        """Calculate and return the average grade."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_grades(self):
        """Return the list of grades."""
        return self.grades

    def display_grades(self):
        """Display the grades in a formatted manner."""
        print(f"Grades for {self.student_name}: {', '.join(map(str, self.grades))}")
