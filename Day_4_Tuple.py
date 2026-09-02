# 0 based INDEXED and ORDERED
# heterogeneous
# can have duplicates
# ** Immutable ** Making it slightly faster than lists, memory bhi kam lagegi since extra metadata nahi store karna hai.


emp_tuple = ('John','Doe','Bangalore',True,True)

# print(emp_tuple)
# print(emp_tuple[-1])
#
# emp_tuple[-1] = False
# print(emp_tuple)

#print(emp_tuple.count(True))

print(emp_tuple.index(True)) ## Index of the first occurrence only

#print(emp_tuple.index(False))

print(len(emp_tuple))
print("Indian" in emp_tuple)