st=input()
ti=0

for i in st:
    if i in 'ABC':
        ti+=3
    elif i in "DEF":
        ti+=4
    elif i in "GHI":
        ti+=5
    elif i in "JKL":
        ti+=6
    elif i in "MNO":
        ti+=7
    elif i in "PQRS":
        ti+=8
    elif i in "TUV":
        ti+=9
    elif i in "WXYZ":
        ti+=10

print(ti)