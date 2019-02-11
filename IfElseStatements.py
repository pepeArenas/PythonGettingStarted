trueValueExample = True
falseValueExample = False

if(trueValueExample):
    print("Printing True value")
else:
    print("Printing false value")

if(not falseValueExample):
    print("Is a falsy")
else:
    print("Is truthty")

print("True at all" if trueValueExample == falseValueExample else "False at all")

if(trueValueExample and falseValueExample):
    print("Both values are true")
else:
    print("Not are true both")

if(trueValueExample or falseValueExample):
    print("At least one of them are true")

if(falseValueExample or trueValueExample ):
    print("At least one of them are true")

print("In python we have truthy or falsy values so consider the following")

"""The following examples are falsy:
String is empty
Int is 0
Variable is None
Boolean is False"""
falsyFalse = False
print("Truthy" if falsyFalse else "Falsy")
falsyZeroInt = 0
print("Truthy" if falsyZeroInt else "Falsy")
falsyNone = None
print("Truthy" if falsyNone else "Falsy")
falsyEmptyString = ""
print("Truthy" if falsyEmptyString else "Falsy")
"""The following examples are truty:
String is not empty
Int is not 0
Variable is not None
Boolean is True"""
falsyFalse = True
print("Truthy" if falsyFalse else "Falsy")
falsyZeroInt = 1
print("Truthy" if falsyZeroInt else "Falsy")
falsyNone = "s"
print("Truthy" if falsyNone else "Falsy")
falsyEmptyString = "s"
print("Truthy" if falsyEmptyString else "Falsy")
