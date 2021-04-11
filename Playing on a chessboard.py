def game(n):
    sum_board = n * n
    if sum_board % 2 == 0:
        return [sum_board / 2]
    else:
        return [sum_board, 2]