'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''
LIST1 = []
LIST2 = []
def print_dictionary(dictionary):
    """kk"""
    for i1_ in dictionary.keys():
        LIST1.append(i1_)
        LIST2.append(dictionary[i1_])
    # print(sorted(l1))
    l3_ = sorted(LIST1)
    # print(l 2)
    for i1_ in range(len(LIST1)):
        print(str(l3_[i1_])+' '+'-'+ ' '+ str(LIST2[i1_]))
def main():
    """kk"""
    dictionary = eval(input())
    # print(dictionary)
    print_dictionary(dictionary)
if __name__ == '__main__':
    main()
