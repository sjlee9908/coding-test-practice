num=int(input())
li=[]

for i in range(num):
    li_score=list(map(int, input().split()))
    li.append(li_score)

for i in li:
    avg=sum(i[1:])/i[0]
    over_avg=0
    for j in i[1:]:
        if j>avg:
            over_avg+=1
    print('{0:0>.3f}%'.format(over_avg/i[0]*100,3))
