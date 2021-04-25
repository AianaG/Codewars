def palindrome(num):
    if not isinstance(num, int) or num <0:
        return "Not valid"
    count_palindrome = 0
    subsets_palindrome = []
    num = str(num)
    for i in range(len(num)):
        count_palindrome += len([num[i:j] for j in range(i+1, len(num)+1) if check_palindrome(num[i:j]) and len(num[i:j])>1])
#         print(count_palindrome)
    return  count_palindrome
    # Code here

    
def check_palindrome(num):
    num = str(num)
    for i in range(len(num)//2):
        print(i)
        if num[i] != num[len(num)- i-1]:
            return False
    return True
        