def solution(num):
    answer = 0
    
    if num == 1:
            return answer
    
    while True:

        if answer == 500:
            answer = -1
            break
        
        if num % 2 == 0:
            num = num / 2
            
        else:
            num = (num * 3) + 1
    
        answer += 1
        
        if num == 1:
            break
    
    return answer