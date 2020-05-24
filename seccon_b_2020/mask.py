""" 
Reversing mask
$ ltrace ./mask
you can see ...
cmpr(input words & mask1, res1)
cmpr(input words & mask2, res2)

The flag of this CTF starts ctf4b{...}
So you can guess first 5 characters of input workds
and then, guess value of mask

this code specify input word using such infromation
"""


mask1 = 0b1110101
mask2 = 0b1101011

res1 = "atd4`qdedtUpetepqeUdaaeUeaqau"
res2 = "c`b bk`kj`KbababcaKbacaKiacki"

a = [0] * 6
ans = ""
for i in range(len(res2)):
    a[0] = ord(res1[i]) & mask1
    a[1] = ord(res2[i]) & mask2
    a[2] = a[0] ^ 0b1010
    a[3] = a[1] ^ 0b10100
    a[4] = a[1] ^ 0b10000
    a[5] = a[1] ^ 0b100

    tmp = ""
    for j in range(6) :
        tmp1 = a[j] & mask1
        tmp2 = a[j] & mask2
        
        if tmp1 != ord(res1[i]) :
            continue
        if tmp2 != ord(res2[i]) :
            continue
        tmp = (chr(a[j]))
    
    ans += tmp
    
print(ans)
    