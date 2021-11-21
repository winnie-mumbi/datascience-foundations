"""
A simple type of secret code can be done by replacing each character with 
a corresponding different character. Let’s assume we want to replace each 
character  with  the  character  that  is  5  ahead  of  it  in  the  ASCII  code  table 
(e.g:  ord(‘A’)=65;  65+5=70;  chr(70)=’F’.  So,  we  will  replace  character  ‘A’ 
with character ‘F’ in our code). Write a program that reads a sentence from 
the user and outputs  a new string that  is produced using the secret  code 
described above (there shouldn’t be any extra space between characters in 
the output).

"""

def encoder():
    message = input("Enter a message: ")

    for char in message:
        code = ord(char)
        new_letter = chr(code + 5)
        print(new_letter,end="")
        

encoder()