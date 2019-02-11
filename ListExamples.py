students=[] #Declare an empty list
print(students)
students = ["jesus", "miguel", "elena", "guadalupe"]# assign some values to our list
print(students)
numberOfStudents = len(students)
print(numberOfStudents)
#students[4] = "mario" #In this case we cannot assign in this way, throws an index out of range Error
students.append("mario")#We add an element to the end of the list
print(students)
#In the next examples we do not affect our original list, is just kind of a temporary view
print(students[1:])#Will skip the first and print the 2,3,4,5
print(students[1:-1])#We skip the first and the last element
print(students[-1:])#Will skip all except the last one (-1)
#If we want to look for value inside our list we can do the following
print("jesus" in students)#As jesus is in the list it will return True
print("Jesus" in students)#As Jesus with the first J is not in the list we will get False
print("Jesus".lower() in students)#As we explicitly convert to lower case the J we will ger a True
#If we want to delete an element we have the del function
del students[-1] #Here we will delete the last element, in this case mario
print(students)#Here we have the student without mario who we delete in the last step



