def convertFracts(lst):
    print(lst)
    # find lcm of denominator
    if len(lst) <=1:
        return lst
    else:
        
        denominators = [a[1] for a in lst]
        lcm_val = denominators[0]
        for i in range(1,len(denominators)):
            lcm_val = lcm(denominators[i], lcm_val)
#         print(lcm_val)
    
    final_lst = []
    for i in lst:
        fact = int(lcm_val/i[1])
#         print(int(i[0]*fact), int(i[0]), fact)
        final_lst.append([int(i[0]*fact), int(lcm_val)])
        
    return final_lst
    

def lcm(a, b):
    
    return (a*b)/hcf(a,b)
    
    
def hcf(a, b):
#     print(a, b)
    if a == 0:
        return b
    else:
        return hcf(b%a, a)