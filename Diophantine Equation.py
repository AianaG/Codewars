def sol_equa(n):
    # your code
    suitable_Fact = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            j = n // i
            if (i + j) % 2 == 0 and (j - i) % 4 == 0:
                x = (i + j) // 2
                y = (j - i) // 4
                suitable_Fact.append([x, y])
    return suitable_Fact 