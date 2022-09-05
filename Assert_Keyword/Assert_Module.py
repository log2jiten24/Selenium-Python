#assert <condition> - if condition fails then it will break
#assert<condition> -<optional message>  if assertion will fail then it will throw error message
import math

assert True
print('Bye')

#assertion with optional message when the condition will fail

#assert  False, "Assertion is failing"
#print('Bye')

#this will check the validation and if validation will fail it will throw an error
assert 'Australia' in 'Australia is world 6th Largest country' "Validation failed -assertion error message"
print("Validation passed ")

str1 = "Python"
str2 = "Python"

assert  str1 == str2 , "Comparison of two Strings Failed :"
print('Two Strings are equal')

#Validate the Assert keyword in the List

assert  'Selenium' in ['Selenium' , 'UFT' , 'REST'] , "Validation failed -Selenium Not Present"
print('Selenium present')

assert  'Zalenium' not in ['Selenium' , 'UFT' , 'REST'] , "Validation failed -Zalenium Not Present"
print('Zalenium present')

assert  math.sqrt(4) == 2 ,'Value is Wrong'
print('Value is Right ')