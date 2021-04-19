def meeting(s):
    lst_names = [a.split(':') for a in s.upper().split(';')]
#     print(lst_names)
    lst_names = sorted(lst_names, key = lambda x: (x[1], x[0]))
    return_str = ''
    for a in lst_names:
        return_str += '(' + a[1] +', ' + a[0] + ')'
    return return_str
    # your code