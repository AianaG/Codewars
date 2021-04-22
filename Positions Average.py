def pos_average(s):
    # your code
    s_y = s.split(', ')
#     print(s_y)
    common_points = 0
    for i in range(len(s_y)):
        common_points += sum([check_common_positions(s_y[i],s_y[j]) for j in range(i+1, len(s_y))])
    
    len_strings = (len(s_y)*(len(s_y)-1)*len(s_y[0]))/2
#     print(len_strings)
    return common_points*100/len_strings

def check_common_positions(s1,s2):
#     print(s1, s2)
    common_positions = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            common_positions +=1
#     print(common_positions)
    return common_positions