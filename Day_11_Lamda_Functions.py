# Lambda Function or Anonymous Functions

# def square (x,y):
#     return (x.__pow__(y))
#
# print(square(5))

'''
lambda <arguments>: <expressions> (pass the value of argument)

Expression me jo bhi likha hai it gets returned
Thus it is recommended to use the Lambda fucntion where the expressions returns something

Q) where to use --> Where functions accept function as an argument,
It has a capability to reduce number of lines drastically.
Though this reduces the readability.


Filter function :
filter(function_name,sequence)
filter function returns a raw data type,
In order to print it we need to typecast the returned value.
'''


# square = lambda x: x*x
# print(square(5))

# lambda x: x*x (5)
#
# print((lambda x: x*x) (5))



# a=2
# print(a.__pow__(5))
#
# print(a**5)

# print((lambda x: x.upper()) ("understanding lambda"))

# list1 = [1,2,3,4,5,6,7]
#
# # def even_nums (list1):
# #     for i in list1:
# #         if i % 2 == 0:
# #             print(i)
#
# def even_nums(x):
#     if x % 2 ==0:
#         return True
#
# #print(list(filter(even_nums,list1)))
#
# #print(list(filter(lambda x: x % 2 == 0,list1)))

print(list(filter(lambda x: x % 2 == 0,[1,2,3,4,5,6,7])))