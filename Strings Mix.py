import numpy as np
def mix(s1, s2):
    unique_words = [a for a in list(set((s1+s2))) if a.isalpha() and a.islower()]
#     dictionary_of_words = dict()
    
    return_str = []
    for a in unique_words:
        count_a_s1 = s1.count(a)
        count_a_s2 = s2.count(a)
        max_of_words = max(count_a_s1, count_a_s2)
        
        if max_of_words >1:
            if count_a_s1 == count_a_s2:
                return_str.append(['=', max_of_words*a])
            else:
                argmax_of_words = np.argmax([count_a_s1, count_a_s2]) +1
                return_str.append([argmax_of_words, max_of_words*a])
    return_str = [str(a[0]) + ':' +str(a[1]) for a in return_str]
    sort_return_str = [a for a in sorted(return_str, key=lambda x: (-len(x[1:]), x))]
#     print(sort_return_str)
    sort_return_str = ('/'.join(sort_return_str))
    return sort_return_str
    