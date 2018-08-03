# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
guess = 0.0
increment = 0.01
num_guesses = 0
while abs(guess**2 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**2 - cube) >= epsilon:
else:
    print(guess)
if __name__== "__main__":
	main()
