"""kkk"""
def main():
	"""kk"""
	str_ = input()
	check_ = 0
	mi_ = 0
	co_ = 0
	# the input string is in s
	# remove pass and start your code here
	while i < 1:
		if str_[i] < str_[i+1]:
			check_ = check_+1
		else:
			check_ = 0
		if check_ > co_:
			co_ = check_
			mi_ = i
		else:
			i = i+1
	print(substring(str_, mi_+1-co_, co_+1))
if __name__== "__main__":
	main()
