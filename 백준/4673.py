def selfnum(num):
    num_str=str(num)
    res=num
    for i in num_str:
        res+=int(i)
    return res

li=list(range(1,10000))

for i in range(1,10001):
    i=selfnum(i)
    if i in li:
        li.remove(i)

for i in li:
    print(i)
