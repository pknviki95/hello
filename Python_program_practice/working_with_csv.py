import csv
list1 = []
req_file="/home/pknviki95/Desktop/Python/Python_program_practice/csv_test.csv"
#reading a csv_file
with open (req_file,'r') as f:
    data = csv.reader(f)
    for each in data:
        list1 += [each]
print(list1)
    

#writing into a csv file
out_file="/home/pknviki95/Desktop/Python/Python_program_practice/csv_write_test.csv"
with open (out_file,'w') as fo:
    out_data = csv.writer(fo,delimiter=",")
    for each in list1:
        print(out_data.writerow(each))