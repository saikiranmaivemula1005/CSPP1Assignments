'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    dictionary = {}
    list1 = string.split(' ')
    # print(list1)
    for word in list1:
        # print(word)
        if word not in dictionary:
            dictionary[word] = word
        else:
            dictionary[word] = list1.count(word)
    return dictionary
    
            
def main():
    inp = int(input())
    string = ''
    for i in range(inp):
        i += 1
        string += input()
        string += '\n'
    # print(string)
    tokenize(string)

if __name__ == '__main__':
    main()
