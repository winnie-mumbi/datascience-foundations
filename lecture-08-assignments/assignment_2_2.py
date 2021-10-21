# A program that gets 23% profit of total revenue of a company
def profit():
    revenue = float(input("Enter total revenue:"))

    profit = (23/100) * revenue

    print("The profit earned from",revenue,"is",profit)
profit()