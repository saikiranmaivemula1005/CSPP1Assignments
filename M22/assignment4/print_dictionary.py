'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''
l1 = []
l2 = []
def print_dictionary(dictionary):
	for i in dictionary.keys():
		l1.append(i)
		l2.append(dictionary[i])
	# print(sorted(l1))
	l3 = sorted(l1)
	# print(l 2)
	for i in range(len(l1)):
		print(str(l3[i])+' '+'-'+ ' '+ str(l2[i]))



    

def main():
    dictionary = eval(input())
    # print(dictionary)
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
