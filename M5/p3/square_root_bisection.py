"""kk"""
# Write a python program to find the square root of the given number
# using Bi-section method
X_ = int(input())
EPSILON_ = 0.01
NOG_ = 0
LOW_ = 0.0
HIGH_ = X_
ANS_ = (HIGH_ + LOW_)/2.0
while abs(ANS_**2 - X_) >= EPSILON_:
    NOG_ += 1
    if ANS_**2 < X_:
        LOW_ = ANS_
    else:
        HIGH_ = ANS_
    ANS_ = (HIGH_ + LOW_)/2.0
print(str(ANS_))
