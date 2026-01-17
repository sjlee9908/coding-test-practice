a, b=map(int, input().split())
li=[]

while a!=0 and b!=0:
    li.append([a, b])
    a, b=map(int, input().split())

for i in li:
    print(sum(i))