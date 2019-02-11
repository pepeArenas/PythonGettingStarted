person = {"name": "Jesus", "age": 34}

# This will raise an error KeyError
# names = person["names"]

# In order to handle the error we need to use try except, in this case we are just catching the key error
try:
    names = person["names"]
except KeyError:
    print("An key error has raisen")
print("Out of the exception block")
print("----------------")
# If we want to catch a different type of error for example TypeError
try:
    sum = person["name"] + person["age"]
except KeyError:
    print("An KeyError has raisen")
except TypeError:
    print("An TypeError has raisen")
print("Out of the exception block")
print("----------------")
# Also we can have an generic excepcion, usually is not recomended, but also we can alias the exception as print inside the exept
try:
    sum = person["name"] + person["age"]
except Exception as error:
    print("An Generic excepcion has raisen")
    print(error)
print("Out of the exception block")
