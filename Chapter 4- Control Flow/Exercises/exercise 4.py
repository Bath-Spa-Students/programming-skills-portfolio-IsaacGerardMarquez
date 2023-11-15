# Exercise 4: Stages of Life (Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:)
# •If the person is less than 2 years old, print a message that the person is a baby.
# •If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# •If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# •If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# •If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# •If the person is age 65 or older, print a message that the person is an elder.

# Assigning the value of 18 to the variable named "Age".
Age = 18

# If the variable named "Age" is less than 2, the message "This person is a baby." will be printed.
if Age < 2:
    print ("This person is a baby.")

# If the variable named "Age" is less than 4, the message "This person is a toddler." will be printed.
elif Age <4:
    print ("This person is a toddler.")

# If the variable named "Age" is less than 13, the message "This person is a kid." will be printed.
elif Age < 13:
    print ("This person is a kid.")

# If the variable named "Age" is less than 20, the message "This person is a teenager." will be printed.
elif Age < 20:
    print ("This person is a teenager.")

# If the variable named "Age" is equal to or greater than 20 but less than 65, the message "This person is an adult." will be printed.
elif Age >= 20 and Age < 65:
    print ("This person is an adult.")

# If the variable named "Age" is equal to or greater than 65, the message "This person is an elder." will be printed.
else:
    print ("This person is an elder.")