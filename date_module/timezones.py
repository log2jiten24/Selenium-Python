import  datetime
import pytz


# dt_today = datetime.datetime.today()
# dt_now   = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()
#
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

dt = datetime.datetime(2022 , 9 , 27 , 12 , 23 , 45 , tzinfo = pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz = pytz.UTC)
print(dt_now)

dt_UTC = datetime.datetime.utcnow().replace(tzinfo = pytz.UTC)
print(dt_UTC)

# for tz in pytz.all_timezones:
#     print(tz)
dt_mtn = dt_UTC.astimezone(pytz.timezone('Australia/Sydney'))
print(dt_mtn)

#convert the date time to specific format using the strftime
new_dt_time = dt_mtn.strftime('%d %B %Y')
print('new date time : ' , new_dt_time)

str_time = '27 September 2022'
#convert the String date to the date object

date_obj = datetime.datetime.strptime(str_time, '%d %B %Y')
print('Converting String to Date Obj :', date_obj)

tdelta = datetime.timedelta(days = 14)

date_obj_02 = date_obj + tdelta
print('New Date time adding 14 days : ' , date_obj_02.date())

#strftime - it converts the datetime obj to string
#strptime - it converts the string to date time object