# RegEx ke liye we need to import a module RE
'''
[] : anyone value inside the bracket will be matched
Case Sensitive hai patterns
[iske andar jo likhte hai is called character class]
[^ : negation only within the []

META CLASS
[]


META CHARACTER
. : any character
^ :Check beginning
$ :Check ending
+ : This comes after a meta class    1 or more occurrence
* : 0 or more occurrence
? : 0 or 1 occurrence
{nnumber}
'''


import re

#print(re.search('el','Hello World'))

text = "_Hello World"

#print(re.search('[lmno]',text))

#print(re.search('[cde][lmno]',text))
#the sequence has to be followed
#cl,cm,cn,co,dl,dm,dn,do,el,em,en,eo
#jaha first match mila vaha bahar aa jaega.

#print(re.search('[a-f]',text))


#print(re.search('[A-Z][a-f]',text))

#print(re.search('[^A-Z]',text))

#print(re.search('[A-Za-z0-9]',text))


#print(re.search('H.l',text)) # H_l (H and L ke beech koi bhi single character)

# print(re.search('^Hello',"Hello")) # H_l (H and L ke beech koi bhi single character)
# print(re.search('^Hello',"Hey Hello")) # H_l (H and L ke beech koi bhi single character)
#
# print(re.search('^[A-Za-z0-9]',"Hello"))
#
# print(re.search('^[A-Za-z0-9]',"!Hello"))
#

# print(re.search('[A-Za-z0-9]$',"!Hello_"))
# print(re.search('[A-Za-z0-9]$',"!Hello"))

# print(re.search('[nta]+i',"Contains"))
# # nni,

# print(re.search('[nta]+i',"nightcontains"))
#
# print(re.search('to[lmna]+',"toll")) #toll
# print(re.search('to[lmna]',"toll")) #tol

#print(re.search('to[lmna]*',"to")) #to   * Returns partial match, even if the pattern has 0 matching chars
#
#print(re.search('to[lmna]+',"tok"))


#print(re.search('to[lmna]?',"tok"))

#print(re.search('to[lmna]{3}',"tolm"))  # {number} the pattern should repeat that many number of times.

#print(re.search('to[lmna]{3,5}',"tolmnll")) #min : 3 max:5 occurrences of the pattern

#print(re.search('to[lmna]{3,}',"tolllllllllllllllllllll")) #min : 3 max: infinite occurrences of the pattern

#print(re.search('to[lmna]{,3}',"to"))  #min : 0 max:3 occurrences of the pattern