students = ["jesus", "miguel", "elena", "guadalupe"]


# We can have functions that not receive parameters and not return anything
def printStudents():
    for student in students:
        print(student)
    print("---------")


# The we call the function
printStudents()


# The function can have arguments
def addStudent(name):
    students.append(name)


# Then we call the function
addStudent("Mario")
printStudents()


# The function can return something
def sum(a, b):
    return a + b


print(sum(1, 4))
