"""
Write sumnum(num1, num2) that returns the sum of numbers from num1 to num2 (both 
inclusive). Call this function as shown below and print the result.
"""

def sumnum(num1, num2):
    # option 1: (n / 2)(first number + last number) = sum -> (101/2)(50 + 100)
    # option 2: for loop
    total = 0
    for num in range(num1,num2+1):
        total+=num
    return total

def mainsum():
    a = 50
    b = 150
    print("Sum of numbers from %d to %d = %d" % (a, b, sumnum(a, b)))


mainsum()