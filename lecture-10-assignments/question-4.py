"""
Assume  that  we  number  the  lower-case letters  starting  from  1:  ‘a’=1,  ‘b’=2, 
etc. Write a program that finds the sum of the number values of the letters of 
a word that the user enters.
"""
def main():
    message = input("Enter a word: ")

    # make all letters lower case
    formattedMsg = message.lower()

    letters = 'abcdefghijklmnopqrstuvwxyz'

    result = 0
    for char in formattedMsg:
        # ignore any digit entered by user
        if char.isalpha():
            result += (letters.index(char) + 1)

    print(result)


main()