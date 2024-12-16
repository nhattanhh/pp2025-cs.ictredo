import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.credits = {}
        self.gpa = 0.0

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, DOB: {self.dob}, GPA: {self.gpa:.1f}"

    def input_mark(self, course_id, mark, credit):
        # Làm tròn điểm xuống 1 chữ số thập phân
        rounded_mark = math.floor(mark * 10) / 10
        self.marks[course_id] = rounded_mark
        self.credits[course_id] = credit

    def calculate_gpa(self):
        if not self.marks:
            self.gpa = 0.0
        else:
            # Tính GPA theo trọng số tín chỉ
            total_weighted_marks = np.sum(
                [self.marks[course] * self.credits[course] for course in self.marks]
            )
            total_credits = np.sum([self.credits[course] for course in self.marks])
            self.gpa = round(total_weighted_marks / total_credits, 1)


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
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student DoB (YYYY-MM-DD): ")
            self.students.append(Student(student_id, name, dob))

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credit = int(input("Enter course credit: "))
            self.courses.append(Course(course_id, name, credit))

    def input_marks(self):
        if not self.students or not self.courses:
            print("No students or courses available to input marks.")
            return
        course_id = input("Enter the course ID to input marks: ")
        course = self.find_course(course_id)
        if not course:
            print("Course not found.")
            return
        print(f"Input marks for course: {course.name} ({course.course_id})")
        for student in self.students:
            try:
                mark = float(input(f"Enter mark for student {student.name} ({student.student_id}): "))
                student.input_mark(course_id, mark, course.credit)
            except ValueError:
                print("Invalid mark. Please enter a numeric value.")

    def calculate_gpas(self):
        for student in self.students:
            student.calculate_gpa()

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: student.gpa, reverse=True)

    def list_students(self):
        if not self.students:
            print("No students available.")
            return
        print("Listing all students:")
        for student in self.students:
            print(student)

    def list_courses(self):
        if not self.courses:
            print("No courses available.")
            return
        print("Listing all courses:")
        for course in self.courses:
            print(course)

    def find_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def display_with_curses(self, screen):
        screen.clear()
        screen.addstr("School Management System - GPA Rankings\n", curses.A_BOLD)
        self.sort_students_by_gpa()
        for idx, student in enumerate(self.students, start=1):
            screen.addstr(f"{idx}. {student}\n")
        screen.addstr("\nPress any key to exit...")
        screen.refresh()
        screen.getch()

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Input number of students and their information")
            print("2. Input number of courses and their information")
            print("3. Input marks for a course")
            print("4. Calculate GPA for all students")
            print("5. List all students sorted by GPA")
            print("6. List all courses")
            print("7. Show GPA rankings with decorations (curses)")
            print("8. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                self.input_marks()
            elif choice == '4':
                self.calculate_gpas()
                print("GPA calculation completed.")
            elif choice == '5':
                self.sort_students_by_gpa()
                self.list_students()
            elif choice == '6':
                self.list_courses()
            elif choice == '7':
                curses.wrapper(self.display_with_curses)
            elif choice == '8':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = SchoolManagementSystem()
    system.run()
