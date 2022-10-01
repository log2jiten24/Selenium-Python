import datetime

current_time = datetime.datetime.now()
#it will give output as Week name in capital letters
print(current_time.strftime('%A'))

#it will give week name in short
print(current_time.strftime('%a'))

#it will give full month name
print(current_time.strftime('%B'))

#it will give the current year format -yyyy
print(current_time.strftime('%Y'))

#to convert the date
print(current_time.strftime("%H_%M_%S_%d_%B_%Y"))
print(current_time.strftime("%d %B %Y"))

date_time = current_time.strftime("%d %B %Y")
print(type(date_time))

