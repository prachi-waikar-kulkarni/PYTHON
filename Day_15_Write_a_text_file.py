# These r,w are access_modifie
# r --> read
# w --> write
# a --> append
# .write() --> always overwrite, nahi hai to create kardega.
#

# file1=open('Day_14_Text_File.txt','r')
# ''' or '''
# file1=open('Day_14_Text_File.txt')

# file1=open('Day_15_Text_File.txt','w')
#
# file1.write('After this was written') # This has overwritten the file.
#
# file1.close()

file2=open('Day_16_Text_File.txt','a')
file2.write('\nAfter this was written')
file2.close()

