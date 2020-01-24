import json
import csv
list1 = []
#Reading a json file
req_file = "/home/pknviki95/Desktop/Python/Python_program_practice/simple_json.json"

with open (req_file,'r') as f:
    data = json.load(f)   # load fn() reads data from json file
print(data)



out_file = "/home/pknviki95/Desktop/Python/Python_program_practice/json_to_csv_write.csv"

with open(out_file,'w') as fo:
    csv_writer = csv.writer(fo)              # writing into csv file
    csv_writer.writerow(data.keys())         #keys are written in first rows
    csv_writer.writerow(data.values())       #its values are written in second rows 
    
    
