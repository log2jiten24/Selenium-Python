import re

txt = "The rain in Spain"

x = re.search("^The.*Spain$", txt)
print(x)

#The findall() function returns a list containing all matches.

y = re.findall("ai", txt)

#it will return the list of the list of the characters list found inside the String
print(y)
print(type(y))

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
#this will return None as Portugal is not present insie the txt

txt = "The rain in Spain"
y = re.search("Spain", txt)
print(type(y))

#Split function - it returns a list where the string is split at each match
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
#it will return the list of the values


#Split function - it returns a list where the string is split for one match
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

#The sub() function replaces the matches with the text of your choice:
#sub function will replace all the character with the character which we want to replace
txt = "The rain in Spain"
x = re.sub("\s" , "9", txt)
print(x)

#suppose if we want to replace only two characters
txt = "The rain in Spain"
x = re.sub("\s" , "9", txt,2)
print(x)
#it will replace only the two spaces

#format function
txt = 'The country is  {} where you are living'
print(txt.format('Australia'))

x = 5
y = 10
if not (x> 10 and y < 10 ):
    print('It not satisfies')