students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase


def print_student_titlcase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


student_list = get_students_titlecase()
while (True):
    student_name = input("Enter student name: ")
    if student_name == "N":
        break
    else:
        add_student(student_name)
        # student_id = input("Enter student ID: ")

for student in students:
    print(student)
