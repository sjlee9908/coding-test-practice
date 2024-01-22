N=int(input())
num=0

for i in range(N):
    word = input()
    error=0
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            new_word=word[j+1:]
            if new_word.count(word[j])>0:
                error+=1
            
    if error==0:
        num+=1

print(num)