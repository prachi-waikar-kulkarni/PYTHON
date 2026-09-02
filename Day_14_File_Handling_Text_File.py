#open("Day_14_Text_File.txt") #This will load my file in RAM.
#In order to work with a file it is imperative to store it into a reference(variable)
# Disadv of using .read() ---> it will load the entire file in one shot which may cause performance bottlenecks.
# Thus it is better to use .readline() instead.

'''
TEXT FILES
open(filename)
.read()
.readline()
.tell()
.seek()
file1.close()
'''


file1= open("Day_14_Text_File.txt")
'''
#print(file1.read())
print(file1.read(7)) #no of chars which are being read
print(file1.tell())

print(file1.read(7)) #the next 7 chars are being read, basically it is storing the value of the cursor.
print(file1.tell())

print(file1.read(7))
print(file1.tell())

#reset the cursor (pointer)
file1.seek(0)
print(file1.tell())
print(file1.read(7))

file1.seek(10) ## Isse cusrsor 10 pe jaega.. jaha pohochana hai vo number de sakte hai.
print(file1.read(7))
print(file1.tell())

print(file1.tell())
print(file1.readline())
print(file1.tell())
print(file1.readline())
print(file1.tell())
file1.seek(0)
'''

'''
READING AN ENTIRE FILE USING THE READLINE FUNCTION
'''
# data=" "
# while data != "" :
#     data = file1.readline()
#     print(data)


''' WHILE LOOP STD WAY'''
# while file1:
#     data=file1.readline()
#     print(data)
#     if data=="" :
#         break

''' FOR LOOP '''

# for line in file1:
#     print(line)

file1.close()  #This closes the file.
               #The close function does not accept a parameter.
               #Close will send the file back to the hard disk.

'''
WITH OPEN()
'''
# Here the scope of the File is limited only to this with block.
# I need not separately open and close the file.
with open("Day_14_Text_File.txt") as file:
    print(file.read())




