#Number Datatype
x=10
y=2.5
z=3+4j

print(x,type(x),id(x))
print(y,type(y),id(y))
print(z,type(z),id(z))

#string datatype
str1="Hi! I am Vignesh"
print(str1,type(str1))

#Boolen datatype
value1=True
value2=False

print(value1,type(value1))
print(value2,type(value2))


#Type conversion/Type casting
'''
 - converting one datatype into other
'''
a=5.6
print(a,type(a))
#After type casting
b=int(a)
print(b,type(b))

c=bool()
print("Empty bool =",c)
d=bool(1)
print("non_empty_bool =",d)