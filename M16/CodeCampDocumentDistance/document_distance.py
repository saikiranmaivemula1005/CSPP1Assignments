'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    doc_1 = str(dict1)
    doc_2 = str(dict2)
    doc_1 = doc_1.lower().split(' ')
    doc_2 = doc_2.lower().split(' ')
    doc_1.strip()
    doc_2.strip()
    stopwords = load_stopwords("stopwords.txt")
    for i in doc_1:
        if i in stopwords:
            doc_1.remove(i)
    print(doc_1)


def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
