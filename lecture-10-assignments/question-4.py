"""
Assume  that  we  number  the  lower-case letters  starting  from  1:  ‘a’=1,  ‘b’=2, 
etc. Write a program that finds the sum of the number values of the letters of 
a word that the user enters.
"""
def main():
    message = input("Enter a word: ")

    # make all letter lower case
    formatted_msg = message.lower()

    letters = 'abcdefghijklmnopqrstuvwxyz'

    result = 0
    for char in formatted_msg:
        # ignore any digit enter by user
        if char.isalpha():
            result += (letters.index(char) + 1)

    print(result)


main()