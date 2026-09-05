'''
Valid Email Id

Extract email from a text.
'''


#<user_id>   : [a-zA-Z0-9_.]+

import re


# Use () for Logical grouping , basically ease of understanding the pattern
#pattern = '([a-zA-Z0-9_.]+)@([a-zA-Z]{3,8})(\.[a-z]{2,3})(\.[a-z]{2,3})?'
pattern = '([a-zA-Z0-9_.]+)@([a-zA-Z]{3,8})(\.[a-z]{2,3})'
while(True) :
    input_email = input("Enter your email: ")
    match = re.search(pattern,input_email)
    #if match.group() == input_email :
    if re.search(pattern,input_email) :
        print("Valid Email Id")
        print(re.search(pattern,input_email))
    else :
        print("Invalid Email Id")
        break

