li=[]

for i in range(3):
    li.append(int(input()))

num=str(li[0]*li[1]*li[2])
one_to_nine=0

for i in '0123456789':
    print(num.count(i))

