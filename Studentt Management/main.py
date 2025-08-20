from student import Student
from course import Course
from jsonn import save_data, load_data

students ={}
courses = {}

def add_new_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    address = input("Enter address")
    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Student Id Already exists")
        return
    students[student_id] = Student(name,age,address,student_id)
    print(f"Student {name} (ID: {student_id}) addes successfully")

def enroll_student_in_progress():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")

    if student_id not in students:
        print("student not found!")
        return
    
    student = students[student_id]
    course = courses[course_code]
    student.enroll_course(course)
    course.add_student(student)
    print(f"Student{students.name} (ID:{student_id}) enrolled in {course.course_name} (code:{course_code}).")

def add_grade_for_student():
    student_id = input("Enter Student Id:")
    course_code = input("Enter course code:")
    grade= input("Enter grade")

    if student_id not in students:
        print("Student not found.")
        return
    if course_code not in courses:
        print("Course not found")
        return 
    
    student = students[student_id]
    if course_code not in student.courses:
        print("Student is not enrolled in this course")
        return
    
    course_name = courses[course_code].course_name
    student.add_grade(course_name,grade)
    print(f"Grade {grade} added for {student.name} in {course_name}.")

def display_students_details():
    student_id = input("Enter student id")
    if student_id not in students:
        print("student not found")
        return 
    
    students[student_id].display_student_info()

def display_course_details():
    course_code = input("Enter Course Code: ")
    if course_code not in courses:
        print("Course not found!")
        return
    courses[course_code].display_course_info()

def add_new_course():
    pass

def enroll_student_in_course():
    pass




def main():
    global students, courses
    while True:
        print("\n==== Student Management System ====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")

        choice = input("Select Option: ")

        if choice == "1":
            add_new_student()
        elif choice == "2":
            add_new_course()
        elif choice == "3":
            enroll_student_in_course()
        elif choice == "4":
            add_grade_for_student()
        elif choice == "5":
            display_students_details()
        elif choice == "6":
            display_course_details()
        elif choice == "7":
            save_data(students, courses)
        elif choice == "8":
            students, courses = load_data()
        elif choice == "0":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()