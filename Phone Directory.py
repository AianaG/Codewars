import re
def phone(strng, num):
    # your code
    phonebooklist = strng.split('\n')
    number = [(i, re.search(num, j).group()) for i, j in enumerate(phonebooklist) if re.search(num, j)]
    print(number)
    if len(number) >1:
        return 'Error => Too many people: ' + str(num)
    elif len(number) == 0:
        return 'Error => Not found: ' + str(num)
    else:
        phoneaddress = phonebooklist[number[0][0]]
        phoneaddress = re.sub(num, '', phoneaddress)
        name = re.search(r'<[a-zA-Z. \']*>', phoneaddress).group()
        address = re.sub(name, '', phoneaddress)
        name = re.sub('>', '', re.sub('<', '', name))
        address = re.sub('_', ' ', re.sub('  ', ' ',re.sub('[\+$;/!?,:*@]', '', address))).strip()
        to_Return_str = 'Phone => ' + str(num) + ', Name => ' + str(name) + ', Address => ' + str(address)
        
        return to_Return_str