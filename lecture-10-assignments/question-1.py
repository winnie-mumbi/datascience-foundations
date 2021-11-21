"""
    Write a program that prints a table as shown below which lists powers of 2 
    and  1/x  for  numbers  1  to  10.  Column  alignment,  space  between  columns, 
    and digit formats should be as shown below.
        1       2       1.000
        2       4       0.500
"""

def main():
    for x in range(1,11):
        power = 2**x
        divided_x = 1/x
        print("{0}\t{1}\t{2:0.3f}".format(x,power,divided_x))


main()