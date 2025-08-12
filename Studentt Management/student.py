from person import Person

class Student(Person):
    def __init__(self,name,age,address,student_id):
        super().__init__(name,age,address)
        self.student_id = student_id
        self.grades = {}
        self.course =[]

    def add_grade(self,subject,grade):
        self.grades[subject]=grade

    def enroll_course(self,course):
        if course.course_code not in self.courses:
            self.courses.append(course.course_code)

    def display_student_info(self):
        print("\nStudent Information:")
        self.display_person_info()
        print(f"ID:{self.student_id}")
        print(f"Enrolled Courses:{self.courses if self.courses else 'None'}")
        print(f"Grades: {self.grades if self.grades else 'None'}")
