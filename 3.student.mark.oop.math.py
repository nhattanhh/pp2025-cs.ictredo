import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.credits = {}
        self.gpa = 0.0

    def input_mark(self, course_id, mark, credit):
        self.marks[course_id] = mark
        self.credits[course_id] = credit

    def calculate_gpa(self):
        if len(self.marks) == 0:
            self.gpa = 0.0
            return
        marks = np.array([self.marks[course] for course in self.marks])
        credits = np.array([self.credits[course] for course in self.credits])
        weighted_sum = np.sum(marks * credits)
        total_credits = np.sum(credits)
        self.gpa = math.floor((weighted_sum / total_credits) * 10) / 10 if total_credits > 0 else 0.0

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}, GPA: {self.gpa:.1f}"


class Course:
    def __init__(self, course_id, name, credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Credit: {self.credit}"


class SchoolManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        for _ in range(int(input("Enter number of students: "))):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter DoB (YYYY-MM-DD): ")
            self.students.append(Student(student_id, name, dob))

    def input_courses(self):
        for _ in range(int(input("Enter number of courses: "))):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credit = float(input("Enter course credit: "))
            self.courses.append(Course(course_id, name, credit))

    def input_marks(self):
        course_id = input("Enter course ID to input marks: ")
        course = self.find_course(course_id)
        if not course:
            print("Course not found.")
            return
        for student in self.students:
            mark = float(input(f"Enter mark for {student.name} ({student.student_id}): "))
            student.input_mark(course_id, mark, course.credit)
        self.calculate_all_gpa()

    def calculate_all_gpa(self):
        for student in self.students:
            student.calculate_gpa()

    def sort_students_by_gpa(self):
        gpas = np.array([student.gpa for student in self.students])
        sorted_indices = np.argsort(gpas)[::-1]
        self.students = [self.students[i] for i in sorted_indices]

    def list_students(self):
        self.sort_students_by_gpa()
        for student in self.students:
            print(student)

    def list_courses(self):
        for course in self.courses:
            print(course)

    def find_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Input students")
            print("2. Input courses")
            print("3. Input marks")
            print("4. List courses")
            print("5. List students with GPA")
            print("6. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                self.input_marks()
            elif choice == '4':
                self.list_courses()
            elif choice == '5':
                self.list_students()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    sms = SchoolManagementSystem()
    sms.run()
