#Constructor Over Riding

class A:

    #create a default constructor inside Class A
    def __init__(self):
        print('Default Constructor of Class A')

#Inherit class A from Class B
class B(A):
    #create default constructot inside class B

   def __init__(self):

       #this will call the parent class constructor
       #A.__init__(self)

       #Another way of doing it is by using the super keyword
       super().__init__()
       print('Default Constructor of Class B')

#create Object of the class A - by default the constructor inside the class A will be invoked
#obj1 = A()

obj2 = B()
#create Object of the class B - by default the constructor inside the class B will get executed



