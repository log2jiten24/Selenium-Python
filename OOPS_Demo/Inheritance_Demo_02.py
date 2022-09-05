#Example of Multi Level Inheritance

class A:
    def methodA(self):
        print('Calling Method from Class A')

    def hello_world(self):
        print('Calling Hello World from Class A ')

class B(A):
    def methodB(self):
        print('Calling Method from Class B')

    def hello_world(self):
        print('Calling Hello World from Class B')

class C(B):
    def methodC(self):
        print('Calling Method from Class C ')

    def hello_world(self):
        print('Calling Hello World from Class C')

#here the Class C extends Class B and Class B is extending Class A
obj = C()
#with the object of C - we can access all the methods of the Class A , Class B and Class C
obj.methodA()
obj.methodB()
obj.methodC()
#Access the Parent Class Method from the Child Class - C Object
obj.hello_world()



