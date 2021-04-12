import copy
def get_generation(cells, generations):
    print(cells, generations)
    
    for i in range(generations):
#         print("round",str(i))
        next_state = [[0 for a in range(len(cells[0])+2)] for b in range(len(cells)+2)]
        for j in range(len(cells)):
            for k in range(len(cells[j])):
                next_state[j+1][k+1] = cells[j][k]
        initial_state = copy.deepcopy(next_state)
#         print(next_state)
        for j in range(len(next_state)):
            for k in range(len(next_state[j])):
#                 print(j ,k)
                neighbours = [[j, k+1], [j, k-1], [j-1, k], 
                             [j-1, k+1], [j-1, k-1], [j+1, k],
                             [j+1, k+1], [j+1, k-1]]
#                 print(neighbours)
                possible_ne  = [initial_state[a[0]][a[1]] for a in neighbours if a[0]>=0 and a[0]<len(initial_state)
                               and a[1]>=0 and a[1]< len(initial_state[j])]
#                 print(possible_ne)
                sum_neighbour = sum(possible_ne)
#                 print(sum_neighbour)
                if initial_state[j][k] == 1 and (sum_neighbour >3 or sum_neighbour <2) :
                    next_state[j][k] =0
                elif initial_state[j][k] == 0 and (sum_neighbour ==3):
                    next_state[j][k] =1
        sum_first_row = sum(next_state[0])
        while sum_first_row == 0:
            next_state = next_state[1:]
            sum_first_row = sum(next_state[0])
        sum_last_row = sum(next_state[-1])
        while sum_last_row == 0:
            next_state = next_state[:-1]
            sum_last_row = sum(next_state[-1])
        sum_first_column = sum([a[0] for a in next_state])
        while sum_first_column == 0:
            next_state = [a[1:] for a in next_state]
            sum_first_column = sum([a[0] for a in next_state])
        sum_last_column = sum([a[-1] for a in next_state])
        while sum_last_column == 0:
            next_state = [a[:-1] for a in next_state]
            sum_last_column = sum([a[-1] for a in next_state])

        
        cells = next_state


#     print(cells)
    return cells