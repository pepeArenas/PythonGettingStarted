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


# We can use vars like in java but instead of use ... we use * and this will result in a list
def printNames(*names):
    print(names)


print(sum(1, 4))
printNames("Jesus", "Pepe", "Elena", "Lupita")


# Also we can have a kvars and this will result in a dictionary rather than a list as vars do
def printValues(**kvars):
    print(kvars["nombre"])


# We call the funtion kvargs defining the properties that the map will have
printValues(nombre="jesus", edad=34)


# Also we can have default values inside our function, this will make optional the arg with default value
def functionWithDefaultValue(name, age=18):
    print("Name: {} Age: {}".format(name, age))


# We can call without the default parameter and will print age default value
functionWithDefaultValue("Jesus")
# Also we can call the function with the second parameter and will override the default value
functionWithDefaultValue("Jesus", 34)
