import datetime

time = datetime.datetime.now()

print("The current date is ...")
print(time.strftime("%y / %m / %d"))
print("The current time is ...")
print(time.strftime("%I / %M / %S"))
print(" ")
print("Or simply")
print(" ")
print (time)
print(" ")