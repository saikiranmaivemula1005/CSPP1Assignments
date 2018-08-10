# Assignment-3
'''
'''
def isValidWord(word_, hand_, word_list):
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
    word=input()
    n=int(input())
    adict={}
    for i in range(n):
        data=input()
        l=data.split()
        adict[l[0]]=int(l[1])
    l2=input().split()
    print(isValidWord(word,adict,l2)) 
if __name__ == "__main__":
    main()
    