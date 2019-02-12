students = []


class Student:
    # Somo special keyword start and finish with double underscore
    def __init__(self, name, id=124):
        student = {"name": name, "studentID": id}
        students.append(student)

    # This is the same of the toString java method
    def __str__(self):
        return "Some words, this is similar a toString method"


jesus = Student("Jesus")
# This will print the whatever we define in our __str__
print(jesus)
