sent = "I Lovee\tPYTHON"
print(sent)

# len function will give the length of the string
print(len(sent))



# Index of the following character inside the String
print(sent.index('L'))

# Replace Method to replace any character inside the String it will replace P with J
print(sent.replace('P', 'J'))
# even we can replace series of characters using the replace method
print(sent.replace('P', 'Kyt'))

# split method - to split the sentence based on any character and store it inside the list and get the first element
print(sent.split('P'))
list_01 = sent.split('P')
print(list_01[0])

print(sent.split(" "))

#string method to convert lower and upper case
print(sent.upper())
print(sent.lower())

print("***************************************************************************************************************************")

print(sent.title())
#to verify the boolean check if its Lower Or Upper case
print(sent.islower())
print(sent.isupper())

#python - count method which gives the count of each character
print(sent.count('e'))

print("***************************************************************************************************************************")
name = 'Jiten'
print("Name is :" +name)

#-format method to replace inside the string
lang = "I know {},{},{}".format("Ruby","Java","JS")
print(lang)
#same thing we can do with the help of index
lang = "I know {0},{1},{2}".format("Ruby","Java","JS")
print(lang)

#same thing we can do with the help of key and value pair
language = "I know {p},{j},{js}".format(p ='python',j ="Java" ,js = 'JavaScript')
print(language)

#f method to replace
lang = "Python"
name = "Aadya"

print(f'I love {name} and {lang}')

#strip method to remove the spaces
mystr = "  My name is Jiten "
print(mystr.strip())
