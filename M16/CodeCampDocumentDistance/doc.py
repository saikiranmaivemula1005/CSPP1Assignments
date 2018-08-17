'''
    Document Distance - A detailed description is given in the PDF
'''
import math 
import re
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    regex = re.compile('[^a-z]')
    words1 =[regex.sub("",w.strip()) for w in dict1.lower().split(" ")]
    words2 =[regex.sub("",w.strip()) for w in dict2.lower().split(" ")]
    dictionary = {}
    stopwords = load_stopwords("stopwords.txt")
    for w in words1:
        if w not in stopwords and len(w)>0:
            if w not in dictionary.keys():
                dictionary[w]=[0,0]
            dictionary[w][0]+=1
    for w in words2:
        if w not in stopwords and len(w)>0:
            if w not in dictionary.keys():
                dictionary[w]=[0,0]
            dictionary[w][1]+=1
    num = sum([v1*v2 for v1,v2 in dictionary.values()])
    den1 = math.sqrt((sum([v1**2 for v1,v2 in dictionary.values()])))
    den2 = math.sqrt((sum([v2**2 for v1,v2 in dictionary.values()])))
    return num/(den1*den2)
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
