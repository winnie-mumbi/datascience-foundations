"""
A user wants to purchase a list of items as much as the budget allows.
Let’s say the budget is 1000 KES.

Write a program that reads item prices from the user one by one;
prints the total upto that point after reading each price;
and prints a message and stops when the total exceeds 1000 KES. 

"""

def purchase():
    total = 0

    while True:
        price = int(input("Enter item price: "))

        total += price
        if total >= 1000:
            print(f"The total is {total}.You have reached your budget limit of 1000")
            break
        else:
            print(f"The total so far is {total}")

purchase()