## Can hold heterogeneous data.
## Can hold duplicate data
## Indexed and Ordered datatype -- Slicing,Negative index
## List is mutable (can be updated,added,removed)
## Membership operator is works
## List + List : possible
## List * int : possible


# emp_fname = "John"
# emp_lname = "Doe"
# emp_city="Bangalore"
# emp_country="India"

#emp_list01=[emp_fname,emp_lname,emp_city,emp_country]
#emp_list=["John","Doe","Bangalore","India",10.0,123456789,440012,True,True] ## This is space-saving compared to normal variables.
# print(emp_list)
# print(emp_list[0])
# print(emp_list[-1])
# print(emp_list[0:4])
# print(emp_list[:10:5])

# print(emp_list)
# emp_list[-1] = False
# print(emp_list)
#
# emp_list_temp=[1,"abc"]
# print(emp_list_temp * 3)
# print(emp_list+emp_list_temp)


# print('Bangalore' in emp_list)
# print('Bangalore' not in emp_list)


# UPDATING A LIST

# ## Add value in existing list
# print(emp_list)
# emp_list.append('India')
# print(emp_list)
# emp_list.append(12000)
# print(emp_list)
#
# ## Add at a specified place
# print(emp_list)
# emp_list.insert(2,'Male')
# print(emp_list)

## Removes last element by default
# emp_list.pop()
# print(emp_list)
# emp_list.pop()
# print(emp_list)
# emp_list.pop(3)
# print(emp_list)

# print(emp_list)
# emp_list.remove("Bangalore")
# print(emp_list)


# print(emp_list)
# emp_list.append('India')
# print(emp_list)


# # Removes first occurrence
# emp_list.remove("India")
# print(emp_list)

# print(emp_list)
# emp_list.clear()
# print(emp_list)
emp_list=["John","Doe","Bangalore","India",10.0,123456789,440012,True,True]
# print(emp_list)

#print(emp_list.reverse())
emp_list.reverse()
print(emp_list)