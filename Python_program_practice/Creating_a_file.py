'''
#for creating a new file if not found and writing into a file

f = open('textfile.txt','w')
data=f.write("Hi! i am vignesh")
print(data)
f.close()
'''

'''
#for reading a existing file
f1=open('textfile.txt','r')
print(f1.read())
f1.close()
'''

#reading from a file and writing into another file

with open('textfile.txt','r') as f:
    data=f.read()
    print(data)

with open('witefile.txt','w') as f1:
    print(f1.write(data))