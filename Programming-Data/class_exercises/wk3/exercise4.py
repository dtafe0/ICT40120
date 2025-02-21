# Exercise 4:
#
# Write a program that reads in the user name and test if its first
# character is a vowel (a, o, I, e or u). if it is a vowel a display
# “the first character is a VOWEL” message, otherwise display a message
# “the first character is a CONSONANT”

def isvowel(n):
    match n:
        case 'a'|'o'|'i'|'e'|'u'|'A'|'O'|'I'|'E'|'U':
            return True
        case _:
            return False


while True:
    username = input("enter username: ")
    if isvowel(username[0]):
        print("the first character is a VOWEL")
    else:
        print("the first character is a CONSONANT")
