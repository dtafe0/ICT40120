# Exercise 7:
# Write a program that simulates the roll of two six sided dice.
# the program should ask the user to guess the total sum of the dice.
# The user has to keep guessing until they get the total correct,
# and the program should tell them how many tries it took.
# An example of the expected output is shown below.
# What do you think the total of two six-sided die will be? 6
# The total was 8. Try again!
# What do you think the total of two six-sided die will be? 4
# The total was 11. Try again!
# What do you think the total of two six-sided die will be? 10
# The total was 10. Congratulations! It took you 3 tries to guess successfully.
import random

x=1
while True:
    rand_num = random.randint(2, 12)
    number = int(input("What do you think the total of two six-sided die will be?"))

    if rand_num == number :
        print(f'The total was {number}. Congratulations! It took you {x} tries to guess successfully.')
        x=1
    else:
        print(f'The total was {rand_num}. Try again!')
        x += 1