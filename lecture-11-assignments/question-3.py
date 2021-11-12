"""
Generalize the above function further and write sumnum(num1, num2, k) , such that it returns the 
sum of given k th power of numbers from num1 to num2. For instance, if k=1 sum of numbers, if 
k=2 sum of squares of numbers, if k=0.5 sum of square roots of numbers, etc. 
"""

def sumnum(num1, num2, k):
    total = 0
    for num in range(num1,num2+1):
        total+=num**k
    return total

def mainsum():
    a = 50
    b = 150
    k = 2
    print("Sum of %d power of numbers from %d to %d = %d" % (k, a, b, sumnum(a, b, k)))


mainsum()