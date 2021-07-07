def solution(n):
    answer_list = ""
    answer = ""

    while n > 0:
        nameji = 0
        mok = 0
        nameji = n % 3 
        mok = int(n / 3) 
        n = mok
        answer_list += str(nameji)
        if mok == 1:
            answer_list += str(mok)
            break

    answer = int(answer_list,3)

    return answer

print(solution(3))