class Base:
    name = "Jiten"
    def basemethod(self):
        print('I am in Base or Parent Class')

class Child(Base):
    Company = "Alexa"
    def childmethod(self):
        print('I am in Child Class')

#create the Object of the Class Child
c = Child()

#Access the Method of the Child Class -objectname.Method Name
c.childmethod()
c.basemethod()
print(c.name)
print(c.Company)


#create the object of the base class and access the Base Class Method
b = Base()
b.basemethod()

