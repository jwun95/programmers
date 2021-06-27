def solution(n):
    answer = []
    
    ntos = str(n)
    
    for i in range(0,len(ntos)):
        answer.append(int(ntos[i]))

    answer = sorted(answer,reverse=True)
    
        
    return answer


print(solution(10545161648780))