def han(num):
    num_str=str(num)
    num_cd=int(num_str[0])-int(num_str[1])
    for i in range(1, len(num_str)-1):
        if num_cd != int(num_str[i])-int(num_str[i+1]):
            return False
    return True
        
    
N=int(input())
if N<10:
    Cou=N
else:
    Cou=9
for i in range(10,N+1):
    if han(i):
        Cou+=1

print(Cou)

