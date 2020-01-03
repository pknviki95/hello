"""
Case_operations of string:
   - It is used to convert the case of the given string
   
-lower()
-upper()
-swapcase()
-title()
-capitalize()
-casefold()
"""

my_string ="Python Scripting"

print(my_string)

#lower()
'''
-This lower() function is used to convert string into lower case
'''
print(my_string.lower())

#upper()
'''
-This upper function is used to convert string into upper case
'''

print(my_string.upper())

print(my_string)
'''
Note:

 -As you above the string eventhough we change the cases it does not affect the original string.
 -Since string is non_mutable
 -To change the original string the string can be stored into a variable and printed.

'''
str1=print("after saving upper() to a variable= ",my_string.upper())
str1=print("after saving lower() to a variable= ",my_string.lower())


#swapcase()
'''
-This swapcase() function is used to convert upper case to lower case and vice-versa of a string
'''
str1=print("after saving swapcase() to a variable= ",my_string.swapcase())

#title()
'''
-This title() function is used to convert the first letter of every word in string to upper case
'''
str1=print("after saving title() to a variable= ",my_string.title())

#capitalize()
'''
-This capitalize() function is used to convert the first letter of string to uppercase
'''
str1=print("after saving capitalize() to a variable= ",my_string.capitalize())

#casefold
'''
-This casefold() is same as lower() function
'''
str1=print("after saving casefold() to a variable= ",my_string.casefold())