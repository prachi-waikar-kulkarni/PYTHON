#input()  -- Input always considers datatype as string
#type()
#TYPECASTING FUNCTIONS --> int(),str(),float()

#input("Enter your name: ")
# name = input("Enter your name: ")
# city = input("Enter your city: ")
# city = "Nagpur"
# country = "India"
# #print("Hi I am",name,"I live in",city,"which is in",country)
#
# #f --> f string, format string.
# #print(f"Hi I am {name} and I live in {city} which is in {country}.")
#
#

# marks_eng = input("Enter your marks in English: ")
# marks_sci =input("Enter your marks in Science: ")
# marks_math = input("Enter your marks in Maths: ")
# total = marks_eng + marks_sci + marks_math
# print(type(marks_eng), type(marks_sci), type(marks_math), type(total),'\n')
# print(total)


marks_eng = int(input("Enter your marks in English: "))
marks_sci =int(input("Enter your marks in Science: "))
marks_math = int(input("Enter your marks in Maths: "))
total = marks_eng + marks_sci + marks_math
print(type(marks_eng), type(marks_sci), type(marks_math), type(total),'\n',total,total*100/300)




