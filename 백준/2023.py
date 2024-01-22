# input
import collections
import math

n = int(input())


# processing
def is_prime(n):
    for d in range(2, int(math.ceil(n / 2 + 1))):
        if n % d == 0:
            return False
    return True


prime_li = collections.deque([2,3,5,7])

for i in range(n-1):
    prime_li_len = len(prime_li)
    #print("len is : ", prime_li_len)
    for _ in range(prime_li_len):
        now_prime = prime_li.popleft()
        #print("now: ", now_prime)
        now_prime = now_prime * 10
        for v in range(1, 10):
            prime = now_prime + v
            #print(prime, end = " ")
            if is_prime(prime):
                prime_li.append(prime)
        #print()



# output
if n == 1:
    for i in [2, 3, 5, 7]:
        print(i)
else:
    for i in prime_li:
        print(i)

