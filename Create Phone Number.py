def create_phone_number(n):
#     phone_str = ''.join([str(a) for a in n[0:3]])
    phone_str = '(' + ''.join([str(a) for a in n[0:3]]) + ') ' + ''.join([str(a) for a in n[3:6]]) + '-' + ''.join([str(a) for a in n[6:10]])
    return phone_str