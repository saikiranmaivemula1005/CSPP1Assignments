"""kkk"""
def calculate_handlen(hand_):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    sum_ = 0
    for i in hand_:
    	sum_ = sum_ + hand_[i]
    return sum_ 
    

def main():
	"""kk"""
	num_ = input()
	adict = {}
	for i in range(int(num_)):
		data = input()
		le_ = data.split()
		adict[le_[0]] = int(le_[1])
	print(calculate_handlen(adict))	
if __name__ == "__main__":
	main()
