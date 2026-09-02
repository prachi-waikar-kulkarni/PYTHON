# Problem with while loop --> need to initialise the counter variable, write a separate comma


# Iterate over a sequence ---> bole to always FOR

# For loop is specifically for iterating over sequences (ranges)
# For is a slightly more compact way of iteration.

# for a in "Hello" :
#     print(a)

# list_ex= ["John","Doe","India",32,12000.5]
# for a in list_ex:
#     print(a)

# emp_tuple = ('John','Doe','Bangalore',True,True)
# for a in emp_tuple:
#     print(a)

# emp_set = {"John","Doe","John","Bangalore"}
# for a in emp_set:
#     print(a)
#
emp_dict = {
    "name": "John",
     "age": 25,
    "age" : 30,
    "name1" : "John",
    "name2" : "John"
}

#print(emp_dict.items())

#Dictionary me
# for a in emp_dict :
#     print(a,emp_dict[a])

# for a in emp_dict.keys() :
#     print(a)

# for a in emp_dict.values() :
#     print(a)

# for key, value in emp_dict.items() :
#     print(key, value)

# for i in range(1,501) :
#     if i == 250 :
#         break
#     print(i)

# for i in range(1,10) :
#     if i % 2 == 0 :
#         continue
#     print(i)

# for i in range(0,10,3) :
#     print(i)

for i in range(0,10,3) :
    print(i)
else :
    print("For loop has completed")


