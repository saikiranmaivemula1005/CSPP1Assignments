'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
LIST = []
def clean_string(string):
    """kk"""
    for i1_ in string:
        if i1_ not in '!@#$%^&*() .':
            LIST.append(i1_)
    return ''.join(LIST)


def main():
    """kk"""
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
