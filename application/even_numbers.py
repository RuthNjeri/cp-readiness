#checks for even numbers

def number(num):

    #check if the number is an integer
    if type(num) != int:
        raise ValueError("Number must be an integer")

    #test if the number is positive
    # if num < 1:
    #     raise ValueError("Must enter a positive number")

    #test if the number is even
    if num % 2 == 0:
            return True
    
