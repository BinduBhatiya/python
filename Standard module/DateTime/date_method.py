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
print(x.strftime("%B"))             # July