#check the Method Over riding concepts in Python
import self


class A:
    def sum(self):
        print('Sum of Numbers coming from Parent Class ')


class B(A):



    def sum(self):
        # when we want to call the base child method inside the child claas

        # A.sum(self)
        # Alternatively we can call the parent class method by using the super keyword
        super().sum()
        print('Sum of Numbers coming from child class ')


#now create the object fo the class A
obj1 = A()
#obj1.sum()

#now create the object of the class B
obj2 = B()
obj2.sum()



#here the child class method will override the parent class Method

