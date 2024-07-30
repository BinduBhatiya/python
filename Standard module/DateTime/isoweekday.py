# isoweekday() return the index of day.

import datetime

date = datetime.date(2024, 7, 30)
iso_weekday = date.isoweekday()

print(iso_weekday)  # Output will be 2, since 2024-07-30 is a Tuesday
