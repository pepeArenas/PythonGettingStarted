students = []


class Student:
    schoolName = "Rep Haiti"

    # Self is the same as this in java, it refers to each instance so the value will change every new instance we create
    def __init__(self, name, id=12):
        self.name = name
        self.id = id
        students.append(self)

    def __str__(self):
        return "Student name:" + self.name + " Student ID: " + self.id

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.schoolName


jesus = Student("Jesus")

print(jesus.get_name_capitalize())
# We can access as a static variable
print(Student.schoolName)
