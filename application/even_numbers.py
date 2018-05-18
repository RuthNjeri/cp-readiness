#checks for even numbers

def number(num):
    if type(num) != int:
        raise ValueError("Number must be an integer")

    if num < 1:
        raise ValueError("Must enter a positive number")

    if num % 2 == 0:
            return True
    
