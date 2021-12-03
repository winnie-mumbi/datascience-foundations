"""
Modify your program so that it prints only the lines where the name starts with the letter “A”
"""

def search_name():
    infile = open("names.txt","r")

    for s in infile:
        # remove leading and trailing spaces and newlines
        line = s.strip()
        if line[0] == 'A':
            print(line)
    
    infile.close()


search_name()