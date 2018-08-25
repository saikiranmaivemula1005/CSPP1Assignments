'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    dictionary = {}
    for word in string:
        list1.append(word) 
        if word in dictionary:
            dictionary[word].append(word, list1.count(word))
        else:
            dictionary[word] = [(word, list1.count(word))]
    return word
    
            
def main():
    inp = int(input())
    string = input()
    print(tokenize(string))
    

if __name__ == '__main__':
    main()
