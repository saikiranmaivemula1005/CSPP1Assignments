#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
	S = input()
	# the input string is in s
	# remove pass and start your code here
	c=0
	for letter in range (str(S)): 
	     if letter == 'a' or 'i' or 'e' or 'o' or 'u':
	         C += 1
	print(C)  
                       

if __name__== "__main__":
	main()
