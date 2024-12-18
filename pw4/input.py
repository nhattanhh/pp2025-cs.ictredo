def input_students():
    num_students = int(input("Enter the number of students: "))
    students = []
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB (YYYY-MM-DD): ")
        from domains.student import Student
        students.append(Student(student_id, name, dob))
    return students


def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    courses = {}
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credit = float(input("Enter course credits: "))
        from domains.course import Course
        courses[course_id] = Course(course_id, name, credit)
    return courses


def input_marks(students, courses):
    if not students or not courses:
        print("No students or courses available to input marks.")
        return
    course_id = input("Enter the course ID to input marks: ")
    course = courses.get(course_id)
    if not course:
        print("Course not found.")
        return
    for student in students:
        try:
            mark = float(input(f"Enter mark for {student.name} ({student.student_id}): "))
            student.input_mark(course_id, mark, course.credit)
        except ValueError:
            print("Invalid mark. Please enter a numeric value.")
