# Exercise 5:
# Write a program that prompts the user for a color.
# If the value is "green" or "orange", print "You win."
# Otherwise display "Sorry!".

while True:
    color = input("enter a color: ")
    if color == 'green' or color == 'orange':
        print("You win")
    else:
        print("Sorry!")