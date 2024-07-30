# fromordinal() is used to convert ordinal number into date.

import datetime

# Ordinal for January 1, 2024
ordinal = 737791
date = datetime.date.fromordinal(ordinal)

print(date)  # Output will be 2024-01-01
