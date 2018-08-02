#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5
def main():
	S_t = input()
	# the input string is in s
	# remove pass and start your code here
	C_o = 0
	for Lette_r in (S_t): 
	     if Lette_r == 'a' or 'i' or 'e' or 'o' or 'u':
	         C_o += 1
	print(C_o)  
                   
if __name__== "__main__":
	main()
