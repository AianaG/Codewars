def count_adjacent_pairs(st): 
    print(st)
    # your code here
    words = st.lower().split(' ')
    distinct_words = []
    curr_word = words[0]
    for i in range(1, len(words)):
        counter  = 0
        if words[i] == curr_word:
            counter += 1
            if len(distinct_words) == 0 and counter >=1:
                distinct_words.append(curr_word)
            elif distinct_words[-1] != words[i] and counter >=1:
                distinct_words.append(curr_word)
                
        else:
            curr_word = words[i]
    print(distinct_words)  
                
    
    return len(distinct_words)
    