'''
Add some functionality/features to an existing function. (This could be system defined or user defined function.)
Dec


'''
'''
def decorated_greetings(greetings):
    #print("Inside decorated_greetings")
    def inner():
        print("################################")
        greetings()
        print("################################")

    return inner


def greetings ():
    print("Hello World")

new_greeting = decorated_greetings(greetings)
new_greeting()
#greetings()
'''
########################
# WAY 2
# Q Why did we not do this way?
# A
########################

def decorated_greetings(greetings):
    print("################################")
    greetings()
    print("################################")


def greetings ():
    print("Hello World")

decorated_greetings(greetings)
