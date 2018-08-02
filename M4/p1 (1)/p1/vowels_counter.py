#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5
def main():
	S_t1 = input()
	# the input string is in s
	# remove pass and start your code here
	C_o1 = 0
	for Lette_r1 in (S_t1): 
	     if Lette_r1 == 'a' or 'i' or 'e' or 'o' or 'u':
	         C_o1 += 1
	print(C_o1)  
                   
if __name__== "__main__":
	main()
