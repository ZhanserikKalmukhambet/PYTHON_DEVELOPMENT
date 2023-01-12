from datetime import datetime

now = str(datetime.now())

dot = now.index('.')

print(now[:dot])