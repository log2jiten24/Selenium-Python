#indexing and slicing in list

list_01 = [10,"Jiten", 10.5, True,10,10]
#to get specific position inside the list
print(list_01[3])
print(list_01[-2])
#to get the count of specific elements inside the list
print(list_01.count(10))

#slicing - to start the list count from specific element -it will print end
print(list_01[0::])
#slicing - from one start till specific element
print(list_01[1:5])

#to replace particular value inside the list
list_01[1] = "AADYA"
print(list_01)

#to insert additional elements inside the list - to add - use sppend method
list_01.append("PRIYA")
print(list_01)

#to insert additional elements at particular position
list_01.insert(2,"PRIYAJEET")
print(list_01)

