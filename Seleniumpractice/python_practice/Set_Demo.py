#set will have unordered ,no duplicate values , no Index and Slicing
my_set = {10,"Jiten", True , 10.4,10,10}

print(my_set)

#addition of elements
my_set.add(25)
print(my_set)

#pop - removal of elements -it will random remove any element
my_set.pop()
print(my_set)

#to remove specific value
my_set.remove(10.4)
print(my_set)

#lenght of the set
print(len(my_set))

#creating set - the constructor and inside the set pass the list
set_01 = set({"Jiten, 10,True,30.5"})
print(set_01)
