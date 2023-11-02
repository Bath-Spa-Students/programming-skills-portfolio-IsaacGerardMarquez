#Q2: Write a python program that takes courses marks as input and then calculates average of all the courses. After calculating the average, calculate the percentage of a student using total marks. Assume the total of all the courses marks is 500 or take the total marks from the user as input.

print ("Enter Courses Marks: ")

# Creating an input function
Code_Lab_1 = float (input ())
Digital_Visual_Design = float (input ())
Digital_Storytelling = float (input ())

# Creating a program that would calculate the total, average, and percentage
total = Code_Lab_1 + Digital_Visual_Design + Digital_Storytelling
average = total / 3.0
percentage = (total / 500.0) * 100

# Displaying or printing the final output
print ("\nThe Total marks for all the courses is:   \t", total, "/ 500.00")
print ("\nThe Average marks for all the courses is: \t", average)
print ("\nThe Percentage (%) for all the courses is:    \t", percentage, "%")