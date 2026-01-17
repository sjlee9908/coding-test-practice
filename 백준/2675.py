n=int(input())
li=[]

for i in range(n):
    num, s=input().split()
    num=int(num)
    li.append([num, s])

for i in li:
    for j in i[1]:
        print(j*i[0], end='')
    print()