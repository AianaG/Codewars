def path_finder(maze):
    path_list = [list(a) for a in maze.split('\n')]
    if len(path_list) ==  1:
        return True
    else:
        n = len(path_list)
        start_positions = [[n-1, n-1]]
        val = recursive_check(path_list, start_positions)
        return val

def recursive_check(path_list, start_positions):
    all_possible_positions = []
    for start_position in start_positions:
        previous_allpos = [[start_position[0]-1, start_position[1]],
                                [start_position[0], start_position[1]-1],
                                [start_position[0]+1, start_position[1]],
                                [start_position[0], start_position[1]+1]]
        n = len(path_list)
        previous_allpos = [a for a in previous_allpos if 0 <= a[0] <= n-1 and 0<=a[1]<=n-1
                              and path_list[a[0]][a[1]] != 'W']
        all_possible_positions.extend(previous_allpos)
        path_list[start_position[0]][start_position[1]] = 'W'
        
    all_possible_positions = [list(x) for x in set(tuple(x) for x in all_possible_positions)]
#     print(all_possible_positions)
    if len(all_possible_positions) == 0:
        return False
    elif [0,0] in all_possible_positions:
        print("yes")
        return True
    
    else:
        return recursive_check(path_list, all_possible_positions)