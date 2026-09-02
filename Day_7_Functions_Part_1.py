# Function : Repeat a code block, but not sequencially.
# Function can take any number of arguments.
#
# Types of Arguments accepted by functions
# 1) Postional Arguments
# 2) Keyword AArguments

# return() ke bad control seedha function se bahaar aa jaega,
# so return() should be the last line of the function code
# In Python the function can return multiple values!


'''
def <name of function> (positional arguments)

'''
import math

'''
# Define a function
# def greeting():
#    print( "Hello world")

# Calling a function
# greeting()
# greeting()
# greeting()
# greeting()
# greeting()

# for i in range (1,10) :
#     greeting()

# def area_of_circle() :
#     area = 3.14 * 2 * 2
#     print(area)
#
# area_of_circle()
# area_of_circle()

# def area_of_circle(radius) :
#     area = 3.14 * radius * radius
#     print(area)
#     print(radius)
#
# area_of_circle(4)
# area_of_circle(2)
# area_of_circle(11)
# area_of_circle(10.5)
#
# def area_of_rectangle(length,width) :
#     area =  length * width
# #     print(area)
# #     print(length,width)
#     return("Success",area)
#
output,answer = area_of_rectangle(10,20)  #The return values are positional and can't be custom specified.
print(output,answer)
# area_of_rectangle(4,18)
# area_of_rectangle(2,70)

# def greeting(wish,fname,lname) :
#     print(wish,fname,lname)
#
#
# #greeting("Good Morning","John","Doe")
#
# greeting(lname="Doe",wish="Good Morning",fname="John")

# ARGUMENTS WITH DEFAULT VALUE
'''
def greeting(wish="Hello",fname=" ",lname="x") :
    print(wish,fname,lname)

greeting("Hello","John")
greeting("Hello","John","Doe")



