# Exercise: Assignment-2
# This function takes in one number and returns one number.
def sum_of_digits(num_):
    """kk"""
    temp_ = num_
    while temp_ > 0:
    	temp_1 = temp_ % 10
    	return temp_1 + sum_of_digits(temp_ // 10)
    return 0   
def main():
    """kk"""
    inp_ = input()
    print(sum_of_digits(int(inp_)))  
if __name__ == "__main__":
    main()
