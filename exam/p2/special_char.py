'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
"""string"""
def main():
    """special"""
    input_ = input()
    s1 = ""
    for i in input_:
        if i in '!' '@' '#' '$' '%' '^' '&' '*':
            s1 = s1 + " "
        else:
            s1 = s1+ i
    print(s1)
if __name__ == "__main__":
    main()
