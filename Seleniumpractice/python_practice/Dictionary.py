#dictionary object - it can have duplicate values but key should be unique always
#it is unordered

my_dict = {"Dev": "Aakash", "QA":"Jiten", "Devops" : "AADYA", "Severity":"Medium", 50 : "High"}
print(my_dict)

#check the type
print(type(my_dict))

#to get the value assosciated with particular key value
print(my_dict['QA'])

#to do same thing using the get method
print(my_dict.get("Dev"))

print('*************************************************************************')
#for loop to iterate over the items
for k,v in my_dict.items():
 print(k,v)
 if v == "AADYA":
     break
print('*************************************************************************')
#to create list of values inside the Dictionary
my_dict_01 = {"Dev": "Aakash", "QA":["Jiten","Priya","Jeet"], "Devops" : "AADYA"}
print(my_dict_01)
#to get the list item from the dictionary object
print(my_dict_01['QA'])
#to print inside the list
print(my_dict_01['QA'][1])

print(my_dict_01.get('QA'))

#use dictionary object inside the dict object
my_dict_obj = {"Dev": "Aakash", "QA":{"Selenium" :"Priya","Cypress" :"Aadya"}, "Devops" : "AADYA"}
print(my_dict_obj)

#to fetch the nested dict object value of Selenium
print(my_dict_obj.get('QA').get('Selenium'))

#to do same thing in another way
print(my_dict_obj['QA']['Cypress'])

#to add element inside the dict object
my_dict_obj["Manager"] = "Jitu"
print(my_dict_obj)

#to update an existing element inside the dictionary
my_dict_obj["Manager"] = "Jeetu"
print(my_dict_obj)

#to delete the particular key value pair
my_dict_obj.pop('Devops')
print(my_dict_obj)

#to delete the last item use popitem
my_dict_obj.popitem()
print(my_dict_obj)

