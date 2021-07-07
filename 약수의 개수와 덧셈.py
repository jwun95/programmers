def check_num(number):
    check_list = []
    for i in range(1,number+1):
        if number % i == 0:
            check_list.append(i)
            
    return check_list


def solution(left, right):
    answer = 0

    for i in range(left,right+1):
        check_number = check_num(i)
        if len(check_number) % 2 == 0:
            answer += i

        else:
            answer -= i

    return answer



print(solution(24,27))