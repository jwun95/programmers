def solution(strings, n):
    base_list = []
    answer = []
    
    #strings.sort()
    
    for item in strings:
        base_list.append(item[n])
    
    #print(base_list)
    base_list.sort()

    for i in range(0,len(base_list)):
        for k in range(0,len(strings)):
            if base_list[i] == strings[k][n]:

                answer.append(strings[k])

    
    return answer      

k = ["sun", "bed", "car"]
s = ["abce", "abcd", "cdx"]
print(solution(s, 2))
print(solution(k, 1))