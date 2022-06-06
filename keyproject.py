import random
import codeproject

keyset= "11110100100001011110111100110101111000111100110010101110001101001101001011110100100010101100011001001101011101101011011001001100"

keylist = []
for i in range(int(codeproject.ptext_bit_len / 128)*2) :
    if i == 0 :
        sboxkeyset = ""
        for a in range(16) :
            keykey = keyset[a*8:(a+1)*8]
            leftkey = int(keykey[:4], 2)
            rightkey = int(keykey[4:], 2)
            keykey = codeproject.sbox[leftkey, rightkey]
            keykey = keykey.split('.')
            keykey = format(int(keykey[0]), 'b').zfill(4) + format(int(keykey[1]), 'b').zfill(4)
            sboxkeyset = sboxkeyset + keykey
        keylist.append(sboxkeyset)
    else :
        keyset = format(int(keyset,2) ^ int((keyset[96:] + keyset[:96]), 2), 'b').zfill(128)
        sboxkeyset = ""
        for a in range(16) :
            keykey = keyset[a*8:(a+1)*8]
            leftkey = int(keykey[:4], 2)
            rightkey = int(keykey[4:], 2)
            keykey = codeproject.sbox[leftkey, rightkey]
            keykey = keykey.split('.')
            keykey = format(int(keykey[0]), 'b').zfill(4) + format(int(keykey[1]), 'b').zfill(4)
            sboxkeyset = sboxkeyset + keykey

        keylist.append(sboxkeyset)
print(len(keylist))