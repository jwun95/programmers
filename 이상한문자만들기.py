def solution(s):
    
    answer = []

    stol = s.split(" ")


    for item in stol:
        ker = ""
        for i in range(0,len(item)):
            if i % 2 == 0:
                ker += item[i].upper()
            else:
                ker += item[i].lower()
        
        answer.append(ker)
    
    answer = " ".join(answer)
    
    return answer


k = "try hello world"
print(solution(k))