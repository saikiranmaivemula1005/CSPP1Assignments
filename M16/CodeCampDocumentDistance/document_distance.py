'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    doc_1 = str(dict1)
    doc_2 = str(dict2)
    doc_1.strip()
    doc_2.strip()
    doc_1 = doc_1.lower().split(' ')
    doc_2 = doc_2.lower().split(' ')
    stopwords = load_stopwords("stopwords.txt")
    for i in doc_1:
        if i in stopwords:
            doc_1.remove(i)
    # print(doc_1)
    for i in doc_2:
        if i in stopwords:
            doc_2.remove(i)
    # print(doc_2)
    fre1 = []
    fre2 = []
    for i in doc_1:
        fre1.append(doc_1.count(i))
    # print(fre1)
    for i in doc_2:
        fre2.append(doc_2.count(i))
    # print(fre2)
    fr_list = fre1+fre2
    print(fr_list)
    fr1_ = {}
    fr2_ = {}
    for i in doc_1:
        if i not in fr1_:
            fr1_[i] = doc_1.count(i) 
    # print(fr1_)
    for i in doc_2:
        if i not in fr2_:
            fr2_[i] = doc_2.count(i)
    # print(fr2_)
    num_ = 0
    for i in fr1_.keys():
        if i in fr2_.keys():
            num_ = sum(fr1_[i] * fr2_[i])
    print(num_)





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
