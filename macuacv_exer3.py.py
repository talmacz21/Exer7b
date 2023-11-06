seconds_past_midnight = 63252
hours = seconds_past_midnight // 60**2
minutes = (seconds_past_midnight % 60**2) // 60
seconds = seconds_past_midnight % 60

time_str = str(hours)+ ":"+ str(minutes) + ":" + str(seconds)
print(time_str)