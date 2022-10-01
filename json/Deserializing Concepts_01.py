
#Deserializing concepts - to convert the JSON String to the Python Dict Object

import  simplejson

str_json = '''{
   "name": "Kumar Jiten",
   "age": 30,
   "address": "Sydney",
   "isMarried": true,
   "isDependent": null
}'''

python_dict = simplejson.loads(str_json)
print(type(python_dict))

print(python_dict)
#printing each key and value pair from the JSON
for k,v in python_dict.items():
    print(k,v)

print('************************************************')
#example of load function

with open('str_json', 'r') as f:
    python_dict_01 = simplejson.load(f)

print(type(python_dict_01))

#printing each key and value pairs
print(python_dict_01.keys())
print(python_dict_01.values())
