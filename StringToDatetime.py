import datetime
print((datetime.datetime.now()))
dt_string = "2022-9-14 9:03:43"
format = "%Y-%m-%d %H:%M:%S"
dt_object = datetime.datetime.strptime(dt_string, format)
print("Datetime: ", dt_object)
print("Minute: ", dt_object.minute)
print("Hour: ", dt_object.hour)
print("Second: ", dt_object.second)