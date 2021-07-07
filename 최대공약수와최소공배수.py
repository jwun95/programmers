def gcd_solution(n, m):

    gcd = m % n

    if gcd == 0:
        return n

    return gcd_solution(gcd, n)


def solution(n, m):
    answer = []

    gcd_solution(n, m)
    gcd = gcd_solution(n, m)

    lcm = (n * m) / gcd

    answer.append(int(gcd))
    answer.append(int(lcm))


    return answer

print(solution(64,72))