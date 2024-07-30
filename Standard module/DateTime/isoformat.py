# isoformat() method used to return the date and time in ISO formate.

import datetime

dt = datetime.datetime(2024, 7, 30, 14, 45, 30)
iso_datetime_custom_sep = dt.isoformat(sep=' ')

print(iso_datetime_custom_sep)  # Output will be '2024-07-30 14:45:30'
