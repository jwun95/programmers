def solution(seoul):
    
    check = 0
    for item in seoul:
        if item == "Kim":
            answer = '김서방은 {0}에 있다'.format(check)
            return answer
        
        else:
            check += 1