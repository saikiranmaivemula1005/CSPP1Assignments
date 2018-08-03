"""kkk"""# Write a python program to find the square root of the number
# using Newton-Rapson method
def main():
    """kk"""
STEP_ = 0.01
Y_ = int(input())
GUESS_ = Y_/2.0
NOG_ = 0
while abs(GUESS_*GUESS_ - Y_) >= STEP_:
    NOG_ += 1
    GUESS_ = GUESS_ - (((GUESS_**2) - Y_)/(2*GUESS_))
print('numGuesses = ' + str(NOG_))
print('Square root of ' + str(Y_) + ' is about ' + str(GUESS_))
if __name__ == "__main__":
    main()
