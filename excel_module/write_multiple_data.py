from openpyxl import workbook
from openpyxl.workbook import Workbook

wb = Workbook()
#create the workbook
#give the Sheet Name
wb['Sheet'].title = "Automation Report"
#active the cell -workbook
sh1 = wb.active

#to update multiple records in the excel
#create the data - to update multiple values - tuples inside the list
data = [('Number', 'Name', 'Marks'), (1,'Jitu', 90),(2,'Python',100),(3,'Priya',200)]

for i in data:
    sh1.append(i)

wb.save("FinalReport_New_Update.xlsx")
