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
    x = str(int(input()))
    product = 1
    i = 1
    while i < x:
        n = temp%10
        product = product*n
        n = n//10
    print(product)
if __name__ == "__main__":
    main()
