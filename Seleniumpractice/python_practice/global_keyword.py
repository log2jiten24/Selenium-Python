a = 10

def something():
    # a = 20
    global a
    a = 15 #now this global variable will be set for a

    b = 10
    #if we comment local variable inside the function - then the global variable can be accessed
    print("in func", a , b)

    #with the help of globals keyword we can access only global variable
    globals()['a'] = 13

#call the function
something()

#once we declare the variable as a , then it will be assigned the variable to inside and outside the variable
print("outside", a)
