import time

# epoch =   a date and time from which a computer measures system time
print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string

print(time.time()) # return current seconds since epoch

print(time.ctime(time.time()))

# Convert seconds since the Epoch to a time tuple expressing local time. 
# When 'seconds' is not passed in, convert the current time instead.
lcl_time_object = time.localtime()
print(lcl_time_object)
gmt_time_object = time.gmtime()
print(gmt_time_object)
# Convert a time tuple to a string according to a format specification. 
# See the library reference manual for formatting codes. 
# When the time tuple is not present, current time as returned by localtime() is used.
lcl_time_object = time.strftime("%B %d %Y %H:%M:%S", lcl_time_object) 
gmt_time_object = time.strftime("%B %d %Y %H:%M:%S", gmt_time_object)
print(lcl_time_object)
print(gmt_time_object)




time_string = "20 April, 2020"
# Parse a string to a time tuple according to a format specification.
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2022, 2, 17, 12, 31, 32, 0, 0, 0)

# Convert a time tuple to a string
time_string = time.asctime(time_tuple)
print(time_string)

# Convert a time tuple in local time to seconds since the Epoch.
time_string = time.mktime(time_tuple)
print(time_string)
