import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def __str__(self):
        return f"{self.name} ({self.student_id}) - GPA: {self.gpa}"

    def input_mark(self, course_id, mark):
        self.marks[course_id] = mark
        self.calculate_gpa()

    def get_mark(self, course_id):
        return self.marks.get(course_id, "Not marked")

    def calculate_gpa(self):
        if self.marks:
            self.gpa = sum(self.marks.values()) / len(self.marks)
            self.gpa = math.floor(self.gpa * 10) / 10

    def calculate_weighted_gpa(self, course_credits):
        weighted_sum = 0
        total_credits = 0
        for course_id, mark in self.marks.items():
            credits = course_credits.get(course_id, 1)
            weighted_sum += mark * credits
            total_credits += credits
        if total_credits > 0:
            self.gpa = weighted_sum / total_credits
            self.gpa = math.floor(self.gpa * 10) / 10
        else:
            self.gpa = 0

class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.course_id}) - Credits: {self.credits}"

class SchoolManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.course_credits = {}

    def input_students(self, stdscr):
        stdscr.clear()
        num_students = int(input("Enter number of students: "))
        for _ in range(num_students):
            student_id = input("Student ID: ")
            name = input("Student Name: ")
            dob = input("Student DoB (YYYY-MM-DD): ")
            self.students.append(Student(student_id, name, dob))
        stdscr.refresh()

    def input_courses(self, stdscr):
        stdscr.clear()
        num_courses = int(input("Enter number of courses: "))
        for _ in range(num_courses):
            course_id = input("Course ID: ")
            name = input("Course Name: ")
            credits = int(input("Credits: "))
            self.courses.append(Course(course_id, name, credits))
            self.course_credits[course_id] = credits
        stdscr.refresh()

    def input_marks(self, stdscr):
        if not self.students or not self.courses:
            print("No students or courses available.")
            return
        stdscr.clear()
        course_id = input("Enter course ID to input marks: ")
        course = self.find_course(course_id)
        if not course:
            print("Course not found.")
            return
        print(f"Input marks for {course.name} ({course.course_id})")
        for student in self.students:
            try:
                mark = float(input(f"Mark for {student.name}: "))
                mark = math.floor(mark * 10) / 10
                student.input_mark(course_id, mark)
            except ValueError:
                print("Invalid mark.")
        stdscr.refresh()

    def list_students(self):
        if not self.students:
            print("No students available.")
            return
        print("Students List:")
        for student in self.students:
            print(student)

    def list_courses(self):
        if not self.courses:
            print("No courses available.")
            return
        print("Courses List:")
        for course in self.courses:
            print(course)

    def show_student_marks(self):
        if not self.students or not self.courses:
            print("No students or courses available.")
            return
        course_id = input("Enter course ID to show marks: ")
        course = self.find_course(course_id)
        if not course:
            print("Course not found.")
            return
        print(f"Marks for {course.name} ({course.course_id})")
        for student in self.students:
            mark = student.get_mark(course_id)
            print(f"{student.name}: {mark}")

    def find_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda x: x.gpa, reverse=True)

    def run(self, stdscr):
        while True:
            stdscr.clear()
            print("\nMenu:")
            print("1. Input Students")
            print("2. Input Courses")
            print("3. Input Marks")
            print("4. List Courses")
            print("5. List Students")
            print("6. Show Marks")
            print("7. Sort Students by GPA")
            print("8. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.input_students(stdscr)
            elif choice == '2':
                self.input_courses(stdscr)
            elif choice == '3':
                self.input_marks(stdscr)
            elif choice == '4':
                self.list_courses()
            elif choice == '5':
                self.list_students()
            elif choice == '6':
                self.show_student_marks()
            elif choice == '7':
                self.sort_students_by_gpa()
                self.list_students()
            elif choice == '8':
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")
            stdscr.refresh()

if __name__ == "__main__":
    system = SchoolManagementSystem()
    curses.wrapper(system.run)
