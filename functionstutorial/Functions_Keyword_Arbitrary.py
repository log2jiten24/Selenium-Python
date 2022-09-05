#example of arbitrary arguments
#if we pass *args - then we can pass any number of parameters  while calling the function

#by default args take value in the form of tuples
def keyword(*args):
    print('My value passed', args)
    #print the first value inside the tuple
    print(args[1])
    #if we want to iterate inside the tuple
    for name in args:
        print(name)

#call the function - and we can pass any number of parameters
keyword('Jiten' ,'Aadya','Priya','Khushi')

#it will return as tuple

#create sum of all the values
def sum_of_all_numbers(*args):
    print(sum(args))

#print the sum of all numbers
sum_of_all_numbers(10,20,30)

#create max of all the values
def max_of_all_numbers(*args):
    print(max(args))

max_of_all_numbers(10,20,80)

#create min of all the values
def min_of_all_numbers(*args):
    print(min(args))

min_of_all_numbers(10,20,80)

print('************************************************************')
#pass argument as kwargs where we can pass parameter value as key and value pair
def keyword(**kwargs):
    print(kwargs)
    #print value of 2nd key pair
    print(kwargs.get('email'))
    print(kwargs['country'])

#when we call the function we can pass key and value pair
keyword(name = 'Jiten', email = 'log@ymail.com', country = 'Australia')
#it will give value as dictionary

print('************************************************************')
#Now in the function pass both the value as args and kwargs - it will print both the tuples and the dictionary
def hello_world(fname,*args, **kwargs):
    print(fname)
    print(args)
    print(args[1])
    print(kwargs)
    print(kwargs.get('country'))

#call the function by passing values as tuples and dictionary
hello_world(10,'Jiten',30,name = "Jitendra", age = 33, country = "Australia")
#first value will be assigned to the variable 
