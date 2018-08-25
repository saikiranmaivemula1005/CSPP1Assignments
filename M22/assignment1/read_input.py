'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    documents = []
    lines = int(input())
    for i in range(lines):
        print(i)
        documents.append(input())
        i += 1
        print(documents)
if __name__ == '__main__':
    main()
