tupl_demo = (1 ,"Jiten" , True, 10.5, "AADYA", 1, 1 )
#to convert tuple to list
#pass the tuple inside the list - constructor
list_new  = list(tupl_demo)
print(type(list_new))

print(list_new)

#in the same way convert tuple into the set
#set does not allow duplicate and set is unordered and it doesnt follow index
set_01 = set(tupl_demo)
print(type(set_01))
print(set_01)

print('**************************************************')
#if we give single value inside the tuple then it will act as String and it will give length
#as sequence of characters
#when we give multiple values inside the tuple then it will give correct lenth
tuple_01 = ('Jitendra')
print(len(tuple_01))
#its giving length as 8 as its calculating all the sequence of characters
tuple_02 = ('Jiten','Aadya')
print(len(tuple_02))
#here it will give length as 2

print('**************************************************')
#to create the list of tuples - to give multiple tuples inside the list
my_tuple_03 = [(1,"Jiten",10.5),(2,"Aadya",3.2),(3,"Priya", 78.2)]
#it will give the first tuple values
print(my_tuple_03[0])
#this will give value as Jiten inside the tuple
print(my_tuple_03[0][1])

print(my_tuple_03[1][2])
print(my_tuple_03[2][1])
print('**************************************************')
#to create tuple by calling the tuple constructor
my_tup = tuple([1,"Jiten",10.5,30])
print(type(my_tup))
#this will give the tuple values
print(my_tup)


print('**************************************************')
#tuple unpacking where we can assign each variable values to different values to the tuple
t1 = ('Jiten', 'Aadya','Priya')
x,y,z = t1
#assigning each variable to the each value inside the tuple
print(x)
print(y)
print(z)




