"""
Write a program that writes to a file the numbers from 1 to 100, and their 
squares and square roots, as a table as shown below. Calculate the width of 
columns and use the appropriate format options when writing the numbers. 
Write the square root with 3 digits after the decimal point.
"""
import math
import os
def main():
    # get current working directory
    dirpath = os.path.dirname(__file__)
    outFile = open(os.path.join(dirpath,"squares-and-roots.txt"),'w')

    for num in range(1,101):
        square = num ** 2
        square_root = math.sqrt(num)
        
        print("{0}{1:10d}{2:10.3f}".format(num,square,square_root),file=outFile)
    
    outFile.close()

main()