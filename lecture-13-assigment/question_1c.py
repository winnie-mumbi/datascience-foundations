"""
Modify both functions such that the end value is not 100, but it is entered by the user.
You can use either < or <= in the while condition.
Consider both cases, how would the boundary value change for both cases?

    - for loop - boundary value will be +1 so that its inclusive of the number entered
    - while loop - boundary value should <= number given / < 'number given + 1'
"""

# sum from 1 to value entered by user using a for loop
def sumnum_1():
    last_num = int(input("Enter a number greater than 1: "))

    if last_num <= 1:
        print("Please enter a number greater than 1")
        return
    
    total = 0

    for num in range(1,last_num+1):
        total += num
    
    print(f"Sum of 1 to {last_num} is {total} ")

# sum from 1 to value entered by user using a while loop
def sumnum_2():
    last_num = int(input("Enter a number greater than 1: "))

    if last_num <= 1:
        print("Please enter a number greater than 1")
        return

    total = 0
    num = 1

    while num <= last_num:
        total += num
        num += 1
    
    print(f"Sum of 1 to {last_num} is {total} ")


sumnum_1()
print()
sumnum_2()