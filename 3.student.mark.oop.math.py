import math

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  # {course_id: mark}
        self.credits = {}  # {course_id: credit}

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}"

    def input_mark(self, course_id, mark, credit):
        self.marks[course_id] = mark
        self.credits[course_id] = credit

    def get_mark(self, course_id):
        return self.marks.get(course_id, "Not marked")

    def calculate_gpa(self):
        total_weighted_marks = sum(self.marks[course_id] * self.credits[course_id] for course_id in self.marks)
        total_credits = sum(self.credits[course_id] for course_id in self.marks)
        if total_credits == 0:
            return 0.0
        gpa = total_weighted_marks / total_credits
        return math.floor(gpa * 10) / 10  # Round down to 1 decimal place


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

    def show_student_marks(self):
        if not self.students or not self.courses:
            print("No students or courses available to show marks.")
            return
        course_id = input("Enter the course ID to show student marks: ")
        course = self.find_course(course_id)
        if not course:
            print("Course not found.")
            return
        print(f"Student marks for course: {course.name} ({course.course_id})")
        for student in self.students:
            mark = student.get_mark(course_id)
            print(f"Student ID: {student.student_id}, Name: {student.name}, Mark: {mark}")

    def calculate_gpa_for_all_students(self):
        print("\nCalculating GPA for all students:")
        for student in self.students:
            gpa = student.calculate_gpa()
            print(f"Student ID: {student.student_id}, Name: {student.name}, GPA: {gpa}")

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda s: s.calculate_gpa(), reverse=True)
        print("\nStudents sorted by GPA (descending):")
        for student in self.students:
            gpa = student.calculate_gpa()
            print(f"Student ID: {student.student_id}, Name: {student.name}, GPA: {gpa}")

    def find_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Input number of students and their information")
            print("2. Input number of courses and their information")
            print("3. Input marks for a course")
            print("4. List all courses")
            print("5. List all students")
            print("6. Show student marks for a given course")
            print("7. Calculate GPA for all students")
            print("8. Sort students by GPA descending")
            print("9. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                self.input_marks()
            elif choice == '4':
                self.list_courses()
            elif choice == '5':
                self.list_students()
            elif choice == '6':
                self.show_student_marks()
            elif choice == '7':
                self.calculate_gpa_for_all_students()
            elif choice == '8':
                self.sort_students_by_gpa()
            elif choice == '9':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = SchoolManagementSystem()
    system.run()
