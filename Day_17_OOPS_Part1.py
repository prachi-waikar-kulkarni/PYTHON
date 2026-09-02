# OBJECT : ATTRIBUTE --> Features
#           Behaviour --> Functionality
#            Object = Instance of the class
# CLASS ---> Template for an Object
# Class ke andar ke function ko Method bolte hai

class Phone :
    #attributes
    model = ''
    price = ''
    color = ''
    brand = ''

    #behaviour (what this class can do)
    def make_calls(self):
        print("This phone can make a call")

phone1 = Phone() # idhar the class is being instnatiated into memory.
print(type(phone1))
phone1.make_calls()
phone1.model = "S23 Ultra"
phone1.price = 100000
phone1.color = "Forest green"
phone1.brand = "Samsung"

print(phone1.model,'\n',phone1.price,'\n',phone1.color,'\n',phone1.brand,'\n')

phone2=Phone()
print(type(phone1))
phone2.make_calls()
phone2.model = "Iphone 14"
phone2.price = 200000
phone2.color = "Slate grey"
phone2.brand = "Apple"

print(phone2.model,'\n',phone2.price,'\n',phone2.color,'\n',phone2.brand,'\n')

