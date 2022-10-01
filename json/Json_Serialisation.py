#Json Module to convert the Python Serialisation concepts - on how to convert the Python Dict Object to String JSON

import simplejson
emp_json = {
    "name": "Kumar Jiten",
    "age": 30,
    "address": "Sydney",
    "isMarried": True,
    "isDependent" : None
}

print(type(emp_json))

#convert this Dict Object to String - JSON
json_string = simplejson.dumps(emp_json)
print(type(json_string))

print('Converted Dict Object to String' + json_string)

#now if we want the json output with proper formatting and the spaces - indent will give 4 spaces
json_string_01 = simplejson.dumps(emp_json, indent = 4)
print('Converting Pyth Dict Object ' + json_string_01)

#now if we want the json output with proper sorted keys order
json_string_02 = simplejson.dumps(emp_json, indent = 4, sort_keys = True )
print('Converting Pyth Dict Object ' + json_string_02)