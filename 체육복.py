#def check_clothe(have, num):


def solution(n, lost, reserve):
    answer = 0

    for i in lost:
        check = 0
        check_lower = 0
        check_upper = 0
        if i == 1:
            check = i + 1

            if check in reserve:
                answer += 1

        elif i == n:
            check = n - 1

            if check in reserve:
                answer += 1

        else:
            check_lower = i - 1
            check_upper = i + 1

            if check_lower or check_upper in reserve:
                answer += 1

    answer += len(reserve)

        
    return answer





n = 5
lost = [2,4]
reserve = [1,3,5]

print(solution(n,lost,reserve))