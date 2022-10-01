# function without any argument
def example():
    print('Hello World')
    c = 10 + 30
    print(c)
    print('Hello World_02')


# call the function()
example()


# function return
def sum(a, b):
    result = a + b
    print("Result is", result)
    return result


# call the stmt
d = sum(10, 30)

print('******************************************')


def greeting(fname, lname):
    print("Result is " + fname + " " + lname)

greeting('Kumar', 'Jiten')

# another way of calling
greeting(fname="Priya", lname='Aadya')
print('******************************************')

#create a function having the list of even numbers and pass parameter as list
def even_numbers_list (list):
    even_list = []
    for x in list:
        if x % 2 == 0:
            even_list.append(x)
        else:
            pass
    return even_list




result = even_numbers_list([2,10,8,9,12,24,56,64])
print(result)




