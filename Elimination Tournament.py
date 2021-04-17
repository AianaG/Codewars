def tourney(inp):
    # your code here
    appended_str = [inp]
    while len(inp)>1:
        new_str = []
        if len(inp)%2 == 0:
            print(inp)
            for i in range(0, len(inp)//2):
                new_str.append(max(inp[i*2], inp[2*i+1]))
            inp = new_str
            appended_str.append(inp)
        else:
            new_str.append(inp[-1])
            for i in range(0, len(inp)//2):
                new_str.append(max(inp[i*2], inp[2*i+1]))
            inp = new_str
            appended_str.append(inp)
    return appended_str