
my_str1="Python Scripting is easy to learn"

#count():

"""
count()-
- This function is used to count the number of sub_string present in string. 
"""

print(my_str1.count('o'))
print(my_str1.count('i'))

#index():

"""
index()-
- This function returns the first occurance index value of a sub_string.
- The arguments are (sub_string,start) (i.e)it starts from the given index value
"""

print(my_str1.index('i'))
print(my_str1.index('i',11))

#find():

"""
find()-
- This function is used to find the position of first occurance of sub-string of a given string
- The arguments are (sub_string,start) (i.e)it starts from the given index value.
- If the given sub_string is not present it returns value -1.
"""

print(my_str1.find('i'))
print(my_str1.find('i',11))

print(my_str1.find("was"))