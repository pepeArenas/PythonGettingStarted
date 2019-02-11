index = 0

# We can use as normal loop, the difference between this an for is that here we need to sum the counter by ourself
while index < 10:
    print("Counter {}".format(index))
    index += 1
print("-----------------")
# We can use break
index = 0
while index < 10:
    if index == 2:
        print("Is equal to 2 and will finish the loop")
        break
    print("Counter {}".format(index))
    index += 1
print("-----------------")
# We also can use with continue
index = 0
while index < 10:
    if index == 2:
        index += 1
        continue
        print("This line will not execute")
    print("Counter {}".format(index))
    index += 1
