def solution(arr):
    answer = []
    count = 0
    i = 0

    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i-1])

    answer.append(arr[-1])

    
    return answer

l = [1,1,3,3,0]
print(solution(l))