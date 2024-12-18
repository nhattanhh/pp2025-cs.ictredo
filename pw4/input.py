import curses

def input_students(stdscr):
    stdscr.clear()
    stdscr.addstr("Enter the number of students: ")
    stdscr.refresh()
    curses.echo()
    num_students = int(stdscr.getstr().decode())
    curses.noecho()
    students = []
    for _ in range(num_students):
        stdscr.clear()
        stdscr.addstr("Enter student ID: ")
        stdscr.refresh()
        curses.echo()
        student_id = stdscr.getstr().decode()
        curses.noecho()
        
        stdscr.clear()
        stdscr.addstr("Enter student name: ")
        stdscr.refresh()
        curses.echo()
        name = stdscr.getstr().decode()
        curses.noecho()
        
        stdscr.clear()
        stdscr.addstr("Enter student DoB (YYYY-MM-DD): ")
        stdscr.refresh()
        curses.echo()
        dob = stdscr.getstr().decode()
        curses.noecho()
        
        from domains.student import Student
        students.append(Student(student_id, name, dob))
    return students

def input_courses(stdscr):
    stdscr.clear()
    stdscr.addstr("Enter the number of courses: ")
    stdscr.refresh()
    curses.echo()
    num_courses = int(stdscr.getstr().decode())
    curses.noecho()
    courses = {}
    for _ in range(num_courses):
        stdscr.clear()
        stdscr.addstr("Enter course ID: ")
        stdscr.refresh()
        curses.echo()
        course_id = stdscr.getstr().decode()
        curses.noecho()
        
        stdscr.clear()
        stdscr.addstr("Enter course name: ")
        stdscr.refresh()
        curses.echo()
        name = stdscr.getstr().decode()
        curses.noecho()
        
        stdscr.clear()
        stdscr.addstr("Enter course credits: ")
        stdscr.refresh()
        curses.echo()
        credit = float(stdscr.getstr().decode())
        curses.noecho()
        
        from domains.course import Course
        courses[course_id] = Course(course_id, name, credit)
    return courses

def input_marks(stdscr, students, courses):
    if not students or not courses:
        stdscr.clear()
        stdscr.addstr("No students or courses available to input marks.\n")
        stdscr.refresh()
        stdscr.getch()
        return
    stdscr.clear()
    stdscr.addstr("Enter the course ID to input marks: ")
    stdscr.refresh()
    curses.echo()
    course_id = stdscr.getstr().decode()
    curses.noecho()
    course = courses.get(course_id)
    if not course:
        stdscr.clear()
        stdscr.addstr("Course not found.\n")
        stdscr.refresh()
        stdscr.getch()
        return
    for student in students:
        stdscr.clear()
        stdscr.addstr(f"Enter mark for {student.name} ({student.student_id}): ")
        stdscr.refresh()
        curses.echo()
        try:
            mark = float(stdscr.getstr().decode())
            curses.noecho()
            student.input_mark(course_id, mark, course.credit)
        except ValueError:
            curses.noecho()
            stdscr.clear()
            stdscr.addstr("Invalid mark. Please enter a numeric value.\n")
            stdscr.refresh()
            stdscr.getch()
