#create the tuple
tupl_demo = (1 ,"Jiten" , True, 10.5, "AADYA", 1, 1 )
print(tupl_demo)
#to print the last item of the tuple using the index
print(tupl_demo[4])

#it will give the value from the last ,here -2 will give the value from the second list
print(tupl_demo[-2])

#to count the item inside the tuple for the particular item
#it is printing 1 count as 4 ,inspite of having 1 as 3 because python treats 1 as True
print(tupl_demo.count(1))

#to check the slicing - particular range
print(tupl_demo[1:5])

#to know the index of the particular element inside the tuple
#it will give index value as 1
print(tupl_demo.index('Jiten'))

print('****************************')
#it will give error as tuple is immutable as we cannot insert any new value inside the tuple
#tupl_demo[0] = 'Priya'
#print(tupl_demo)

print(type(tupl_demo))
#it will give output as class<'tuple'>
