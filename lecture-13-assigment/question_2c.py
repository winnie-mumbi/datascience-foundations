"""
Add a counter to your program and find how many steps x reaches the value 0
"""

def division():
    x = 1.0
    num = x
    counter = 0

    while x != 0:
        x = x / 2
        counter += 1
    
    print(f"It takes {counter} steps to continually divide {num} by 2 till 0")

division()