#
# Docstring batata hai what do I do?
# Docstring -- Description about the function
#           -- It has to be written inside the function scope with ''' ''' only.


def item_list(a,b,*args) :
    '''
    Write the desc about the function
    Try to be as desc as we can for a third person to understand
    :param a: any value
    :param b: any value
    :param args: multiple values
    :return: there are no return values here.
    '''

    #print(args)
    for i in args:
        print(i)

    print(__name__,"Function ke ander wala")
if __name__ == '__main__':
    print("We are starting the execution now","\n","execution completed")

print(__name__)

#print(item_list.__doc__)

# print(item_list.__name__)

#item_list(1,2,3,4,5)



