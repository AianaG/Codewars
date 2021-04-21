def valid_spacing(s):
    print(s)
    count_space = list(s).count(' ')
    count_words = len([a for a in s.split(' ') if a != ''])
    if s == '':
        return True
    elif count_space > count_words-1:
        return False
    else:
        return True