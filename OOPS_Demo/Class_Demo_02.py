class Person:
    #define the method inside the class - by default self keyword will be assigned
    def welcome(self):
        print("Hello Python")
    #self means Instance of the Current class
    def hello_world(self):
        #even we can call the parent class method with the help of self keyword
        self.welcome()
        print('Print Hello_World')

    #create the method inside the class with two parameters
    def sum(self, num1, num2):
        print(num1+num2)




#create the Object of the class
p1 = Person()
#pass the object name inside the Method Name by calling the class Name with the Method Name
#Person.hello_world(p1)
p1.hello_world()

p1.sum(10,20)


#Each object will have unique set of properties
p1.name = "Jiten"
p1.phone = 405009378
p1.country = "AUS"

#create a new object of the class
p2 = Person()
p2.name = "Kumar"
p2.phone = 4784512010
p2.country = "IND"
p2.city = "Sydney"

#now access the variable name with the object
print(p1.name)
print(p2.city)

#another way of accessing the object variable is by using the getattr method
print(getattr(p2,"name"))
