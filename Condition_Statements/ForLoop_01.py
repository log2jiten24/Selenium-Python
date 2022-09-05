#string is a sequence of characters
name ='Python'
#it will print each character of the string
for a in name:
    print(a)

l1_marks = [70,80,90,100]
final_marks =0
for marks in l1_marks:
    #Concatenation is only done with the help of String
    #print("Each Marks :" +str(marks))
   final_marks = final_marks + marks
print("Final Marks is :"+str(final_marks))

#Example of Not In Operator - to check over the String is not present inside the list
list_01 = ["Apples" , "Mangoes" ,"Oranges"]
print("Pineapples" not in list_01)
#this will give boolean list as True

print('***********************************************')
#Iterate over the dictionary
dict_01 = {'name': 'Jiten' , 10 :'AADYA' , 'hasMarried': False}

#Iterate over the key and value pair
for k,v in dict_01.items():
    print(k,v)

my_dictionary = dict(QA="Jitu", Dev="Akash", qa="AAdya")
#getting all the keys and values from the dictionary
for k,v in my_dictionary.items():
    print("Each key :" +str(k) + " " + "Each Value is :" +str(v))

#getting all the values
for value in my_dictionary.values():
    print("All values present :" +str(value))

#iterate over the range between 0 to 10
#for x in range(0,10):
   #print(x)

#iterate over the range and get the list of even and odd numbers
evenlist = []
oddlist  = []
for x in range(50):
    if x%2 ==0:
        evenlist.append(x)
else:
    oddlist.append(x)
#print the list
print(evenlist)
print(oddlist)

#Iterate over the two For Loops
l1 = ['Java' ,'Python' ,'Ruby']
l2 = ['Jiten','AADYA','Priya']
l3 = ['Ind' ,'Aus', 'SA']

for a in l1:
    for b in l2:
        for c in l3:
            print(a + " " + b + " " + c)


#first here the outer loop will execute and then it it will execute each element for the second loop

print('******************************************')
#Work with tuples
t1 = (1,2,3)
t2 = (50,60,70)
t3 = (80,90,100)
#create the list having all the tuples
list_01 = [t1,t2,t3]
print(list_01)

for x in list_01:
    #it will print each tuples element  inside the list
    print(x[0])
    print(x[1])
    print(x[2])

#now do it in alternate way
for x,y,z in list_01:
    print(x)
    print(y)
    print(z)