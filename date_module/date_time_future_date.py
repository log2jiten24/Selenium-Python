import datetime
import pytz
#from datetime import datetime

#get the todays date
today = datetime.date.today()

print(type(today))

tday = '27 September 2022'
print(type(tday))

#converting string to date time object
date_object = datetime.datetime.strptime(tday,'%d %B %Y')
print('Converting String to Date Object', date_object)

#get the day , month , and year
print(today)
print(today.day)
print(today.month)
print(today.year)

#if we want to increase the number of current days to 14 days - with the help of time delta we can increase the number of days

tdelta = datetime.timedelta(days= 14)
print('Final Date : ', today + tdelta)

#increase the date for  a string
print('Final Date_01 - String to Date  : ', date_object + tdelta)

final_date = today + tdelta
print(final_date.strftime("%d %B %Y"))

#decrease the date
final_date = today - tdelta
print(final_date.strftime("%d %B %Y"))

#final_date_01 = date_object + tdelta
# print(final_date_01.strftime("%d %B %Y"))

#print(today.strftime('%B'))

#get the birthday date
bday = datetime.date(2023,3,24)
till_bday = today - bday
print(till_bday.days)
