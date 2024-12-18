import curses
import os
import zipfile
from input import input_students, input_courses, input_marks
from output import list_students, list_courses, show_message

def compress_files():
    with zipfile.ZipFile('students.dat', 'w') as zipf:
        for filename in ['students.txt', 'courses.txt', 'marks.txt']:
            if os.path.exists(filename):
                zipf.write(filename)

def decompress_files():
    if os.path.exists('students.dat'):
        with zipfile.ZipFile('students.dat', 'r') as zipf:
            zipf.extractall()

def load_data():
    students = []
    courses = {}
    if os.path.exists('students.txt'):
        with open('students.txt', 'r') as f:
            from domains.student import Student
            for line in f:
                student_id, name, dob = line.strip().split(', ')
                students.append(Student(student_id, name, dob))
    if os.path.exists('courses.txt'):
        with open('courses.txt', 'r') as f:
            from domains.course import Course
            for line in f:
                course_id, name, credit = line.strip().split(', ')
                courses[course_id] = Course(course_id, name, float(credit))
    return students, courses

def main(stdscr):
    curses.curs_set(0)
    decompress_files()
    students, courses = load_data()

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
            compress_files()
            break
        else:
            show_message(stdscr, "Invalid choice. Please try again.")

if __name__ == "__main__":
    curses.wrapper(main)
