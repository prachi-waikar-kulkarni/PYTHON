def div_decorator(div):
    print("Aao test karen")
    def inner(a,b):
        if b==0:
            print("Please enter a non zero value for the Denominator")
        else:
            div(a,b)
    return inner

@div_decorator
def div(a,b) :
    print(a/b)

div(4,2)

div(4,0)

div(5,2)


## Abhi me pure div ka kabhi call nahi kar sakungi
## To overcome this,

