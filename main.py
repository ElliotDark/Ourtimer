import datetime

time = datetime.datetime.now()
relationships_start = datetime.datetime(year=2021,month=7,day=2,second=time.second,microsecond=time.microsecond)
print(time)
print(relationships_start)
diff_time = time - relationships_start
print("Our relationships timer was start", diff_time, "min")
