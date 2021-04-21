def decodeMorse(morse_code):
    morse_code_words = morse_code.strip().split('   ')
    word_list = []
    for i in morse_code_words:
        alphabets = i.split(' ')
#         print(alphabets)
        word = ''.join([MORSE_CODE[a] for a in alphabets if len(a) >0])
        word_list.append(word)
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    return ' '.join(word_list)