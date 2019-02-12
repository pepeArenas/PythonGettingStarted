students = []


class Student:
    # Self is similar concept of this
    def add_student(self, name, studentId=123):
        student = {"name": name, "studentId": studentId}
        students.append(student)


student = Student()
student.add_student("Jesus")
print(students)
