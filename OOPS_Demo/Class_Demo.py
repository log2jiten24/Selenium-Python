class Person:
    #define the method inside the class - by default self keyword will be assigned
    def welcome(self):
        print("Hello Python")

    def hello_world(self):
        print('Print Hello_World')

def welcome_function():
    print("Function is called outside the class ")

 #to create object of the class -here p is the object name
p = Person()
p.welcome()
#call another object of the class
p.hello_world()

#Function is called without crating any object - and it is defined outside the class
welcome_function()



