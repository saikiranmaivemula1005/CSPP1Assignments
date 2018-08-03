"""kk"""# Write a python program to find the square root of the given number
# using approximation method
# testcase 1
# input: 25
# output: 4.999999999999998
# testcase 2
# input: 49
# output: 6.999999999999991
def main():
    """kk"""
INP_ = int(input())
EPSILON_ = 0.01
GUESS_ = 0.0
INC_ = 0.1
NOG_ = 0
while abs(GUESS_**2 - INP_) >= EPSILON_:
    GUESS_ += INC_
    NOG_ += 1
if abs(GUESS_**2 - INP_) >= EPSILON_:
    print('Failed on cube root of', INP_)
else:
    print(GUESS_)
if __name__ == "__main__":
    main()
