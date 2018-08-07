"""kk"""
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and returns the factorial of given number.

# This function takes in one number and returns one number.


def factorial(n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    return n_ * factorial(n_-1)
  	if n_ == 0:
        return 1
    
    


def main():
    a_ = input()
    print(factorial(int(a_)))    

if __name__== "__main__":
    main()
