'''
NOTEWORTHY POINTS

Functions where no of arguments is not sure
Functions with arbitarary values
pass : use this keyword
*args : to input flexible  positional arguments. Through here args is just a variable name, wee could give any other name
        But it is industry practice to use args
        The args aere stored as a tuple
        We can perform all the actions that we do on a tuple with args.

**kwargs : to input flexible keyword arguments.
           they are stored as a dictionary.
           we can perform all the actions that we do on a dictionary.
'''

'''
def item_list(*args) :
    print(args)

def item_list(a,b,*args) :
    #print(args)
    for i in args:
        print(i)

item_list(1,2)
item_list(1,2,["sample","list"])

def item_list(*x) :
    print(x)
item_list(1,2,"hello","brother")



# Arbitary number of keywords args

def personal_details(**kwargs) :
    #print(kwargs)
    for x,y in kwargs.items() :
        print(x,y)

personal_details(fname="John",lname="Doe",emp_id=1, city="Nagpur")

personal_details(fname="John",lname="Doe",emp_id=1, city="Nagpur", state="Maharashtra")

