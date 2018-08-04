'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    inp_ = input()
    i = 0
    for i in len(inp_):
        char_ = inp_[i]
        if char_ in('!' or '@' or '#' or '$' or '%' or '^' or '&' or '*'):
            print('')
    print(inp_)
if __name__ == "__main__":
    main()
