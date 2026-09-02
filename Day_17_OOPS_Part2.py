#self carries the referrence of the Object.

class Phone( ):
    #attributes
    model = ''
    price = ''
    color = ''
    brand = ''

    #behaviour (what this class can do)
    def __init__(self,model,price,color,brand): # ye __init__ wali method is auto invoked when an object is created.
        #print("Phone object created")
        self.model = model
        self.price = price
        self.color = color
        self.brand = brand
    def make_calls(self):
        print("This phone can make a call")
    def show_details(self):
        print(self.model,self.price,self.color,self.brand)

#Line 18,25 is called as constructor, since it is constructing an object.
phone1=Phone("S23 Ultra","100000","ForestGreen","Samsung")
#phone1 = Phone()
#phone2 = Phone()

#print(phone1.model,'\n',phone1.price,'\n',phone1.color,'\n',phone1.brand,'\n')

phone2=Phone("Iphone 14","200000","Slate Grey","Apple")
#print(phone2.model,'\n',phone2.price,'\n',phone2.brand,'\n')

phone1.show_details()
phone2.show_details()