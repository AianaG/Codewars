def task(w,n,c):
    work_dict = {'Monday': 'James', 'Tuesday': 'John',
                'Wednesday': 'Robert', 'Thursday': 'Michael',
                'Friday': 'William'}
    return 'It is {0} today, {1}, you have to work, you must spray {2} trees and you need {3} dollars to buy liquid'.format(w, work_dict[w], n, n*c)
    # your code