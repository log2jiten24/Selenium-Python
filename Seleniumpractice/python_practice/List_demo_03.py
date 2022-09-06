#indexing and slicing in list

list_01 = [10,"Jiten", 10.5, True,10,10]
#extend keyword to combine values of two list

list_02 = [30,"Kumar"]

list_01.extend(list_02)
print(list_01)

#pop method to remove the elements-if we dont give index then it will remove the last element
list_01.pop()
print(list_01)

list_01.pop(2)
print(list_01)

#reverse the elements inside the list
list_01.reverse()
print(list_01)


print("*********************************************************************************************")
#to create list of list
list_upd = [10,20, ["Java","Selenium"],24]
print(list_upd)

#to get the values inside the list of list
print(list_upd[2][1])
#it will give output as Selenium


#to create the List in another way by passing list inside the List - constructor
list_03 = list([10,20,30])
print(list_03)