'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
"""string"""
def main():
    """special"""
    input_ = input()
    s1_ = ""
    for i_ in input_:
        if i_ in '!' '@' '#' '$' '%' '^' '&' '*':
            s1_ = s1_ + " "
        else:
            s1_ = s1_ + i_
    print(s1_)
if __name__ == "__main__":
    main()
