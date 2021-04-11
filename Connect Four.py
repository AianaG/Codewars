def who_is_winner(pieces_position_list):
    print(pieces_position_list)
    col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
               'G': 6}
    color_dict = {'Yellow': 0, 'Red': 1}
    counter = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    game_list = [ [None for _ in range(7)] for _ in range(6) ]
    for i in range(len(pieces_position_list)):
        
        column = col_dict[pieces_position_list[i].split('_')[0]]
        row = counter[column]
        game_list[row][column] = color_dict[pieces_position_list[i].split('_')[1]]
        counter[column] += 1
        yellow_win = winning_criteria(game_list, 0)
        red_win = winning_criteria(game_list, 1)
        if yellow_win == 0 and red_win >= 1:
            return 'Red'
        elif yellow_win >= 1 and red_win == 0:
            return 'Yellow'
    
    return 'Draw'

def winning_criteria(game_list, player):
    horizontal_check = sum([1 for i in game_list for j in range(0, 4) if len(set(i[j:j+4])) == 1 and i[j] == player])
    vertical_check = sum([1 for a in [[x[i] for x in game_list] for i in range(7)] for j in range(0,3) if len(set(a[j:j+4])) == 1 and a[j] == player])
    right_diagonal_check = 0
    left_diagonal_check = 0
    for i in range(3):
        for j in range(4):
            diagonal_group = [game_list[i][j], game_list[i+1][j+1], game_list[i+2][j+2], game_list[i+3][j+3]]
            if len(set(diagonal_group)) == 1 and diagonal_group[0] == player:
                right_diagonal_check += 1
        for j in range(6, 2, -1):
            diagonal_group = [game_list[i][j], game_list[i+1][j-1], game_list[i+2][j-2], game_list[i+3][j-3]]
            if len(set(diagonal_group)) == 1 and diagonal_group[0] == player:
                left_diagonal_check += 1 
    return horizontal_check + vertical_check + right_diagonal_check + left_diagonal_check