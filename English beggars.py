def beggars(values, n):
    return [sum([values[a] for a in range(len(values)) if (a-i)%(n) == 0]) for i in range(n)]
