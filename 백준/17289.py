n = int(input())
a = list(map(int, input().split()))

res = [-1] * n
b = []
ex_i = 0

for i in range(0, len(a)):
    if(b == []):
        b.append(a[i])
    else:
        if(b[len(b)-1] > a[i]):
            b.append(a[i])
        else:
            ex_i = i-1
            while(ex_i >= 0 and b != [] and b[len(b)-1] < a[i]):
                if(res[ex_i] != -1):
                    ex_i -= 1
                    continue
                res[ex_i] = a[i]
                b.pop(len(b)-1)
                ex_i -= 1
            b.append(a[i])

print(" ".join(list(map(str, res))))
