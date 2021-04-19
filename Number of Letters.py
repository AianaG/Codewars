def switcher(arr):
    alphabets = ' ?!abcdefghijklmnopqrstuvwxyz'
    return ''.join([alphabets[29-int(a)] for a in arr])
    