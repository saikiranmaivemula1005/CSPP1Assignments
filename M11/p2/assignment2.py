"""kkk"""
def update_hand(hand_, word_):
    """kkk"""
    for ite_ in word_:
        if ite_ in hand_.keys():
            hand_[ite_] -= 1
    return hand_
def main():
    """kk"""
    n = input()
    adict={}
    for i in range(int(n)):
        data=input()
        l=data.split()
        adict[l[0]]=int(l[1])
    data1=input()
    print(update_hand(adict, data1))
if __name__ == "__main__":
	main()
