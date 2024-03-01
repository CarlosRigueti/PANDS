# Rounds a number.
# Be careful of round, it rounds to the nearest even number 
# eg 4.5 rounds to 4,
# but 5.5  rounds to 6,
# So do not use it accuracy is essential.
# Author: Carlos Rigueti

numberToRound = float(input("enter a float number:"))
roundedNumber = round(numberToRound)
print ( '{} rounded is {}'.format(numberToRound,roundedNumber))