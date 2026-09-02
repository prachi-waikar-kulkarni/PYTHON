# Loop : Something which repeats itself
#print("Hello World")

# WHILE
# A Counter is mandatory
# Use break to come out of infinite loop

# continue --> suspended that iteration
# break --> kill the loop, abort the loop
# Infinite loop can be need while designing games, when you want your code to be always on

# Iteration can be done on SEQUENCE (string,list,set,tuple,set,dict)

'''
while <condition> :
    code block
'''

## WHILE LOOP

# a = 0
# while a < 10 :
#     print(a,"Hello World")
#     a+=1

list_ex= ["John","Doe","India",32,12000.5]
# print(len(list_ex))

# a= 0
# while a < len(list_ex):
#     print(list_ex[a])
#     a+=1

# a= 0
# while a < len(list_ex):
#     if type(list_ex[a]) == int  or type(list_ex[a]) == float :
#         print(list_ex[a])
#     a+=1

a=0
while a < 5 :
    inp_str = input("Please enter a string")
    print(inp_str.upper())
    a+=1
else :
    print("Thank you for using this program")
    print("We are out of the loop")

# # INFINITE WHILE LOOP
# while True :
#     inp_str = input("Please enter a string")
#     if inp_str.upper() == "END" :
#         break   ## kicking out of the loop
#     print(inp_str.upper())

list_ex= ["John","Doe","India",32,12000.5]
a= 0
while a < len(list_ex):
    if type(list_ex[a]) == int  or type(list_ex[a]) == float :
        a+=1
        continue    ## suspend the execution for that iteration
    print(list_ex[a])
    a+=1

str = "prachi"
a=0

while a < len(str) :
    print(str[a])
    a+=1



