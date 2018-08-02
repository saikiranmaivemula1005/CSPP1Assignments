#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5
S = input()
C=0
for Letter in (S): 
     if Letter == 'a' or 'i' or 'e' or 'o' or 'u':
	         C += 1
	print(C)  