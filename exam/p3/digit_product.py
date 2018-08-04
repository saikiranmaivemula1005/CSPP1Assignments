'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    inp_ = int(input())
    pro_ = 1
    temp_ = inp_
    while inp_ > 0:
        num_ = inp_%10
        pro_ = pro_*num_
        num_ = temp_//10
        print(pro_)
    if __name__ == "__main__":
        main()
