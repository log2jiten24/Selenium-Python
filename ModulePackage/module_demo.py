import calendar
import math
import os

# write the package name inside the module name
import ModulePackage.Module_demo_02



result = calendar.month(2022,9)
print(result)

result_01  = calendar.monthcalendar(2022,10)
#print(result_01)

#get the current work directory
print(os.getcwd())
#get the Math Module
print(math.sqrt(10))

#call the method
ModulePackage.Module_demo_02.print_hello()

