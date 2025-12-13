import sys

N = int(sys.stdin.readline())

length_table = [3, ]
k, length = 0, 3

while length < N:
    k += 1
    length = 2 * length_table[k-1] + (k + 1 + 2)
    length_table.append(length)

# print(k, length_table)
while k != 0:
    if N <= length_table[k-1]:
        N = N
        k -= 1
    elif N <= k+ 1 + 2 + length_table[k-1]:
        if N == length_table[k-1]+1: print('m')
        else: print('o')
        exit(0)
    else:
        N -= (k+ 1 + 2 + length_table[k-1])
        k -= 1

if N == 1: print('m')
elif N == 2: print('o')
elif N == 3: print('o')
     
