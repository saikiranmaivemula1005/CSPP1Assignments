'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
# helper function to load the stop words from a file
import re
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords
def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    text = str(text)
    regex = re.compile('[^a-z]')
    word_list = [regex.sub("", w.strip()) for w in text.lower().split(" ")]
    # print(word_list)
    return word_list
def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''
    # initialize a search index (an empty dictionary)
    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop
    # clean up doc and tokenize to words list
    # add or update the words of the doc to the search index
    # return search index
    search_index = {} 
    k =0
    stopwords = load_stopwords('stopwords.txt')
    l1 = word_list(docs)
    for i in docs:
        doc_id = docs.index(i)
        for j in l1:
            print(j)
            if j not in stopwords:
                if j not in search_index.keys():
                    search_index[k] = [(i, l1.count(i))]
                else:
                    search_index[k].append((i, l1.count(i)))    
    return search_index
# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])
# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        # print(i)
        documents.append(input())
        # print(documents)
        i += 1
    # call print to display the search index
    word_list(documents)
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
