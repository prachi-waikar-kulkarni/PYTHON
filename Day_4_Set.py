# SET = Unique data elements
# UNORDERED and UNINDEXED
# Mutable - add, remove

emp_set = {"John","Doe","John","Bangalore"}
print(emp_set)

emp_set.add("India")
print(emp_set)
emp_set.add("Indian")
print(emp_set)

emp_set.discard("India")
print(emp_set)

print(len(emp_set))
print("Indian" in emp_set)
