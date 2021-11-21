"""
Write a function named sumnum that finds the sum of numbers from 1 to 100, and returns the 
result. Use the following print statement to print the result on screen.
"""

def sumnum():
    total = 100*(100 + 1) / 2
    return total

    
print(f"Sum of numbers from 1 to 100 = {sumnum()}")