"""kk"""
# Write a python program to find the square root of the given number 
# using Bi-section method
def main():
	"""kk"""
inp_ = int(input())
Step_ = 0.01
Guesses_ = 0
Low_ = 0.0
High_ = inp_
Ans_ = (High_ + Low_)/2
while abs(Ans_**2 - inp_) >= Step_:
        Guesses_ += 1
    if Ans_**2 < inp_:
        Low_ = Ans_
    else:
    	High_ = Ans_
    Ans_ = (High_ + Low_)/2
print(str(inp_))
if __name__== "__main__":
	main()
