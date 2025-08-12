class Course:
    def __init__(self,course_name,course_code,instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self,student):
        if student.student_id not in[s.student_id for s in self.students]:
            self.students.append(student)

    def display_course_info(self):
        print("\nCourse Information:")
        print(f"Course Name:{self.course_name}")
        print(f'Code: {self.course_code}')
        print(f"Instructor: {self.instructor}")
        if self.students:
            print("Enrolled Students:",",".join([s.name for s in self.students]))
        else:
            print("Enrolled Student: None")