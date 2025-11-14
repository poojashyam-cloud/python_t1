from datetime import datetime
now = datetime.now()
extract_all = lambda dt: (dt.date(), dt.time(), dt.year, dt.month)
print(extract_all(now))  # (date, time, year, month)