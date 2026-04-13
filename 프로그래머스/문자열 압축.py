def zipit(s, n):
    ex_sub_count = 1
    ex_sub_s = ""
    ziped_string = ""

    for sub_s_start_idx in range(0, len(s), n):
        sub_s = s[sub_s_start_idx: sub_s_start_idx + n]


        if ex_sub_s == sub_s : 
            ex_sub_count += 1
        else:
            if ex_sub_s != "":
                if ex_sub_count != 1:
                    ziped_string += (str(ex_sub_count) + ex_sub_s)
                else:
                    ziped_string += (ex_sub_s)
            ex_sub_count = 1
            ex_sub_s = sub_s
                


    if ex_sub_count != 1:
        ziped_string += (str(ex_sub_count) + ex_sub_s)
    else:
        ziped_string += (ex_sub_s)

    return len(ziped_string)



def solution(s):
    res = len(s)
    for n in range(1, len(s)//2 + 1):
        res = min(res, zipit(s, n))
    return res


print(solution("ababcdcdababcdcd"))