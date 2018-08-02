'''Assume s is a string of lower case characters.
Number of times bob occurs is: 2'''
def main():
    """geee"""
    s_1 = input()
    s_2 = 'bob'
    co_ = 0
    for i in range(len(s_1)-2):
        if s_2 == s_1[i]+s_1[i+1]+s_1[i+2]:
            co_ = co_+1
    print(co_)
if __name__ == "__main__":
    main()
