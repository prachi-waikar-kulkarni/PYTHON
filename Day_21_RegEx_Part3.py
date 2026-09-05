import re

#re.fullmatch()

# Use () for Logical grouping , basically ease of understanding the pattern
#pattern = '([a-zA-Z0-9_.]+)@([a-zA-Z]{3,8})(\.[a-z]{2,3})(\.[a-z]{2,3})?'
pattern = '([a-zA-Z0-9_.]+)@([a-zA-Z]{3,8})(\.[a-z]{2,3})'
while(True) :
    input_email = input("Enter your email: ")
    match = re.fullmatch(pattern,input_email)
    if match.group() == input_email :
        print("Valid Email Id")
        print(re.fullmatch(pattern,input_email)
    else :
        print("Invalid Email Id")
        break
