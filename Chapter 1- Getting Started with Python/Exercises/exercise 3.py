#Exercise 3: Print date and Time (Write a Python program to display the current date and time.)

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