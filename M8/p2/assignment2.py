"""kk"""
# Exercise: Assignment-2
# This function takes in one number and returns one number.
def sum_of_digits(num_):
    """kk"""
    if num_ == 0:
        return 0
    return num_%10+sum_of_digits(num_//10)
def main():
    """kk"""
    inp_ = input()
    print(sum_of_digits(int(inp_)))
if __name__ == "__main__":
    main()
