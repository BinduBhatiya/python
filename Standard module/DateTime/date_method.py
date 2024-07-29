# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

# exercise 1:
import datetime
x = datetime.datetime.now()
print(x)                    # 2024-07-28 15:30:40.559312


# exercise 2:
import datetime
x = datetime.datetime(2024, 5, 30)
print(x)                    # 2024-05-30 00:00:00


# strftime():
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

import datetime
x = datetime.datetime(2024, 7, 6)
print(x.strftime("%a"))             # sat(Weekday, short version)
print(x.strftime("%A"))             # saturday(Weekday, full version)
print(x.strftime("%w"))             # 6(Weekday as a number 0-6, 0 is Sunday)
print(x.strftime("%d"))             # 06(Day of month 01-31)
print(x.strftime("%b"))             # Jul(Month name, short version)
print(x.strftime("%B"))             # July(Month name, full version)
print(x.strftime("%m"))             # 07(Month as a number 01-12)
print(x.strftime("%y"))             # 24(Year, short version, without century)
print(x.strftime("%Y"))             # 2024(Year, full version)
print(x.strftime("%H"))             # 00(Hour 00-23)
print(x.strftime("%I"))             # 12(Hour 00-12)
print(x.strftime("%p"))             # AM(AM/PM)
print(x.strftime("%M"))             # 00(Minute 00-59)
print(x.strftime("%S"))             # 00(Second 00-59)
print(x.strftime("%f"))             # 0000(Microsecond 000000-999999)
print(x.strftime("%j"))             # 188(Day number of year 001-366)
print(x.strftime("%U"))             # 26(Week number of year, Sunday as the first day of week, 00-53)
print(x.strftime("%W"))             # 27(Week number of year, Monday as the first day of week, 00-53)
print(x.strftime("%c"))             # Sat Jul  6 00:00:00 2024(Local version of date and time)
print(x.strftime("%C"))             # 20(Century)
print(x.strftime("%x"))             # 07/06/24(Local version of date)
print(x.strftime("%X"))             # 00:00:00(Local version of time)