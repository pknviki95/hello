"""
strip():
- This function is used to remove the two existing sides of the string.
- By default it reomves the space
lstrip():
-This function is used to remove the left extreme content of the string.

rstrip():
-This function is used to remove the right extreme content of the string.
"""

#strip():
my_str="   Python   "

print(my_str.strip())
'''
Note:
-By default it removes the spaces in the string
'''
#To strip out selected string

my_str1="Python Scripting is easy to learn"
print(my_str1.strip("learn").strip("Python"))

#lstrip():

print(my_str1.lstrip("Python"))

#rstrip():

print(my_str1.rstrip("learn"))

#split():
'''
split()-
- The split function is used to split the string into a list of strings.
- By Default the de-limiter is space (i.e) string are seperated to list of string based on space
- The de-limeter is passed as arguments based on the requirements
'''

print(my_str1.split())

print(my_str1.split("is"))  #with delimeter passed as argument
