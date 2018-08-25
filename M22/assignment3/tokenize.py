'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def tokenize(string):
    """kk"""
    dictionary = {}
    list1 = string.split(' ')
    # print(list1)
    length = len(list1)
    for i in range(length):
        # print(word)
        if list1[i]  not in dictionary:
            dictionary[list1[i]] = list1.count(list1[i])
        else:
            dictionary[list1[i]][i].append(list1.count(list1[i]))           
        print(dictionary)
    return dictionary
def main():
    """kk"""
    inp = int(input())
    string = ''
    for i in range(inp):
        i += 1
        string += input()
        # string += '\n'
    # print(string)
    print(tokenize(string))
if __name__ == '__main__':
    main()
