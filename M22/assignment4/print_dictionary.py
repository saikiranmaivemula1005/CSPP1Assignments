'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''
l1 = []
def print_dictionary(dictionary):
	for i in dictionary.keys():
		l1.append(i)
	for i in dictionary.keys():
		for i in sorted(l1):
			print(i+' '+'-'+' '+dictionary[i])
		# print(dictionary[i])

    

def main():
    dictionary = eval(input())
    # print(dictionary)
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
