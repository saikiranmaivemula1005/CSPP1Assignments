'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
lSt_ = []
def clean_string(string):
    """kk"""
    for i1_ in string:
        if i1_ not in '!@#$%^&*() .':
            lSt_.append(i1_)
    return ''.join(lSt_)


def main():
    """kk"""
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
