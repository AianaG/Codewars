def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string_ = ''.join([a for a in list(string_) if a.lower() not in vowels])
    return string_