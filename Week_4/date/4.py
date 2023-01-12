from datetime import datetime, timedelta

now = datetime.now()
week_before = now - timedelta(days=7,hours=5,minutes=30)

today = now.day
hour_today = now.hour
min_today = now.minute
sec_today = now.second

last = week_before.day
hour_last = week_before.hour
min_last = week_before.minute
sec_last = week_before.second

print(86400*(abs(today-last)) + 3600*abs(hour_today-hour_last) + 60*abs(min_today-min_last) + abs(sec_today-sec_last))

