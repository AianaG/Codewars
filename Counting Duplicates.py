def duplicate_count(text):
    # Your code goes here
    text = text.lower()
    count_word = {}
    duplicate_words = []
    for i in text:
        if i not in count_word:
            count_word[i] =1
        else:
            count_word[i] += 1
            if count_word[i] > 1 and i not in duplicate_words:
                duplicate_words.append(i)
    return len(duplicate_words)
     