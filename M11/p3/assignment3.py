"""kk"""
def is_valid_word(word_, hand_, word_list):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    for ite_ in word_:
        if ite_ not in hand_.keys(): 
            return False
    return bool(word_ in word_list)
def main():
    """kk"""
    word = input()
    num_ = int(input())
    adict = {}
    for i in range(num_):
        data = input()
        le_ = data.split()
        adict[le_[0]] = int(le_[1])
        i = i + 1
    l2_ = input().split()
    print(is_valid_word(word,adict,l2_)) 
if __name__ == "__main__":
    main()
