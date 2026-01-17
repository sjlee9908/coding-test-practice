import sys

def alpha2digit(alpha:str):
    if alpha.isupper(): return ord(alpha) - 65
    else: return ord(alpha) - 97 + 26

def _digit2alpha(digit:int):
    if digit < 26: return chr(digit + 65) 
    else: return chr(digit + 97 - 26)

def print_grp():
    true_prop = []
    count = 0
    for f in range(52):
        for t in range(52):
            if grp[f][t] == True and f != t:
                count += 1
                true_prop.append(f"{_digit2alpha(f)} => {_digit2alpha(t)}")
    print(count)
    print(*true_prop, sep = '\n')


def fw():
    for k in range(52):
        for i in range(52):
            for j in range(52):
                if grp[i][j] == False:
                    grp[i][j] = (grp[i][k] and grp[k][j])


N = int(sys.stdin.readline())
grp = [[False] * 52 for _ in range(52)] 

for _ in range(N):
    prop = sys.stdin.readline().strip()
    f, t = alpha2digit(prop[0]), alpha2digit(prop[-1])
    grp[f][t] = True


fw()
print_grp()







