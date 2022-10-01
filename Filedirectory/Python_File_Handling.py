
#open the file

try:
    f = open("F:\\Python\\Selenium-Python\\Demo1.txt", "r")
    #read the content of the  file
    data = f.read()
    print(data)
    #to check the mode
    print(f.mode)
    print(f.closed)
    f.close()

except Exception as err:
    print('File not found', err)

finally:
    f.close()
    # to verify whether the file has been closed or not - it will give boolean value as True
    print(f.closed)
