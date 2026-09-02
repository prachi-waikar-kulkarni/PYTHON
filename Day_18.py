'''
# The Init function will be called only when the Object is being constructed.
# instance variables - model, price etc.. jiska value jo instance call kar rha hai uske hisab se value lega.
# static variable - jo class ke andar defined hai.
# instance method - Function whose value depends on the object/instance that is call. Ex show_details()
# We should use the decorator@staticmenthod, only when we do not wish to collect the
self (instance referrrence that gets passed when an object calls this method.)

Jab mujhe aisa method chahiye which is not dependent on the object calling/using it, I will create a static method.
- Agar static method use karni hai with the object, then we need the @staticmethod decorator.
'''


class Phone( ):
    #behaviour (what this class can do)
    type='Mobile'    ##

    @classmethod
    def greeting(cls):
        print(cls,"Good Morning",type(cls))

    @staticmethod
    def describe():
        print("This class describes the Phone")

    def __init__(self,model,price,color,brand): # ye __init__ wali method is auto invoked when an object is created.
        #print("Phone object created")
        self.model = model
        self.price = price
        self.color = color
        self.brand = brand
        type = 'Phone'
    def make_calls(self):
        print("This phone can make a call")
    def show_details(self):
        print(self.model,self.price,self.color,self.brand)

#print(type(Phone))
#Line 18,25 is called as constructor, since it is constructing an object.
phone1=Phone("S23 Ultra","100000","ForestGreen","Samsung")
#phone1 = Phone()
#phone2 = Phone()

#print(phone1.model,'\n',phone1.price,'\n',phone1.color,'\n',phone1.brand,'\n')

phone2=Phone("Iphone 14","200000","Slate Grey","Apple")
#print(phone2.model,'\n',phone2.price,'\n',phone2.brand,'\n')

#print(Phone.type)
#Phone.describe()

phone1.greeting()

#print(type(phone1))

