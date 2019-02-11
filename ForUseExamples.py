students = ["Jesus", "Guadalupe", "Miguel", "Elena"]
# Classic for each like iteration
for student in students:
    print("Welcome: {0} ".format(student))

index = 0

# This is an example with ranges by adding 0 -9
for index in range(10):
    print("Hello: {0}".format(index))

# This is an example with ranges by 2-9(we are starting at 2nd index), this is done by the use of range with 2 args
print("-----------------")
for index in range(2, 10):
    print("Hello {0}".format(index))

# Example with ranges by 2-9(starting at 2nd index) and move forward 2 by 2 position by the use ot range with 2 args
print("-----------------")
for index in range(2, 10, 2):
    print("Hellow {0}".format(index))
print("-----------------")

# In the case of the break, it will NOT continue as soon as it fulfill the condition, in this case miguel
for student in students:
    if student == "Miguel":
        print("Found Miguel")
        break
    print(student)
print("-----------------")

for student in students:
    if student == "Miguel":
        continue
        print("This line will NOT execute, when use continue it skip to the next itaration and everuthing below")
    print(student)
