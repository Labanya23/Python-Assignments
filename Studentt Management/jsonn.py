import json
from student import Student
from course import Course

def save_data(students,courses):
    data = {
        "students":{

            sid:{
                "name": s.name,
                "age": s.age,
                "address":s.address,
                "student_id":s.student_id,
                "grades":s.grades,
                "courses": s.courses
            }
            for sid , s in students.items()

        },
        "courses": {
            c.course_code:{
                "course_name": c.course_name,
                "course_code": c.course_code,
                "instructor": c.instructor,
                "students":[s.student_id for s in c.students]
            }
            for cid, c in courses.items()
        }
    }
    with open("STUDENT_MANAGEMENT.json","w") as f:
        json.dump(data,f)
    print("All student and course data saved successfully")

def load_data():
    students = {}
    courses = {}
    try:
        with open("STUDENT_MANAGEMENT.json","r") as f:
            data = json.load(f)
        
        for sid, s in data["students"].items():
            student = Student(s["name"], s["age"], s["address"], s["student_id"])
            student.grades = s["grades"]
            student.courses = s["courses"]
            student[sid]= student

        for cid, c in data["courses"].items():
            course = Course(c["course_name"], c["course_code"], c["instructor"])
            for sid in c["students"]:
                if sid in students:
                    course.add_student(students[sid])
            courses[cid] = course

            print("Data loades successfully")
    except FileNotFoundError:
        print("No saved data found")

    return students,courses

