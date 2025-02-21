# Exercise 6:
# Write a “fortune-telling” program that prompts the user to enter the following for input:
# •	favourite number from 1 to 50
# •	favourite colour out of red, grey or black.
# •	a floating point number from 1 to 10.
# Based on the following chart, respond as appropriate.
# Less than 9	or Less than ‘grey’ and equal to 8.43 “You will win the lottery soon”
# not equal to 10	and	equal to ‘red’ or less than or equal to 1.79 “You will live to 110”
# greater than/ equal to 26 and equal to ‘black’ or equal to 8.2 “You will become the next prime minister”
# Then print the fortune to the console.
# For an else statement, print “I cannot read your fortune”
# If you complete the exercise, try adding additional statements to this program.
# *You should fully parenthesize your logical expressions in order to make sure it is clear what you mean.
# In this exercise, always prioritize the first two statements and then connect that result to the last statement.

while True:
    number = int(input("enter your favourite number from 1-50: "))
    colour = input("enter your favourite colour out of red, grey or black: ")
    floater = float(input("enter your favourite floating point number from 1-10: "))

    if (number < 9 or colour != 'grey') and floater == 8.43:
        print('You will win the lottery soon')
    elif (number != 10 and colour == 'red') or floater <= 1.79:
        print('You will live to 110')
    elif (number >= 26 and colour == 'black') or floater == 8.2:
        print('You will become the next prime minister')
    else:
        print('I cannot read your fortune')