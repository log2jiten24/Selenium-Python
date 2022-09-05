#demonstrate the use of Constructor

class Person_02:
    def __init__(self, fname, lname):
        print('Hello Word Constructor')
        self.fname = fname
        self.lname = lname
        print("First Name is : " +self.fname + " " + "Last Name is : " +self.lname)

    #create the sum method to pass two parameters x and y
    def sum(self, x , y):
        #assign the values using the self keyword
        self.v1 = x
        self.v2 = y

        return  x + y




#when we create object of the class - by default the constructor is called and while calling it invoked the statement
#inside the constructor
x = Person_02('Kumar', 'Jitendra')

#Now create another object of the class

y = Person_02('Jiten' ,'Jeet')
#again the same constructor will be invoked

#call the method
print(x.sum(10,20))
