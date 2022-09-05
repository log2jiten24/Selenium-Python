lang = input('Enter the language from the User : ')

#instead of giving lang value as hardcoded we will give the lang value as Input
#lang = "Python"

if lang == "Ruby":
    print('Ruby Found')
elif lang == "GO":
    print('GO Found')
elif lang == "Java":
    print('Java Found')
elif lang == "Python":
    print('Python found')
else:
    print('No Lang found')

print('*****************************************************')
#having multiple IFS
sal = 1000
#convert sal to integer 
sal = int(sal)

if sal >= 50000:
    print("Eligible for car loan")
if sal > 80000:
    print("Eligible for home loan")
if sal > 100000:
    print("Eligible for premium customer")
else:
    print("Not Eligible for any loan")