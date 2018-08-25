'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    """kk"""
    dictionary = {}
    list1 = string.split(' ')
    # print(list1)
    lis = []
    for i in list1:
        lis.append(re.sub('[^a-zA-Z0-0]',"",i))
    # print(lis)
    # length = len(list1)
    # for i in range(length):
    #     # print(word)
    #     if list1[i] in dictionary:
    #         dictionary[list1[i]][1].append(list1.count(list1[i]))
    #     else:
    #         dictionary[list1[i]] = list1.count(list1[i])
    # # print(dictionary)
    dictionary = {}
    for i in lis:
        if i not in dictionary:
            dictionary[i] = lis.count(i)
    return dictionary
def main():
    """kk"""
    inp = int(input())
    string = ''
    for i in range(inp):
        i += 1
        string += input()
        string += " "
        # string += '\n'
    # print(string)
    print(tokenize(string))
if __name__ == '__main__':
    main()
