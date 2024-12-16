import math
import numpy as np
import curses


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


class Course:
    def __init__(self, course_id, name, credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Credits: {self.credit}"


class SchoolManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = {}

    def input_students(self, stdscr):
        num_students = int(self.get_input(stdscr, "Enter the number of students: "))
        for _ in range(num_students):
            student_id = self.get_input(stdscr, "Enter student ID: ")
            name = self.get_input(stdscr, "Enter student name: ")
            dob = self.get_input(stdscr, "Enter student DoB (YYYY-MM-DD): ")
            self.students.append(Student(student_id, name, dob))

    def input_courses(self, stdscr):
        num_courses = int(self.get_input(stdscr, "Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = self.get_input(stdscr, "Enter course ID: ")
            name = self.get_input(stdscr, "Enter course name: ")
            credit = float(self.get_input(stdscr, "Enter course credits: "))
            self.courses[course_id] = Course(course_id, name, credit)

    def input_marks(self, stdscr):
        if not self.students or not self.courses:
            self.show_message(stdscr, "No students or courses available to input marks.")
            return
        course_id = self.get_input(stdscr, "Enter the course ID to input marks: ")
        course = self.courses.get(course_id)
        if not course:
            self.show_message(stdscr, "Course not found.")
            return
        for student in self.students:
            mark = float(self.get_input(stdscr, f"Enter mark for {student.name} ({student.student_id}): "))
            student.input_mark(course_id, mark, course.credit)

    def list_students(self, stdscr):
        if not self.students:
            self.show_message(stdscr, "No students available.")
            return
        self.students.sort(key=lambda s: s.calculate_gpa(), reverse=True)  
        stdscr.clear()
        for student in self.students:
            stdscr.addstr(str(student) + "\n")
        stdscr.refresh()
        stdscr.getch()

    def list_courses(self, stdscr):
        if not self.courses:
            self.show_message(stdscr, "No courses available.")
            return
        stdscr.clear()
        for course in self.courses.values():
            stdscr.addstr(str(course) + "\n")
        stdscr.refresh()
        stdscr.getch()

    def show_message(self, stdscr, message):
        stdscr.clear()
        stdscr.addstr(message + "\n")
        stdscr.refresh()
        stdscr.getch()

    def get_input(self, stdscr, prompt):
        stdscr.addstr(prompt)
        stdscr.refresh()
        curses.echo()
        input_value = stdscr.getstr().decode("utf-8")
        curses.noecho()
        return input_value

    def run(self, stdscr):
        curses.curs_set(0)
        while True:
            stdscr.clear()
            stdscr.addstr("Menu:\n")
            stdscr.addstr("1. Input Students\n")
            stdscr.addstr("2. Input Courses\n")
            stdscr.addstr("3. Input Marks\n")
            stdscr.addstr("4. List Students (Sorted by GPA)\n")
            stdscr.addstr("5. List Courses\n")
            stdscr.addstr("6. Exit\n")
            stdscr.refresh()

            choice = stdscr.getch()
            if choice == ord('1'):
                self.input_students(stdscr)
            elif choice == ord('2'):
                self.input_courses(stdscr)
            elif choice == ord('3'):
                self.input_marks(stdscr)
            elif choice == ord('4'):
                self.list_students(stdscr)
            elif choice == ord('5'):
                self.list_courses(stdscr)
            elif choice == ord('6'):
                break
            else:
                self.show_message(stdscr, "Invalid choice. Please try again.")


if __name__ == "__main__":
    curses.wrapper(SchoolManagementSystem().run)
