def revrot(strng, sz):
    return_str = ''
    if sz <=0 or len(strng) <sz or strng == "": 
        return ""
    else:
        for i in range(0,len(strng), sz):
            subset = strng[i: i+sz]
            print(subset)
            if len(subset) == sz:
                cubes_ofnum = sum([int(j)**3 for j in subset])
                print(cubes_ofnum)
                if cubes_ofnum%2 == 0:
                    subset = [subset[-k-1] for k in range(len(subset))]
                else:
                    subset = [subset[i+1] for i in range(len(subset)-1)] + [subset[0]]
                print(subset)
                return_str += ''.join(subset)
        return return_str