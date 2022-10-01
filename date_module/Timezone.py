import datetime

#give the time format in hours , minutes , seconds , and microseconds
t = datetime.time(9, 30 , 45 , 100000)

print(t)
#get the specific hour
print(t.hour)

#now pass the entire date time
#pass the entire date time in year , day , month , hours , minutes , seconds , milliseconds
new_time = datetime.datetime(2022 , 9, 27 , 12, 30 , 34 , 10000)
print('New time is ',  new_time)

#now get the specific date
print('Date time ' , new_time.date())

#now get the specific time
print('Time Item ' , new_time.time())

tdelta = datetime.timedelta(hours= 24)

new_time_01 = new_time + tdelta
print(new_time_01)