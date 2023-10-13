#Exercise 5: USB Shopper (A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each. Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left. You will to use the arithmetic operators to complete this exercise.)

import math

Budget= 50
Price = 6

Number_of_USB_Sticks_She_Can_Buy = (round(Budget/Price))
print (f"The number of USB Sticks she can buy is {Number_of_USB_Sticks_She_Can_Buy}.")

How_Many_Pounds_She_Has_Left = (Budget-(Price*Number_of_USB_Sticks_She_Can_Buy))
print (f"The amount of pounds she has left is £{How_Many_Pounds_She_Has_Left}.")