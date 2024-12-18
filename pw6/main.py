import curses
import os
import pickle
from input import input_students, input_courses, input_marks
from output import list_students, list_courses, show_message

def compress_files(students, courses):
    data = {
        'students': [(s.student_id, s.name, s.dob, s.marks, s.courses) for s in students],
        'courses': [(c.course_id, c.name, c.credit) for c in courses.values()]
    }
    with open('students.dat', 'wb') as f:
        pickle.dump(data, f)

def decompress_files():
    students = []
    courses = {}
    if os.path.exists('students.dat'):
        with open('students.dat', 'rb') as f:
            data = pickle.load(f)
            from domains.student import Student
            from domains.course import Course
            for student_id, name, dob, marks, student_courses in data['students']:
                student = Student(student_id, name, dob)
                student.marks = marks
                student.courses = student_courses
                students.append(student)
            for course_id, name, credit in data['courses']:
                courses[course_id] = Course(course_id, name, credit)
    return students, courses

def main(stdscr):
    curses.curs_set(0)
    students, courses = decompress_files()

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
            students = input_students(stdscr)
        elif choice == ord('2'):
            courses = input_courses(stdscr)
        elif choice == ord('3'):
            input_marks(stdscr, students, courses)
        elif choice == ord('4'):
            list_students(stdscr, students)
        elif choice == ord('5'):
            list_courses(stdscr, courses)
        elif choice == ord('6'):
            compress_files(students, courses)
            break
        else:
            show_message(stdscr, "Invalid choice. Please try again.")

if __name__ == "__main__":
    curses.wrapper(main)
