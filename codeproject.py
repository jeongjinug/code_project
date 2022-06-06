import numpy as np
import random

f1 = open('plaintext.txt', encoding='utf-8', mode= 'r')
f2 = open('codetext.txt', encoding='utf-8', mode= 'w')

keyset = ""
for a in range(128) :
    a = random.randrange(2)
    keyset = keyset + str(a)


sbox = ['3.0', '9.9', '15.10', '7.4', '5.9', '4.1', '5.13', '5.12', '12.6', '0.1', '6.9', '10.0', '14.0', '3.11', '4.2', '13.6', '4.9', '13.7', '15.1', '3.10', '2.1', '8.1', '14.4', '13.15', '12.3', '15.7', '2.10', '4.14', '9.4', '4.0', '5.5', '8.2', '8.8', '13.8', '14.5', '1.14', '14.3', '14.13', '3.7', '11.12', '12.13', '14.6', '13.13', '2.11', '15.5', '12.2', '6.5', '12.15', '10.3', '7.5', '15.4', '15.3', '5.6', '2.13', '0.9', '8.3', '9.11', '0.2', '10.7', '7.6', '4.5', '9.8', '6.15', '6.10', '15.14', '1.13', '2.9', '15.11', '8.10', '4.12', '0.15', '9.13', '8.14', '11.0', '3.5', '11.13', '1.3', '6.8', '9.5', '1.6', '6.3', '14.1', '3.3', '14.11', '12.7', '0.8', '8.6', '14.8', '0.6', '11.1', '1.4', '7.1', '3.4', '5.0', '2.5', '1.8', '1.1', '3.14', '9.14', '3.6', '15.2', '8.0', '10.13', '8.4', '7.0', '13.4', '15.9', '2.0', '13.0', '5.2', '9.2', '15.12', '6.13', '4.13', '10.4', '7.8', '2.8', '6.2', '12.4', '7.7', '1.0', '7.14', '7.12', '5.7', '6.7', '7.11', '11.11', '11.3', '4.8', '4.7', '9.7', '11.9', '9.12', '2.4', '3.8', '7.13', '6.4', '8.11', '1.12', '11.2', '9.6', '1.7', '0.14', '1.11', '14.15', '5.8', '4.10', '1.10', '11.15', '15.13', '11.10', '6.1', '8.12', '3.15', '7.15', '9.0', '2.14', '11.4', '4.15', '5.15', '14.10', '0.12', '8.13', '8.15', '5.1', '12.10', '0.10', '10.6', '6.6', '12.5', '9.10', '10.14', '11.14', '13.11', '8.7', '12.11', '10.5', '4.4', '7.3', '5.14', '15.8', '8.9', '12.0', '13.3', '4.6', '10.8', '13.10', '4.11', '13.9', '11.7', '2.6', '7.10', '1.9', '9.1', '3.13', '7.2', '14.7', '13.5', '5.3', '13.1', '14.9', '11.8', '13.2', '9.3', '0.11', '15.0', '10.15', '1.5', '3.2', '13.12', '15.15', '2.12', '3.9', '12.12', '0.7', '5.10', '0.4', '14.12', '14.14', '10.1', '14.2', '10.9', '7.9', '13.14', '8.5', '2.7', '2.2', '9.15', '4.3', '12.9', '1.2', '12.14', '6.0', '0.0', '6.11', '12.1', '10.11', '3.1', '0.13', '10.10', '11.5', '11.6', '6.12', '3.12', '12.8', '2.3', '15.6', '0.3', '6.14', '5.11', '0.5', '5.4', '10.2', '10.12', '1.15', '2.15']
sbox = np.array(sbox).reshape(16,16)

ptext = list(f1.read())
ptext_len = len(ptext)

# 텍스트 파일 한글자씩 비트로 만들기
ptext_bit = ""
for i in range(ptext_len) :  
    bit = format(ord(ptext[i]), 'b').zfill(16)
    ptext_bit = ptext_bit + bit    
# 텍스트 파일 패딩
if len(ptext_bit) % 128 >=1 :
    paddingbit = (int(len(ptext_bit) / 128) + 1) * 128
    ptext_bit = ptext_bit.ljust(paddingbit, "0")
ptext_bit_len = len(ptext_bit)

print(ptext_bit)
print(ptext_bit_len)

keylist = []
for i in range(int(ptext_bit_len / 128)*2) :
    if i == 0 :
        sboxkeyset = ""
        for a in range(16) :
            keykey = keyset[a*8:(a+1)*8]
            leftkey = int(keykey[:4], 2)
            rightkey = int(keykey[4:], 2)
            keykey = sbox[leftkey, rightkey]
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
            keykey = sbox[leftkey, rightkey]
            keykey = keykey.split('.')
            keykey = format(int(keykey[0]), 'b').zfill(4) + format(int(keykey[1]), 'b').zfill(4)
            sboxkeyset = sboxkeyset + keykey

        keylist.append(sboxkeyset)

