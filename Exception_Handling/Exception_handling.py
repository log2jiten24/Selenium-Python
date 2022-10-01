
#Open the File in Read Only Mode

try:
    file_content = open("F:\\Python\\Selenium-Python\\Demo1.txt", "r")
    # open the file and read the file content line by line
    print(file_content.read())
    print('Read the file successfully')
except:
    print('Something went wrong')

print('THis is last statement ')


#Now we want to print the exception type - which exception is coming
try:
    file_content = open("F:\\Python\\Selenium-Python\\Demo.txt", "r")
    # open the file and read the file content line by line
    print(file_content.read())
    print('Read the file successfully')
except FileNotFoundError as err :
    print('Something went wrong' , err)

print('THis is last statement ')

