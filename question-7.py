#  A program that finds the sum of 5 numbers entered by user

def sum():
    total = 0

    for i in range(5):
        num = float(input("Enter a number:"))
        total+=num
    
    print(total)


sum()