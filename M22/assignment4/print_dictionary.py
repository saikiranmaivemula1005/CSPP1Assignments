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
        LIST1.append([i1_,dictionary[i1_]])
    l3_ = sorted(LIST1)
    for i in l3_:
        print(i)
        for j in i:
            print(j)
def main():
    """kk"""
    dictionary = eval(input())
    # print(dictionary)
    print_dictionary(dictionary)
if __name__ == '__main__':
    main()
