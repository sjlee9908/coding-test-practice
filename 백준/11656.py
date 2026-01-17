s = input()

s_pre = [ s[x:-1]+s[-1] for x in range(0,len(s)*-1, -1) ]
s_pre.sort()

for i in s_pre:
    print(i)