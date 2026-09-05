import re
pattern = '([a-zA-Z0-9_.]+)@([a-zA-Z]{3,8})(\.[a-z]{2,3})'

with open("email.txt",'r') as f:
    input_email = f.read()

#print(input_email)

emails = re.findall(pattern,input_email)
for email in emails:
    print(email[0],'@',email[1],email[2],sep='')
