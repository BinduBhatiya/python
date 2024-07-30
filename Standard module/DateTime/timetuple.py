# timetuple() is used to give the data in tuple formate.

import datetime

dt = datetime.datetime(2024, 7, 30, 14, 45, 30)
tt = dt.timetuple()

print(tt)

# time.struct_time(tm_year=2024, tm_mon=7, tm_mday=30, tm_hour=14, tm_min=45, tm_sec=30, tm_wday=1, tm_yday=212, tm_isdst=-1)
