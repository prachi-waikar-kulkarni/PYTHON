'''

'''


def decorated_greetings(greetings):
    #print("Inside decorated_greetings")
    def inner():
        print("################################")
        greetings()
        print("################################")

    return inner

'''
- Decorator can be thought of as a wrapper.
- At a time a function can be attached to only one decorator
- You can have multiple decorators for a function but then as you use them they will get overwritten as per the flow of the code.
- To use a function as a Decorator we add a '@' and this structure needs the enclosing function to be an inner function.
- Basically hum

@ : This expects one function to be returned.
  : The biggest USP of the @ is we are using the same Function name.

@ is same as writing line 25,26.
new_greeting = decorated_greetings(greetings)
new_greeting()

'''

@decorated_greetings # isse Python ko ye samjhega ki greetings is a decorated fucntion. so now now we don't have to call it explicitly.
def greetings ():
    print("Hello World")


@decorated_greetings_1 # isse Python ko ye samjhega ki greetings is a decorated fucntion. so now now we don't have to call it explicitly.
def greetings ():
    print("Hello World")

# new_greeting = decorated_greetings(greetings)
# new_greeting()
greetings()


