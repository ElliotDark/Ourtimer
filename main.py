import datetime

time = datetime.datetime.now()
relationships_start = datetime.datetime(year=2021,month=7,day=2)
print(time)
print(relationships_start)
diff_time = time - relationships_start
print(diff_time)