def solution(s):
    answer = False
    p = 0
    y = 0
    
    
    for i in s:
        if i == 'p' or i == 'P':
            p += 1
            
        elif i == 'y' or i == 'Y':
            y += 1
            
    if p == y:
        answer = True
            
    
    return answer

kkk = "pPoooyY"
print(solution(kkk))