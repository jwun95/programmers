def solution(n):
    sieve = [True] * (n + 1)

    if n > 7:
        m = int(n ** 0.5)

    else:
        m = n
    
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, len(sieve), i):
                sieve[j] = False




    # 소수 목록 산출
    answer = [i for i in range(2, n+1) if sieve[i] == True]

    return answer


print(solution(100))