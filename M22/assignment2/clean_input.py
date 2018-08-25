'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
	"""kk"""
    for i in string:
    	if i not in '!@#$%^&*()':
    		l1.append(i)
    print(''.join(l1))


def main():
	"""kk"""
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
