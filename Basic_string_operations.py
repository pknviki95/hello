'''
string- String is a non-Mutable(it cannot be edited) sequence of characters marked under quotations.
    - It is case-sensitive
    - the string can be a alphabet,number,white space and special characters within quotations
'''

str1="Welcome to python scripting."
str2="I am Vignesh"
str3="i am vignesh"

#case-sensitive
if str2 == str3:
    print("Equal")
else:
    print("Not-Equal")

#Concatination
'''
the string can be concatinated by using '+' operator if both are strings
'''
print(str1+str2)

#Sequence Type
'''
- The strings are sequence of characters as they can be acessed through their index
'''
print(str1[0])
print(str1[3])

#Repetation of string
'''
- The string can be repeated by * with numbers
'''
print(str2 * 3)

#slicing of string
'''
- This is slicing of strings by str[start:end:step=0(default)]
'''
#positive slicing
print(str1[0:4:])

#Negative slicing
print(str1[:-5:-1])

#Reversing of string
'''
- The string can be accesesed with their index to reverse print we have to start from reverse index
'''
print(str1[::-1])