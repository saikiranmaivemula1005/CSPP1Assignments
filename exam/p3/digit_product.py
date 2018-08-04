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
    for i in x:
    	n = i*i
    print(i)
if __name__ == "__main__":
    main()
