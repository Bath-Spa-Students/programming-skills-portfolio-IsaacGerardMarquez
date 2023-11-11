#Exercise 5: USB Shopper (A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each. Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left. You will to use the arithmetic operators to complete this exercise.)

# I assigned the variable "Budget" to have the value 50 and the variable "Price" to have the value of 6.
# These variables represent the available budget and the price of a USB stick.
Budget= 50
Price = 6

# Calculating the number of USB Sticks that can be purchased within the given budget.
# The quotient is calculated by dividing "Budget" by the "Price".
# Use the round() function to round the quotient to its nearest whole number.
Number_of_USB_Sticks_She_Can_Buy = (round(Budget/Price))

# Use print() function that uses a f-string format to display a message that shows the number of USB Sticks she can buy.
print (f"The number of USB Sticks she can buy is {Number_of_USB_Sticks_She_Can_Buy}.")

# Calculating the amount of money left after purchasing the USB Sticks.
# The total cost of the purchased USB Sticks is subtracted to the budget.
How_Many_Pounds_She_Has_Left = (Budget-(Price*Number_of_USB_Sticks_She_Can_Buy))

# Use print() function that uses a f-string format to display a message that shows the amount of pounds she has left.
print (f"The amount of pounds she has left is £{How_Many_Pounds_She_Has_Left}.")