'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    """product"""
    input_ = int(input())
    num_ = abs(input_)
    pro_ = 1
    rem_ = 0
    if num_ == 0:
        print(num_)
    else:
        while num_ >= 1:
            rem_ = num_ % 10
            pro_ = pro_ * rem_
            num_ = num_ // 10
        if input_ < 0:
            pro_ = -pro_
        print(pro_)
if __name__ == "__main__":
    main()
