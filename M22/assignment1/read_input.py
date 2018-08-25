'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    documents = []
    lines = int(input())
    for i in range(lines):
        documents.append(input().split(','))
        i += 1
        print(documents)
        # print(''.join(documents),end='')
if __name__ == '__main__':
    main()
