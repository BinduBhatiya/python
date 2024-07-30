# toordinal() is used to convert date into ordinal number.

import datetime

date = datetime.date(2024, 7, 30)
ordinal = date.toordinal()

print(ordinal)  # Output will be 738001


# find the difference between two date.

import datetime

date1 = datetime.date(2024, 7, 30)
date2 = datetime.date(2023, 7, 30)

res = date1.toordinal() - date2.toordinal()
print(res)                                      # 366 (it means 2024 is leap year.)

