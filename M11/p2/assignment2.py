"""kkk"""
def update_hand(hand_, word_):
    """kkk"""
    i = 0
    for ite_ in word_:
        if ite_ in hand_.keys():
            hand_[ite_] -= 1
    i = i + 1
    return hand_
def main():
    """kk"""
    num_ = input()
    adict = {}
    i = 0
    for i in range(int(num_)):
        data = input()
        le_ = data.split()
        adict[le_[0]] = int(le_[1])
    i = i + 1
    data1 = input()
    print(update_hand(adict, data1))
if __name__ == "__main__":
    main()
