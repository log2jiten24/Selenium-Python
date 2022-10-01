
import  os

# open the file with the help of context manager :-
#by default - open method will open the file in read only mode

#with the help of os - package - inside the package - we have getcwd method to get the current  directory
file_path = os.getcwd()
print('Current Directory ', file_path)


with open(os.path.dirname(file_path)+"\\Demo1.txt") as f:
    #get the current status of the file
    print('Current status of the file : ', f.closed)
    #read the content of the file
    data = f.read()
    #read the content of the file
    print(data)

#as soon as cwe come out of the with block it will close the file
print('Status after coming out of with stmt : ', f.closed)


