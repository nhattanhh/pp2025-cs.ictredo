import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.courses = {}

    def input_mark(self, course_id, mark, credit):
        rounded_mark = math.floor(mark * 10) / 10  
        self.marks[course_id] = rounded_mark
        self.courses[course_id] = credit

    def calculate_gpa(self):
        if not self.marks or not self.courses:
            return 0.0
        marks = np.array(list(self.marks.values()))
        credits = np.array([self.courses[course_id] for course_id in self.marks.keys()])
        weighted_sum = np.sum(marks * credits)
        total_credits = np.sum(credits)
        return weighted_sum / total_credits if total_credits > 0 else 0.0

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}, GPA: {self.calculate_gpa():.2f}"