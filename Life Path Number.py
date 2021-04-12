def life_path_number(birthdate):
    li = birthdate.split('-')
    li_split = [recursive_sum(i) for i in li]
    return recursive_sum(sum(li_split))
    
    
def recursive_sum(number):
    number_list = [int(i) for i in list(str(number))]
    number_sum = sum(number_list)
    if number_sum <=9:
        return number_sum
    else:
        return recursive_sum(number_sum)