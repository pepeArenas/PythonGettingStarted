# We declare a value pair dictionary
persona = {"name": "Jesus", "age": "34"}
# We can declare list of maps or dictionaries
personas = [
    {"name": "Jesus", "age": "34"},
    {"name": "Miguel", "age": "64"},
    {"name": "Elena", "age": "54"}
]

# We can access by its index and the property in order to get the value
print(personas[0]["name"])
# If we put a bad name it will thows an error
# print(personas[0]["names"])

print("---------------")
# In order to avoid the last error we can define a default message, in this case a Unknown"
print(personas[0].get("names", "Unknown 3"))
print("---------------")
# If we want to erase an entry is the same as list with the del function
del personas[0]
print(personas)
print("---------------")
# If we want to list all the values
print(personas[0].values())
print("---------------")
# If we want to list all the keys
print(personas[0].keys())
