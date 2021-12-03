"""
Modify your program so that it first reads a letter from the user, and then prints only the lines 
where the name starts with that letter. Handle the lower/upper case issue.
EXTRA: Let the user search with a longer string. E.g. Search with Ah instead of A

"""

# first reads a letter from the user, and then prints only the lines where the name starts with that letter
def search_name_1():
    infile = open("names.txt","r")

    letter = input("Enter a letter: ")
    letter = letter.upper()

    found = False

    for s in infile:
        line = s.strip()

        if line[0] == letter:
            print(line)
            found = True
    
    if not found:
        print(f"No person with name starting with letter {letter} found")
    
    infile.close()

# user can search with a longer string
def search_name_2():
    infile = open("names.txt","r")

    letters = input("Enter first few letters of a name: ")

    found = False

    count = len(letters)
    letters = letters[0].upper() + letters[1:].lower()

    for s in infile:
        line = s.strip()
        if line[:count] == letters:
            print(line)
            found = True
    
    if not found:
        print(f"No person with name starting with {letters} found")
    
    infile.close()
    

search_name_1()
search_name_2()