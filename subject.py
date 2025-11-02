class Subject:
    def __init__(self, subject_name: str, pre_exam: int, exam: int):
        self.subject_name = subject_name
        self.pre_exam = pre_exam
        self.exam = exam
        self.final_point = 0
        self.gpa = 0.0
        self.letter_grade = ""
        self.calculate_final_points()
        self.calculate_gpa_letter()

    def calculate_final_points(self):
        self.final_point = self.pre_exam + self.exam

    def calculate_gpa_letter(self):
        if 90 < self.final_point <= 100:
            self.gpa = 4.0
            self.letter_grade = "A"
        elif 80 < self.final_point <= 90:
            self.gpa = 3.5
            self.letter_grade = "B"
        elif 70 < self.final_point <= 80:
            self.gpa = 3.0
            self.letter_grade = "C"
        elif 60 < self.final_point <= 70:
            self.gpa = 2.5
            self.letter_grade = "D"
        elif 50 < self.final_point <= 60:
            self.gpa = 1.5
            self.letter_grade = "F"
        else:
            self.gpa = 0.0
            self.letter_grade = "F"

    def __str__(self):
        return f"{self.subject_name} Final point: {self.final_point}, GPA: {self.gpa}, Grade: {self.letter_grade}"
