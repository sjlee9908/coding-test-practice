s=input()
s=s.lower()
li=[]

for i in 'abcdefghijklmnopqrstuvwxyz':
    li.append(s.count(i))

m=max(li)
a=0

for i in li:
    if i==m:
        a+=1

if a==1:
    print(chr(65+li.index(m)))

else:
    print('?')