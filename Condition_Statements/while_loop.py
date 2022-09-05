#while loop - will have one variable outside the loop
#then we need to write the condition to evaluate the while loop
#once the condition is met - loop will get executed
x = 2
#evaluate the while loop condition
while x <10:
    print(x)
    #increment the value
    x = x+1

#now do while loop with else condition
num = 100
while num >100:
    print(num)
    num = num + 1
else:
    print("Above condition is not met ")


#now do while loop with break statement
number = 20
while number < 30:
    print(number)
    number = number+1
    if number == 25:
        break
#now do the same thing with continue statement
#contnue statement will continue the loop and the condition inside the continue stmt will not get executed
#it will directly hand it over the loop

number_01 = 50
while number_01 <60:
    print(number_01)
    number_01 = number_01 + 1
    if number_01 == 56:
        continue
        print('It will not get executed')

feedback =""
#when we enter the values present inside the list - it will come out of the loop
while feedback not in ["1" , "2" ,"3"]:
    feedback = input("Please enter feedback")
    print('Thank You')

