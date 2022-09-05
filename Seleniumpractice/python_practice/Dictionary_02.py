my_dict = {"Dev": "Aakash", "QA":"Jiten", "Devops" : "AADYA", "Severity":"Medium", 50 : "High"}
#it will give length based on the key items
print(len(my_dict))

#suppose if we want to get only the keys  from the dictionary
print(my_dict.keys())
#suppose if we want to get only the  values from the dictionary
print(my_dict.values())

#suppose if we want to see both the keys and values -it will return the values in terms of tuples
print(my_dict.items())

#another way of creating dictionary in python using the dict -constructor method
#in this way key will always be default string
my_dictionary = dict(QA="Jitu", Dev ="Akash", qa = "AAdya")
print(my_dictionary)

#another way of creating dictionary by giving values as tuple-list of tuples
my_dict_tuple = dict([(1,"Jiten"), (2,"AADYA"),(3,"PriyaJeet")])
print(my_dict_tuple)
