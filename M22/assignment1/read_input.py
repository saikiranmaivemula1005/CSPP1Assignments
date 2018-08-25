'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    """kk"""
    documents = []
    lines = int(input())
    for i in range(lines):
        documents.append(input())
        i += 1
    for i in documents:
        print(i)
if __name__ == '__main__':
    main()
