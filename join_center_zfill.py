"""
join():
- This function is used to join the given string between the characters of string

center():
- This function is used to allocate the string to centre based on allocated space 
- (i.e) if allocated space is 10 then the string is printed from centre of allocated space 

zfill():
- This function is used to add zero's to leftside of the existing string based on allocated space.
- This is also called as Padding.

"""

my_str = "Python"

#join():

print("*".join(my_str))

#center():

print(my_str.center(20))

#zfill():

print(my_str.zfill(20))
