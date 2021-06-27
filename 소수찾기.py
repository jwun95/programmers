def solution(n):
    answer = 0
    gogo = []
    
    if n == 2:
        return 1
       
    else:    
        for i in range(3,n+1):
            count = 0 
            for k in range(2,i):
                if i % k == 0:
                    count = 0
                    gogo.append(i)

    answer = len(set(gogo))
    
    return answer

print(solution(10))