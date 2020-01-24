import json
dic={}
#reading a json file
req_file= "/home/pknviki95/Desktop/Python/Python_program_practice/json_test.json"

with open (req_file,'r') as f:
    data = json.load(f)
    print(data)
#writing data to json file
out_file= "/home/pknviki95/Desktop/Python/Python_program_practice/json_write_test.json"
with open (out_file,'w') as fo:
    print(json.dump(data,fo,indent=4))
