def step(g, m, n):
    for x in range(m, n):
#         print(x)
        if isprime(x):
            if isprime(x+g) and x+g <n:  
                return [x, x+g]

        
def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        elif i*i > num:
            return True
    return True
