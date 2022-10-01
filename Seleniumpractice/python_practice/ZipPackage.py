#Example of Zip Package - avaialable inside the Python built in package

#zip function - it combines two list and give the result in one tuple

#to get all the built ins package or class available
print(dir(__builtins__))

print(zip)

name = ['Jiten' , 'Priya' ,'Aadya','Kumar']
marks_01 = [80 , 90 , 95]

#using zip function to combine two lists and form a tuple of elements combined together
combined_data = zip(name , marks_01)

#Now convert the tuples into the list - just pass the tuple inside the list -constructor values
lis_new = list(combined_data)
print(lis_new)

#to fetch the fist element
print(lis_new[0][1])

#now create a single list and the zip will work for single list
list_03 = [1 , 2 , 3.5]
print(list(zip(list_03)))

#create three list and try to combine more than two list
name = ['Jiten' , 'Priya' ,'Aadya','Kumar']
marks_01 = [80 , 90 , 95]
address = ['Pune' , 'Mumbai', 'Kolkata']

#using zip function to combine two lists and form a tuple of elements combined together
combined_data = zip(name , marks_01, address)

#Now convert the tuples into the list - just pass the tuple inside the list -constructor values
lis_new = list(combined_data)
print(lis_new)

#unzipping the tuples and assigning to different variables :-
x, y , z = zip(*lis_new)
print('Fist tuple values', x)
print('Second tuple values', y)
print('Third  tuple values', z)