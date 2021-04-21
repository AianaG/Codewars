def get_positions(n):
    val = tuple([(n%3), (n//3)%3, (n//9)%3])
    return val