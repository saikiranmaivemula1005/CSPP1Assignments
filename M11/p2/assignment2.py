"""kkk"""
def updateHand(hand, word):
    """kkk"""
    for i in word:
        if i in hand.keys():
            hand[i] -= 1
    return hand
def main():
    """kk"""
	n = input()
	adict={}
	for i in range(int(n)):
		data=input()
		l=data.split()
		adict[l[0]]=int(l[1])
	data1=input()
	print(updateHand(adict, data1))
if __name__ == "__main__":
	main()