def move_zeros(arr):
    count_zeros = arr.count(0)
    arr = [i for i in arr if i!=0]
    for i in range(count_zeros):
        arr.append(0)
    return arr
