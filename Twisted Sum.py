def compute_sum(n):
    # recursive sum_of_digits
    sum_digits = 0
    for i in range(1, n+1):
        if i <= 9:
            sum_digits += i
        else:
            sum_digits += sum([int(a) for a in list(str(i))])
            
    return sum_digits