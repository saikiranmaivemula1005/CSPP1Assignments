'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''

    # remove the pass below and start writing your code
    x1_ = data.split('\n')

    # print(x1_)
    dic_ = {}
    # data = data.split(' follows ')
    # print(data)
    for ite_ in range(len(x1_)-1):
        ite_ = x1_[ite_].split(' follows ')
        # print(ite_)
        if len(ite_) <= 1:
            return dic_
        print(ite_[0],ite_[1])
        if ite_[0] not in dic_:
            dic_[ite_[0]] = ite_[1].split(',')
            # print(ite_[0], dic_[ite_[0]])
        else:
            dic_[ite_[0]].append(ite_[1].split(','))
    return dic_
def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'

    print(create_social_network(string))

if __name__ == "__main__":
    main()
