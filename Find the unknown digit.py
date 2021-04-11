def solve_runes(runes):
    # Your code here   
    start_with0 = [str(0)+str(i) for i in range(0, 10)]
    for i in range(0, 10):
        rune_check = runes.replace('?', str(i)).replace('=', '==')
        rune_list = rune_check.replace('==', ' ').replace('-', ' ').replace('+', ' ').replace('*', ' ').split(' ')
        rune_check_list = [1 for i in rune_list if i[0:2] not in start_with0]
        if str(i) not in runes and len(rune_list) == sum(rune_check_list):
            if eval(rune_check):
                return i
    return -1