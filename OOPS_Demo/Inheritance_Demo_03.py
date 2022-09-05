#Example of Multiple Inheritance in Python

class classA:
    def methodA(self):
        print('Calling Method from Class A')


class classB():
    def methodB(self):
        print('Calling Method from Class B')


#Example on how to extend Multiple Classes at One time
class classC(classA,classB):
    def methodC(self):
        print('Calling Method from Class C ')

#create Object of the Class C
obj1 = classC()

#Now we can access all the Methods of the class A and Class B
obj1.methodC()
obj1.methodB()
obj1.methodA()

#type the MRO - we will get to know the Order Sequence in which the Classes are going to be called

print(classC.mro())

#[<class '__main__.classC'>, <class '__main__.classA'>, <class '__main__.classB'>, <class 'object'>]