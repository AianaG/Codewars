import re
class Calculator(object):
    def evaluate(self, string):
        print(string)
        while isinstance(string, str):
            string = step(string)
        return string
    
    
def step(to_eval):
    to_eval = to_eval.split(' ')
    if '(' in to_eval:
        inner_open_bracket = max([i for i in range(len(to_eval)) if to_eval[i] == '('])
        to_eval1 = to_eval[inner_open_bracket:]
        inner_close_bracket = min([i for i in range(len(to_eval1)) if to_eval1[i] == ')'])
        ops_str = to_eval[inner_open_bracket+1:inner_open_bracket+inner_close_bracket]
        ops_str = [a for a in ops_str if a != '' and  a!= ' ']
        final_num = float(add(subtract(multiply(divide(ops_str))))[0])
        to_eval[inner_open_bracket] = final_num
        del to_eval[inner_open_bracket+1:inner_open_bracket+inner_close_bracket +1]
        return ' '.join([str(a) for a in to_eval])
    else:
        ops_str = to_eval
        ops_str = [a for a in ops_str if a != '' and  a!= ' ']
#         print(ops_str)
        final_num = float(add(subtract(multiply(divide(ops_str))))[0])
#         print(final_num)
        return final_num
    
def divide(ops_list):
    if '/' in ops_list:
        while '/' in ops_list:
            divide_sym = min([i for i in range(len(ops_list)) if ops_list[i] == '/'])
            ops_list[divide_sym-1] = float(ops_list[divide_sym-1])/float(ops_list[divide_sym+1])
            ops_list.pop(divide_sym)
            ops_list.pop(divide_sym)
    return ops_list

def multiply(ops_list):
    if '*' in ops_list:
        while '*' in ops_list:
            divide_sym = min([i for i in range(len(ops_list)) if ops_list[i] == '*'])
            ops_list[divide_sym-1] = float(ops_list[divide_sym-1])*float(ops_list[divide_sym+1])
            ops_list.pop(divide_sym)
            ops_list.pop(divide_sym)
    return ops_list

def add(ops_list):
    if '+' in ops_list:
        while '+' in ops_list:
            divide_sym = min([i for i in range(len(ops_list)) if ops_list[i] == '+'])
            ops_list[divide_sym-1] = float(ops_list[divide_sym-1])+float(ops_list[divide_sym+1])
            ops_list.pop(divide_sym)
            ops_list.pop(divide_sym)
    return ops_list

def subtract(ops_list):
    if '-' in ops_list:
        while '-' in ops_list:
            divide_sym = min([i for i in range(len(ops_list)) if ops_list[i] == '-'])
            ops_list[divide_sym-1] = float(ops_list[divide_sym-1])-float(ops_list[divide_sym+1])
            ops_list.pop(divide_sym)
            ops_list.pop(divide_sym)
    return ops_list