
#write the file content- by default once we come out of the with statement file will close

with open('Demo3.txt', 'w') as fw:
    fw.write('Write the Lines of Python code')

#append the lines of code

with open('Demo3.txt' , 'a') as fw:
    #writing in new line
    fw.write("\n")
    fw.write('Write the updating lines of code')
    #\t it will add additional space bwtween the lines
    fw.write("\n")
    fw.write("\t")
    fw.write("Writing again with new line of code")

#to override the lines - with new line
#with open('Demo3.txt' , 'w') as fw:
    #fw.write('Updating  the lines of code')