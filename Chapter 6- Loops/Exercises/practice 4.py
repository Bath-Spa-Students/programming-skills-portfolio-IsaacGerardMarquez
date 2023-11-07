# Practice 4: Write a Python program that uses the break statement to exit a for loop when a specific condition is met.

# Python Program to terminate the for loop after a certain number of iterations.
# We have used the for loop to print the value of i. 
for i in range(18):

# When i is equal to 14, the break statement terminates the loop. 
    if i == 14:
        break

# Hence, the output doesn't include values after 13.
    print(i,end=" ")