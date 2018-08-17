'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def kind(face_values, num):
    """kk"""
    for face in face_values:
        if face_values.count(face) == num:
            return face
def get_facevalues(hand):
    """k"""
    print(sorted(['--23456789TJQKA'.index(face) for face, suite in hand], reverse = True))
    return sorted(['--23456789TJQKA'.index(face) for face, suite in hand], reverse = True)
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    face_values = get_facevalues(hand)
    if face_values == [14, 5, 4, 3, 2]:
        face_values = [5, 4, 3, 2, 1]
    set_face_values = set(face_values)
    return (len(set_face_values) == 5) and ((max(set_face_values) - min(set_face_values)) == 4)
def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    set_ = set([suite for face, suite in hand])
    return len(set_) == 1
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush
    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    face_values = get_facevalues(hand)
    return ((8, face_values) if is_flush(hand) and is_straight(hand) else
            (7, kind(face_values, 4), face_values) if kind(face_values, 4) else
            (6, kind(face_values, 3), kind(face_values, 2))
            if  kind(face_values, 3) and kind(face_values, 2) else
            (5, face_values) if is_flush(hand) else
            (4, face_values) if is_straight(hand) else
            (3, kind(face_values, 3), face_values) if kind(face_values, 3) else
            (2, kind(face_values, 2), kind(sorted(face_values), 2), face_values)
            if kind(face_values, 2) and kind(sorted(face_values), 2) else
            (1, kind(face_values, 2), face_values) if kind(face_values, 2) else
            (0, face_values))
def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.
        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation
        Output: Return the winning poker hand
    '''
    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)
if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
