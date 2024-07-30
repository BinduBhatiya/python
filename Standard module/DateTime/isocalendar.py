# isocalendar() is used to give the year,week number, and weekday.

import datetime

# Create a date object
date = datetime.date(2024, 7, 30)

# Get the ISO calendar date
iso_cal = date.isocalendar()

print(iso_cal)  # Output will be (2024, 31, 2)
