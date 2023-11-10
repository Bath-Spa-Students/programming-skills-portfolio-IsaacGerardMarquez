# Practice 3: You need to make a program for a leader board. The program needs to output the numbers 1 to 9, each on a separate line followed by a dot.

# Create a for loop to iterate over the range of numbers from 1 to 10. The loop variable named "leaderboard" will then take on the values from 1 to 9 in each iteration.
for leaderboard in range(1, 10):

# Create a print() function to display or print the value of number.
# The "end" parameter is set to ".\n", which means that there will be a dot (.) printed after each number.
# The new line character, “\n”, is used so that each number will be printed each on a separate line.
    print(leaderboard, end=".\n")
