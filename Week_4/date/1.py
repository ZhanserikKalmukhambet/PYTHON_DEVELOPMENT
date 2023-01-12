from datetime import datetime, timedelta

now = datetime.now()

d2 = now - timedelta(days=5)
print(d2)