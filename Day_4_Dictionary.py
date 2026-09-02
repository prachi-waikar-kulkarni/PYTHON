# Dictionary = MAPPING
# {key:value} key is unique
# Ordered --> FIFO
# Mutable

emp_dict = {
    "name": "John",
     "age": 25,
    "age" : 30,
    "name1" : "John",
    "name2" : "John"
}
# print(emp_dict["name"])
# print(emp_dict["age"])
# print(emp_dict)
#
# emp_dict["age"] = 40
# print(emp_dict)
#
# emp_dict["fname"]="John"
# print(emp_dict)
#
# del emp_dict["name"]
# print(emp_dict)
#
# print(emp_dict.get("name1","The key was not found"))

# print(emp_dict.keys())
# print(emp_dict.values())
#
# print(type(emp_dict.keys()))
# print(type(emp_dict.values()))

print(emp_dict.items()) ## returns kind of tuples
print(emp_dict)
emp_dict.clear()  ## returns an empty dictionary
print(emp_dict)