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
    inp_ = input()
    pro_ = 0
    temp_ = inp_
    while inp_ > 0:
        num_ = temp_%10
        print(num_)
        pro_ = pro_*num_
        num_ = inp_/10
    print(pro_)
    if __name__ == "__main__":
        main()
