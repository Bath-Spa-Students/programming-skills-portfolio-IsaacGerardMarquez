# Practice 1: Write a Python program that uses a while loop to print the even numbers from 2 to 10

print ("The even numbers from 2 to 10 are: ")

# The variable "loop" has a value of 2.
loop = 2

# A while loop is used with the condition that it will run until the value will be less than or equal to the value of "loop".
while loop <= 10:

# It checks a condition whether the remainder of loop/2 is 0 or not. Then, if it is 0, it will be printed. If not, then it will not be printed.
    if loop % 2 == 0:

# The "end=” ” shows that each print value will be printed in the same line.
        print(loop, end=",")

# Shows that "loop's" value will increment by 1 after one print is done.
    loop+=1