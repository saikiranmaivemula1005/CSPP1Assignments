"""kk"""
# Write a python program to find if the given number is a perfect cube or not 
# using guess and check algorithm
def main():
    """kk"""
X = int(input()) 
ANS_ = 0 
while ANS_**3 < abs(X):
    ANS_ = ANS_ + 1 
if ANS_**3 != abs(X):
    print(str(X)+' is not a perfect cube') 
else: 
    if X < 0: 
        ANS_ = - ANS_
    print(str(X) + ' is ' + 'a perfect cube') 
if __name__ == "__main__":
    main()
