'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    """kk"""
    list1 = []
    dictionary = {}
    for i in string:
        lis2 = i.split(' ')
        for j in lis2:
            list1.append(j)
        # print(list1)
    lis = []
    for i in list1:
        lis.append(re.sub('[^a-zA-Z0-9]', '', i))
    for i in lis:
        if i not in dictionary:
            dictionary[i] = lis.count(i)
    return dictionary
def main():
    """kk"""
    inp = int(input())
    string = []
    for i in range(inp):
        i += 1
        string.append(input())
        # string += '\n'
    # print(string)
    print(tokenize(string))
if __name__ == '__main__':
    main()
