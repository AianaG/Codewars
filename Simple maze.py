def has_exit(maze):


    check_mutliple_kate = sum([a.count('k') for a in maze])
    if check_mutliple_kate != 1:
        raise Error
    
    kate_position = find_original_position(maze)
    reached_edge = check_if_on_edge(maze, kate_position[0], kate_position[1])

    possible_way_outs = way_outs(maze, kate_position)
    lengths = max([len(i) for i in maze])
    print(lengths)
    for i in range(len(maze)):
        if len(maze[i]) < lengths:
            print(maze[i])
            print((lengths - len(maze[i])))
            maze[i] = maze[i] + (lengths - len(maze[i]))*' '
    if reached_edge :
        return True
    elif possible_way_outs == 0:
        return False
    else:
        val = recursive_movement(maze, [kate_position])
        return val
        
def find_original_position(maze):
    for i in range(len(maze)):
        if 'k' in maze[i]:
            return [i, [j for j in range(len(maze[i])) if maze[i][j] =='k'][0]]

def check_if_on_edge(maze, i, j):
    if i ==0 or j ==0 or i == len(maze)-1 or j == len(maze[i])-1:
        return True
    else:
        return False

def way_outs(maze, current_position):
    way_outs = [[current_position[0]-1, current_position[1]],
                       [current_position[0]+1, current_position[1]],
                       [current_position[0], current_position[1] -1],
                       [current_position[0], current_position[1] +1]]
#     print(way_outs)
    possible_way_outs = [i for i in way_outs if i[0] >=0 and i[1] >=0 and i[0] < len(maze) and i[1] < len(maze[i[0]]) and maze[i[0]][i[1]] == ' '] 
#     print(possible_way_outs)
    return possible_way_outs
        


def recursive_movement(maze, start_positions):
    all_possible_positions = []
    for start_position in start_positions:
        previous_allpos = way_outs(maze, start_position)
        all_possible_positions.extend(previous_allpos)
        maze[start_position[0]] = list(maze[start_position[0]])
        maze[start_position[0]][start_position[1]] = '#'
        maze[start_position[0]] = ''.join(maze[start_position[0]])
        
    all_possible_positions = [list(x) for x in set(tuple(x) for x in all_possible_positions)]
    print(all_possible_positions)
    check_if_any_pos_reached_edge = [1 for i in all_possible_positions if check_if_on_edge(maze, i[0], i[1])]
    if len(all_possible_positions) == 0:
        print("here")
        print(all_possible_positions)
        return False
    elif sum(check_if_any_pos_reached_edge) >=1:
        print("yes")
        return True
    
    else:
        return recursive_movement(maze, all_possible_positions)