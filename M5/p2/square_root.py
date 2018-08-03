"""kk"""
# Write a python program to find the square root of the given number
# using approximation method
def main():
    """kk"""
NEG_ = False
ANS_ = 0
X = int(input())
if X < 0:
    NEG_ = True
while ANS_**2 < X:
    ANS_ = ANS_ + 1
if ANS_**2 == X:
    print("Square root of", X, "is", ANS_)
else:
    print(X, "is not a perfect square")
    if NEG_:
        print("Enter a positive number")
if __name__ == "__main__":
    main()
