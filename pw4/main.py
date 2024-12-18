import curses
from input import input_students, input_courses, input_marks
from output import list_students, list_courses, show_message

def main(stdscr):
    curses.curs_set(0)
    students = []
    courses = {}

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
            break
        else:
            show_message(stdscr, "Invalid choice. Please try again.")

if __name__ == "__main__":
    curses.wrapper(main)
