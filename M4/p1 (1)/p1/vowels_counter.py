"""kkk"""
#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels
#contained in the string s. Valid vowels are:
# 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',
# your program should print:
#Number of vowels: 5
def main():
    """kk"""
    str_ = input()
    cou_ = 0
    for letter_ in str_:
        if letter_ in ('a', 'i', 'e', 'o', 'u'):
            cou_ += 1
    print(cou_)
if __name__ == "__main__":
    main()
