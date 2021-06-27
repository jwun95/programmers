def solution(n):
    answer = 0
    k = []
    ntos = str(n)
    
    for i in range(0, len(ntos)):
        k.append(ntos[i])
        
    k = sorted(k,reverse=True)

    answer = "".join(k)
    
    
    return answer

print(solution(15678945))