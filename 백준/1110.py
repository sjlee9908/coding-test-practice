first_number_str=input()
first_number=first_number_str

if len(first_number_str)==1:
    first_number_str=first_number_str+'0'
    first_number=first_number+'0'

cycle=0
last_num_str=''

while True:
    cycle+=1
    first_number_sum=sum(map(int, first_number_str))
    first_number_sum_str=str(first_number_sum)
    if len(first_number_sum_str)==1:
        first_number_sum_str='0'+first_number_sum_str
    last_num_str=first_number_str[1]+first_number_sum_str[1]
    if last_num_str==first_number:
        break
    else:
        first_number_str=last_num_str

print(cycle)


