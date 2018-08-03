# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    cube = int(input())
    epsilon = 0.0001
    guess = 0.0
    increment = 0.000001
    num_guesses = 0
    while abs(guess**2 - cube) >= epsilon:
        guess += increment
        num_guesses += 1
    if abs(guess**2 - cube) >= epsilon:
        print('Failed on cube root of', cube)
    else:
        print(guess)

if __name__== "__main__":
	main()
