"""kk"""
# Write a python program to find if the given number is a perfect cube or not 
# using guess and check algorithm

def main():
	"""kk"""
x = int(input('Enter an integer: ')) 
ans = 0 
while ans**3 < abs(x):
    ans = ans + 1 
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube') 
else: 
    if x < 0: 
        ans = - ans
    print(str(x) + ' is ' + 'a perfect cube')
  
if __name__== "__main__":
    main()
