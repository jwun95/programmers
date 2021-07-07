def check_answer(student, answer):
    answer_length = len(answer)
    student_length = len(student)
    mok = int(answer_length / student_length)
    namegi = answer_length % student_length
    add_student = []

    if student_length < answer_length:
    
        for i in range(0, namegi):
            add_student.append(student[i])
        
        student = (student * mok) + add_student
        
    return_answer = 0
    
    for j, k in zip(student, answer):
        if j == k:
            return_answer += 1

    return return_answer


def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []
    
    one_count = check_answer(one, answers)
    two_count = check_answer(two, answers)
    three_count = check_answer(three, answers)

    my_dic = {1: one_count, 2: two_count, 3:three_count}
    max_number = max(my_dic.values())


    for item in my_dic.items():
        if item[1] == max_number:
            answer.append(item[0])
    
    answer.sort()

    return answer

print(solution([1,3,2,4,2]))
