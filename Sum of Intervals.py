def sum_of_intervals(intervals):
    all_num = []
    for i in intervals:
        all_num.extend([j for j in range(i[0], i[1])])
#     print(len(set(all_num)))
    return len(set(all_num))