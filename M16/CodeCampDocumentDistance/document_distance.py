'''
    Document Distance - A detailed description is given in the PDF
'''
import math 
import re
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
    regex_ = re.compile('^a-z')
    doc_1 = [regex_.sub('', w) for w in doc_1]
    doc_2 = [regex_.sub('', w) for w in doc_2]
    stopwords = load_stopwords("stopwords.txt")
    for i in doc_1:
        if i in stopwords:
            doc_1.remove(i)
    # print(doc_1)
    for i in doc_2:
        if i in stopwords:
            doc_2.remove(i)
    # print(doc_2)
    # fre1 = []
    # fre2 = []
    # for i in doc_1:
    #     fre1.append(doc_1.count(i))
    # # print(fre1)
    # for i in doc_2:
    #     fre2.append(doc_2.count(i))
    # # print(fre2)
    fr_list = doc_1+doc_2
    # print(len(fr_list))
    # print(fr_list)
    fr_dic = {}
    for i in fr_list:
        if i not in fr_dic and len(i)>0:
            fr_dic[i] = [doc_1.count(i), doc_2.count(i)]
    # print(sorted(fr_dic.keys()))
    # print(len(fr_dic))
    num_ = 0
    for i in fr_dic:
        num_ = num_ + fr_dic[i][0]*fr_dic[i][1]
    # print(num_)
    # den_ = 0
    # sum1_ = 0
    # sum2_ = 0
    # sqr1_ = 0
    # sqr2_ = 0
    # for i in fr_dic:
    #     sum1_ = sum1_ + fr_dic[i][0]**2
    #     sum2_ = sum2_ + fr_dic[i][1]**2
    # sqr1_ = math.sqrt(sum1_)
    # sqr2_ = math.sqrt(sum2_)
    # den_ = sqr1_*sqr2_
    # # print(den_)
    # if(den_==0.0):
    #     return 0.0
    # res_ = num_ / den_
    # # print(res_)
    # return (res_)
    num = sum([v[0] * v[1] for v in fr_dic.values()])
    den1 = math.sqrt(sum([v[0] **2 for v in fr_dic.values()]))
    den2 = math.sqrt(sum([v[1] **2 for v in fr_dic.values()]))

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
