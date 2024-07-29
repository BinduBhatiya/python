import datetime
my_date = datetime.date(2024, 7, 29)
print("Date:", my_date)             # Date: 2024-07-29


print("Year:", my_date.year)        # Year: 2024
print("Month:", my_date.month)      # Month: 7
print("Day:", my_date.day)          # Day: 29


today = datetime.date.today()
print("Today's date:", today)       # Today's date: 2024-07-29


my_time = datetime.time(14, 30, 45)  
print("Time:", my_time)             # 14:30:45


print("Hour:", my_time.hour)        # Hour: 14
print("Minute:", my_time.minute)    # Minute: 30
print("Second:", my_time.second)    # Second: 45
print("Microsecond:", my_time.microsecond) # Microsecond: 0


my_datetime = datetime.datetime(2024, 7, 29, 14, 30, 45)
print("Datetime:", my_datetime)     # Datetime: 2024-07-29 14:30:45


delta = datetime.timedelta(days=5, hours=3, minutes=30)
print("Timedelta:", delta)          # Timedelta: 5 days, 3:30:00
 

future_date = today + delta
print("Future date:", future_date)  # Future date: 2024-08-03

past_date = today - delta
print("Past date:", past_date)      # Past date: 2024-07-24


formatted_date = my_date.strftime("%Y-%m-%d")
print("Formatted date:", formatted_date)    # Formatted date: 2024-07-29

formatted_time = my_time.strftime("%H:%M:%S")
print("Formatted time:", formatted_time)    # Formatted time: 14:30:45

formatted_datetime = my_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime:", formatted_datetime)    # Formatted datetime: 2024-07-29 14:30:45


date_str = "2024-07-29"
parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
print("Parsed date:", parsed_date)      # Parsed date: 2024-07-29







