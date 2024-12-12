def input_students():
    num_students = int(input("Enter the number of students: "))
    students = []
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB (YYYY-MM-DD): ")
        students.append({'id': student_id, 'name': name, 'dob': dob, 'marks': {}})
    return students
def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    courses = []
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses.append({'id': course_id, 'name': name})
    return courses
def input_marks(students, courses):
    if not students or not courses:
        print("No students or courses available to input marks.")
        return
    course_id = input("Enter the course ID to input marks: ")
    course_found = False
    for course in courses:
        if course['id'] == course_id:
            course_found = True
            print(f"Input marks for course: {course['name']} ({course['id']})")
            for student in students:
                try:
                    mark = float(input(f"Enter mark for student {student['name']} ({student['id']}): "))
                    student['marks'][course_id] = mark
                except ValueError:
                    print("Invalid mark. Please enter a numeric value.")
            break
    if not course_found:
        print("Course not found.")
def list_courses(courses):
    if not courses:
        print("No courses available.")
        return
    print("Listing all courses:")
    for course in courses:
        print(f"Course ID: {course['id']}, Course Name: {course['name']}")
def list_students(students):
    if not students:
        print("No students available.")
        return
    print("Listing all students:")
    for student in students:
        print(f"Student ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")
def show_student_marks(students, courses):
    if not students or not courses:
        print("No students or courses available to show marks.")
        return
    course_id = input("Enter the course ID to show student marks: ")
    course_found = False
    for course in courses:
        if course['id'] == course_id:
            course_found = True
            print(f"Student marks for course: {course['name']} ({course['id']})")
            for student in students:
                mark = student['marks'].get(course_id, "Not marked")
                print(f"Student ID: {student['id']}, Name: {student['name']}, Mark: {mark}")
            break
    if not course_found:
        print("Course not found.")
def main():
    students = []
    courses = []
    while True:
        print("\nMenu:")
        print("1. Input number of students and their information")
        print("2. Input number of courses and their information")
        print("3. Input marks for a course")
        print("4. List all courses")
        print("5. List all students")
        print("6. Show student marks for a given course")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            students = input_students()
        elif choice == '2':
            courses = input_courses()
        elif choice == '3':
            input_marks(students, courses)
        elif choice == '4':
            list_courses(courses)
        elif choice == '5':
            list_students(students)
        elif choice == '6':
            show_student_marks(students, courses)
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()