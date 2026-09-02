'''

NESTED FUNCTIONS

greeting2(greeting)   --> passing a function --> it will pass it as a function which will be used in the outer function.
greeting2(greeting()) --> passing a function call --> output pass hoga

'''
'''
def outer():
    print("This is the outer function")
    def inner():
        print("This is the inner function")
    inner()

outer()
'''

# def greeting():
#     return("Hello")
#
# def greeting2(func):
#     print(func)
#
# greeting2(greeting())

# when I go greeting() , passing a function call bole to function ka output pass hoga


def greeting():
    print("Hello")

def greeting2(func):
    func()

greeting2(greeting)
print(type(greeting)) ## Here the type of greeting is a function

greeting = 2
## This will work as this is just an identifier

print(type(greeting)) ## Ans <int>

