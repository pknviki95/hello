'''
input()- It is used for user input

- It takes every input as string
- Based on the requirement typecast to required data type

'''
'''
eval() function is used to evaluate the data type and it is generally associated with input() function for auto type casting.
''' 
'''
print() function is used to print output to output console.
    - print() function as mandatory has end character of new-line'\n'
    - In python 2 the print is not a function but in python 3 it is function and printing content has to be within paranthesis
'''

x = eval(input("enter a number = "))
print(type(x))
