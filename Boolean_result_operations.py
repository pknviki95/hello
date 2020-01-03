"""
-Boolean result string functions:
 -startswith()
 -endswith()
 -isupper()
 -islower()
 -isalpha()
 -isdecimal()
 -isdigit()
 -isspace()
 -istitle()

"""

my_str="PythonScripying"

#startswith():
'''
-This function returns boolean result if the given string starts with the character (or) sub-string
-These functions are case-sensitive
'''
print(my_str.startswith('p'))  

#endswith():
'''
-This function returns boolean result if the given string ends with the character (or) sub-string
-These functions are case-sensitive
'''
print(my_str.endswith('g'))

#islower():
'''
-This function returns boolean result if the given string is lowercase (or) not
-These functions are case-sensitive
'''
print(my_str.islower())

#isupper():
'''
-This function returns boolean result if the given string is uppercase (or) not
-These functions are case-sensitive
'''
print(my_str.isupper())

#istitle():
'''
-This function returns boolean result if the given string with each word starting with uppercase (or) not
-These functions are case-sensitive
'''
print(my_str.istitle())


#isspace():
'''
-This function returns boolean result if the given string with only space
-These functions are case-sensitive
'''
my_str1=" "
print(my_str1.isspace())

#isalpha():
'''
-This function returns boolean result if the given string with only alphabets
-These functions are case-sensitive
-There should not be any spaces in string
'''
print(my_str.isalpha())

#isdigit():
'''
-This function returns boolean result if the given string with only digit value
-These functions are case-sensitive
-There should not be any spaces in string
'''
my_str2="122425"
print(my_str2.isdigit())