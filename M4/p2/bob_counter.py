'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
	# the input string is in s
	# remove pass and start your code here
	s_1 = input("enter a string")
	s_2 = input("enter a sub string")
	print(s_1.count(s_2))
if __name__== "__main__":
	main()
