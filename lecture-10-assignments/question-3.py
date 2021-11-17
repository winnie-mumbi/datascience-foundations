"""
Write a program that reads two numbers from the user and prints the product 
digit by digit. Each digit should be printed on a separate line. Hint: There are 
various  ways  to  do  this  (e.g.  using  mathematical  operations).  But  with  our 
current  programming  knowledge,  the  best  way  would  be  to  use  the  str() 
conversion function.
"""

def main():
    first_num = int(input("Enter first number: "))
    sec_num = int(input("Enter second number: "))

    product = first_num * sec_num

    for num in str(product):
        print(num)


main()