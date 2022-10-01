#serialisation concept - to use the load function to convert the python dict to file module

import  simplejson

emp_json = {
    "name": "Kumar Jiten",
    "age": 30,
    "address": "Sydney",
    "isMarried": True,
    "isDependent" : None
}

with open('emp.json', 'w') as f:
    simplejson.dump(emp_json, f, indent = 3)

print('convert python dict object to JSON file ')