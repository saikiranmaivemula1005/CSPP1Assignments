'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''
LIST1 = []
LIST2 = []
def frequency_graph(dictionary):
    """kk"""
    dic = {'1':'#', '2':'##', '3':'###', '4':'####', '5':'#####', '6':'######', '7':'#######', '8':'########', '9':'#########', '11':'###########'}
    for i1_ in dictionary.keys():
        LIST1.append([i1_, dictionary[i1_]])
    l3_ = sorted(LIST1)
    for i in l3_:
        # print(i)
        for j in range(1):
            print(str(i[0]) + ' '+ '-'+' '+dic[str(i[1])])
            j += 1
def main():
    """kk"""
    dictionary = eval(input())
    frequency_graph(dictionary)
if __name__ == '__main__':
    main()
