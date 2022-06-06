import numpy as np
import random
import codeproject

f3 = open('codetext.txt', encoding='utf-8', mode= 'r')
f4 = open('outcome.txt', encoding='utf-8', mode= 'w')
sbox_re = codeproject.sbox.copy()

for a in range(16) :
    for b in range(16) :
        subs = codeproject.sbox[a][b]
        subs = subs.split('.')
        sbox_re[int(subs[0]), int(subs[1])] = str(a) + "." + str(b)

ctext = list(f3.read())
ctext_len = len(ctext)
ctext_bit = ""
for i in range(ctext_len) :  
    bit = format(ord(ctext[i]), 'b').zfill(8)
    ctext_bit = ctext_bit + bit
ctext_bit_len = len(ctext_bit)

wow = ""
for i in range(int(ctext_bit_len / 128)-1,-1,-1) :
    last = ""
    if i == int(ctext_bit_len / 128) :
        yeah = codeproject.addround
    else :
        yeah = format(int(codeproject.keylist[(i*2)+1], 2) ^ int(codeproject.roundkey[i], 2), 'b').zfill(128)
    


    subarray = np.empty((0,16))
    changesubarray = np.empty((0,16), dtype= object)
    sboxarray = np.empty((0,16), dtype = object)

    for a in range(16) :
        subarray = np.append(subarray, yeah[a*8:(a+1)*8])

    subarray = subarray.reshape(4,4)
    

    for r in range(4) :
        
        croissant = np.empty((0,16))
        subarray = subarray.flatten()
        for x in range(8) :
            croi = ""
            croi = str(subarray[x*2]) + str(subarray[x*2+1])
            baba = croi[1] + croi[5] + croi[6] + croi[2] + croi[9] + croi[13] + croi[14] + croi[10] + croi[8] + croi[12] + croi[15] + croi[11] + croi[0] + croi[4] + croi[7] + croi[3]
            croissant = np.append(croissant, str(baba[:8]))
            croissant = np.append(croissant, str(baba[8:]))
        croissant = croissant.reshape(4,4)
        
        
        mixrows = croissant.flatten()
        mixrows = np.flip(mixrows)
        for g in range(0,16,8) :
            mixrows[g:g+8] = mixrows[g:g+8][::-1]
        mixrows = mixrows.reshape(4,4)
        

        windmillarray = mixrows.flatten()
        windmillarray = np.array([mixrows[1,0], mixrows[2,0], mixrows[1,2], mixrows[0,2], mixrows[1,1], mixrows[0,0], mixrows[0,3], mixrows[0,1], mixrows[3,2], mixrows[3,0], mixrows[3,3], mixrows[2,2], mixrows[3,1], mixrows[2,1], mixrows[1,3], mixrows[2,3]])
        windmillarray = windmillarray.reshape(4,4)
        
        
        subarray = windmillarray.flatten()
        for e in range(0,16,4) :
            subarray[e:e+4] = subarray[e:e+4][::-1]
        for f in range(0,16,2) :
            subarray[f:f+2] = subarray[f:f+2][::-1]
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
            sboxarray = np.append(sboxarray,sbox_re[int(sub[0]),int(sub[1])])
    sboxarray = sboxarray.reshape(4,4)
   
    sboxarray = sboxarray.flatten()
    for w in range(16) :
        didi = str(sboxarray[w]).split('.')
        didi = format(int(didi[0]), 'b').zfill(4) + format(int(didi[1]), 'b').zfill(4)
        last = last + didi
    
    last = format(int(codeproject.keylist[(i*2)], 2) ^ int(last, 2), 'b').zfill(128)
    wow = last + wow

for l in range((int(len(wow) / 16))) :
    fin = wow[int(l*16):int((l+1)*16)]
    fin = int(fin, 2)
    fin = chr(fin)
    f4.write(fin)


f3.close()
f4.close()