roundkey = []
last = ""
for s in range(int(ptext_bit_len / 128)) :
    
    ptext_bit_ch = ptext_bit[s*128:(s+1)*128]
    
    addround = format(int(keylist[s*2], 2) ^ int(ptext_bit_ch, 2), 'b').zfill(128)
    

    subarray = np.empty((0,16))
    changesubarray = np.empty((0,16), dtype= object)
    sboxarray = np.empty((0,16))

    for a in range(16) :
        subarray = np.append(subarray, addround[a*8:(a+1)*8])
    subarray = subarray.reshape(4,4)
    

    # p-박스 전 윗 비트열을 숫자.숫자로 만들기
    for a in range(4) :
        for b in range(4) :
            leftbit = int(subarray[a,b][:4], 2)
            rightbit = int(subarray[a,b][4:], 2)
            changebit = str(leftbit) + "." + str(rightbit)
            changesubarray = np.append(changesubarray, changebit)
    changesubarray = changesubarray.reshape(4,4)
    

    # 해당 숫자.숫자를 sbox 치환
    for c in range(4) :
        for d in range(4) :
            sub = changesubarray[c][d].split('.')
            sboxarray = np.append(sboxarray,sbox[int(sub[0]),int(sub[1])])
    sboxarray = sboxarray.reshape(4,4)
    print(sboxarray)
    


    for r in range(4) :
        if r >= 1 :
           
            subarray = np.empty((0,16))
            changesubarray = np.empty((0,16), dtype= object)
            sboxarray = np.empty((0,16))
            for a in range(16) :
                subarray = np.append(subarray, yeah[a*8:(a+1)*8])
            subarray = subarray.reshape(4,4)
            

     

            # p-박스 전 윗 비트열을 숫자.숫자로 만들기
            for a in range(4) :
                for b in range(4) :
                    leftbit = int(subarray[a,b][:4], 2)
                    rightbit = int(subarray[a,b][4:], 2)
                    changebit = str(leftbit) + "." + str(rightbit)
                    changesubarray = np.append(changesubarray, changebit)
            sboxarray = changesubarray.reshape(4,4)
            

       

        # mixcolumns
        subarray = sboxarray.flatten()
        for e in range(0,16,4) :
            subarray[e:e+4] = subarray[e:e+4][::-1]
        for f in range(0,16,2) :
            subarray[f:f+2] = subarray[f:f+2][::-1]
        subarray = subarray.reshape(4,4)
        print(subarray)
      


        # windmill bits
        windmillarray = subarray.flatten()
        windmillarray = np.array([subarray[1,1], subarray[1,3], subarray[0,3], subarray[1,2], subarray[0,0], subarray[1,0], subarray[0,2], subarray[3,2], subarray[0,1], subarray[3,1], subarray[2,3], subarray[3,3], subarray[2,1], subarray[3,0], subarray[2,0], subarray[2,2]])
        windmillarray = windmillarray.reshape(4,4)
        print(windmillarray)
  

        # mixrows
        mixrows = windmillarray.flatten()
        mixrows = np.flip(mixrows)
        for g in range(0,16,8) :
            mixrows[g:g+8] = mixrows[g:g+8][::-1]
        mixrows = mixrows.reshape(4,4)
        print(mixrows)
    
        
        # croissant bits
        croissant = np.empty((0,8))
        yeah = ""
        gogo = ""
        for x in range(0,4) :
            for y in range(0,4) :
                dada = mixrows[x,y].split('.')
                bubu = format(int(dada[0]), 'b').zfill(4) + format(int(dada[1]), 'b').zfill(4)
                gogo = gogo + bubu
        for o in range(0,128,16) :
            croissant = np.append(croissant, gogo[o:o+16])
        for p in range(8) :
            pepe = croissant[p]
            mumu = pepe[12] + pepe[0] + pepe[3] + pepe[15] + pepe[13] + pepe[1] + pepe[2] + pepe[14] + pepe[8] + pepe[4] + pepe[7] + pepe[11] + pepe[9] + pepe[5] + pepe[6] + pepe[10]
            yeah = yeah + mumu
        print(yeah)
        
        
    
    
    #print(keylist[s*2+1])
    addround = format(int(keylist[(s*2)+1], 2) ^ int(yeah, 2), 'b').zfill(128)
    
    roundkey.append(addround)
    hou = ""
    for tt in range(16) :
        wow = format(int(addround[tt*8:(tt+1)*8]), 'd').zfill(8)
        wow = chr(int(wow, 2))
        hou = hou + wow
    f2.write(hou)

f1.close()
f2.close()