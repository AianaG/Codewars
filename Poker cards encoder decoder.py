def encode(cards):
    encoded = []
    encoding_dict = {'A': 1, 'T': 10, 'J':11, 'Q': 12, 'K':13 }
    type_dict = {'c': 0, 'd': 1, 'h': 2, 's': 3}
    for i in cards:
        if i[0] in encoding_dict:
            val = encoding_dict[i[0]]
        else:
            val = int(i[0])
        final_val = type_dict[i[1]]*13+(val-1)
        encoded.append(final_val)
    return sorted(encoded)

def decode(cards):
    type_dict  = {0: 'c', 1: 'd', 2: 'h', 3: 's'}
    decoding_dict = {1: 'A', 10: 'T', 11:'J', 12: 'Q', 13: 'K' }
    decoded = []
    for i in sorted(cards):
        decoded_str = ''
        if ((i)%13 + 1) in decoding_dict:
            decoded_str = decoding_dict[((i)%13 + 1)]
        else:
            decoded_str = str((i)%13 + 1)
        decoded_str +=  type_dict[i//13]
        decoded.append(decoded_str)
    return decoded