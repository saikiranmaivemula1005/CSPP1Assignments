"""kk"""
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and returns the factorial of given number.

# This function takes in one number and returns one number.


def factorial(num_):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    
    if num_ in (0, 1):
        return 1
    return num_ * factorial(num_-1)
    


def main():
    """kk"""
    inp_ = input()
    print(factorial(int(inp_)))    
if __name__== "__main__":
    main()
