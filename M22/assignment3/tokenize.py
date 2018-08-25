'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
list1 = []
def tokenize(string):
    dictionary = {}
    for word in string:
        if word in dictionary:
            dictionary[word].append(list1.count(word))
        else:
            dictionary[word] = [list1.count(word)]
    return dictionary
    
            
def main():
    inp = int(input())
    string = input()
    print(tokenize(string))
    

if __name__ == '__main__':
    main()
