def rank_check(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    answer = []
    
    check_0 = 0
    check = 0
    
    for i in range(0,len(lottos)):
        if lottos[i] not in win_nums:
            if lottos[i] == 0:
                check_0 += 1 

        else:
            check += 1
            
    min_rank = rank_check(check)
    max_rank = rank_check(check + check_0)

    answer.append(max_rank)
    answer.append(min_rank)
            
    return answer