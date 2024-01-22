hour, minute=map(int, input().split())

hour-=1
minute+=15

if minute>=60:
    hour=hour+(minute//60)
    minute%=60

if hour>=24:
    hour-=24
elif hour<0:
    hour=24+hour

print(hour, minute)
