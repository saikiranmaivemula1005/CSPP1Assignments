'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    """kk"""
    input_ = input()
    s1_ = ""
    for i1_ in input_:
        if i1_ in '!' '@' '#' '$' '%' '^' '&' '*':
            s1_ = s1_ + " "
        else:
            s1_ = s1_ + i1_
    print(s1_)
if __name__ == "__main__":
    main()
