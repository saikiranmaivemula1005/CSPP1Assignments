'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    dictionary = {}
    list1 = string.split(' ')
    # print(list1)
    for i in range(len(list1)):
        # print(word)
        if list1[i] in dictionary:
            dictionary[list1[i][1]].append(list1.count(list1[i]))
        else:
            dictionary[list1[i]] = list1.count(list1[i])
    print(dictionary)
    return dictionary
    
            
def main():
    inp = int(input())
    string = ''
    for i in range(inp):
        i += 1
        string += input()
        # string += '\n'
    # print(string)
    tokenize(string)

if __name__ == '__main__':
    main()
