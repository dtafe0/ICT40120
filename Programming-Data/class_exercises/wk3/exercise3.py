# Exercise 3:
#
# Take user input for a number. Check if the number is Odd or Even, then print the result to the console.

while True:
    number = int(input("enter a number to check odd or even: "))
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
