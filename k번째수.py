def solution(array, commands):
    answer = []
    
    for item in commands:
        k = array[item[0]-1:item[1]]
        k.sort()
        answer.append(k[item[2]-1])
        
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))