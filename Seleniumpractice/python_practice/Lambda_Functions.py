#to calculate the square of the number - before lambda functions
def square (num):
    print(num * num)

#call the function
square(3)

#create a list
l1 = [2,3,6,8]

for x in l1:
    square(x)
print ('*********************************************************')

#syntax of lambda expressions:
#funcobj = lambda arguments : expression

data = lambda num : num * num

#data is turned as anonymous function - function without any body
result = data(8)
print(result)

newData = lambda n1, n2, n3 : n1*10+n2*3+n3*2
print(newData(10 , 20 , 30 ))