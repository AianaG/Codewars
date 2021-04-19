def make_a_window(num): 
    window_row = '|' + num*'.' + '|' + num*'.' + '|' 
    window_break = '|' + num*'-' + '+' + num*'-' + '|' 
    window_list = '\n'.join([window_row for i in range(num)])
    final_window = (2*num +3)*'-' +'\n' + window_list + '\n' + window_break + '\n' + window_list + '\n' + (2*num +3)*'-'
    return final_window