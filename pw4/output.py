import curses


def list_students(stdscr, students):
    stdscr.clear()
    students.sort(key=lambda s: s.calculate_gpa(), reverse=True)  # Sort by GPA descending
    for student in students:
        stdscr.addstr(str(student) + "\n")
    stdscr.refresh()
    stdscr.getch()


def list_courses(stdscr, courses):
    stdscr.clear()
    for course in courses.values():
        stdscr.addstr(str(course) + "\n")
    stdscr.refresh()
    stdscr.getch()


def show_message(stdscr, message):
    stdscr.clear()
    stdscr.addstr(message + "\n")
    stdscr.refresh()
    stdscr.getch()
