'''
list- list is mutable collection of elements seperated with comma which is enclosed in []
'''
'''
list - mutable
'''
list0=[]
list1= [1,2,3,4,5]

#the boolean of empty list is always "false" which is later useful for automation
print(bool(list0))
#the boolean of non-empty list is always "true" which is later useful for automation
print(bool(list1))

#printing list values
print(list1)

#printing positive index values
print(list1[0])
print(list1[3])
print(list1[4])

#printing negative index values
print(list1[-1])
print(list1[-3])

#printing substring from list
#print(list1[3][2])

#slicing from list

print(list1[2::])

#reverse printing list

print(list1[::-1])

#replacing values based on index

list1[0] = 22
print(list1)



list2=list1.sort()
print(list2)
print(list1)