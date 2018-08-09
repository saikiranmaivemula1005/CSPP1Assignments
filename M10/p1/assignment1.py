"""kk"""
def get_available_letters(letters_guessed):
    """kk"""
    import string
    res__ = ''
    key_ = list(string.ascii_lowercase)
    val_ = key_
    dic_ = dict(zip(key_, val_))
    for i1_ in letters_guessed:
        if i1_ in dic_.values():
            del dic_[i1_]
    for j1_ in dic_.values():
        res_ = res_ + j1_
    return res_
def main():
    """kk"""
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))
if __name__ == "__main__":
    main()
