'''
closure function : a function which has ability to remember the value from its inclusive function.
                   ability to call an inner function from the main code.
                   Ye concept --> Decorators me use hoga

                   Kind of variablizing an inner function.

Global keyword se Global variables ka value update hoga.


Application : Database
'''

# x and y are global variables, they are accessible throughout the code.
x=10
y=20

def outer():
    msg= "Hello World"

    # global x
    # global y
    x = 100  # non local variable
    y = 200
    print("from outer before :",x,y)
    def inner():
        #print(msg)
        # global x
        # global y
        nonlocal x
        nonlocal y
        x = 1000    # local var
        y = 2000
        print("from inner:", x, y)
    inner()
    print("from outer after ", x, y)
    #return inner()  #inner call hoga and uska output jaega
    return inner   #idhar mujhe inner function milega


new_inner_func = outer() #Here new_inner_func is called as Closure Function

# inner function ke respect me outer function is called Enclosing function.

print("from global:", x, y)
# print(outer.__name__)
# print(new_inner_func.__name__)

## the scope of a variable defined inside a function is limited only to that function definition,
## Although in this code their names are same but they are different variables.

#new_inner_func()

# Q) I want to update the value of x and y in the outer function from the inner function without updating the global x and y.