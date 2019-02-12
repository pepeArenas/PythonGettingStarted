

class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print("Hello: {0} your age is: {1}".format(self.name, self.age))
