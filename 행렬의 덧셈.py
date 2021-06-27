def solution(arr1, arr2):
    answer = []
    count = 0

    
    for i in range(0, len(arr1)):
        line = []
        for k in range(0, len(arr1[0])):
            line.append(arr1[i][k]+arr2[i][k])
        
        answer.append(line)

    return answer
    

arr1 = [[1,2],[2,3]]
arr2 = 	[[3,4],[5,6]]
print(solution(arr1,arr2))