#now lets create the zip function with the set of values

set_01 = {"Jitu" , "Jeet" ,"Jiten"}
set_02 = {250 , 560 , 254}
set_03 = {"Kokata" , "Pune" ,"Mumbai"}

#convert the combine of sets to tuples
list_01 = list(zip(set_01, set_02,set_03))
print(list_01)


#unpacking the zip and tuples
a,b,c = zip(*list_01)
print(a)
print(b)
print(c)
