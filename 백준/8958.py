num=int(input())
li=[]

for i in range(num):
    li.append(input())

for i in li:
    score=0
    total_score=0
    for j in i:
        if j=='O':
            score+=1
            total_score+=score
        else:
            score=0
    print(total_score)