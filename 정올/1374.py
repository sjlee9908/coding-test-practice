from sys import stdin, exit

while True:
    a = int(stdin.readline())
    b = int(stdin.readline())
    if a == 0 and b == 0:
        break
        
    print(a + b)
    print(abs(a - b))

exit(0)