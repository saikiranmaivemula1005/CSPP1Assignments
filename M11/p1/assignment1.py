'''
Exercise: Assignment-1
The first step is to implement some code that allows us to calculate the score for a single word. The function get_word_score should accept as input a string of lowercase letters (a word) and return the integer score for that word, using the game's scoring rules.
'''

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    import string
    key_ = list(string.ascii_lowercase)
    val_ = 0
    l1 = []
    sum = 0
    for i in range (0, 25):
        l1.append(val_)
        val_ += 1
        #print(val_)
    di1 = dict(zip(key_, l1))
    length = len(word)
    if n < length:
        for i in word:
            sum = sum + di1[i]
    #print(sum) 
    #print(di1)
        sum = sum * length
        if length <= n:
            sum += 50
        return sum
    else:
        return'invalid'
    # TO DO ... <-- Remove this comment when you code this function
    


def main():
    '''
    Main function for the given problem
    '''
    data = input()
    data = data.split()
    print(get_word_score(data[0], int(data[1])))


if __name__ == "__main__":
    main()
