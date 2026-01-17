li=[]
a=input()

while True:
    try:
        a=map(int, a.split())
        li.append(list(a))
        a=input()
    except EOFError:
        break


for i in li:
    print(sum(i))