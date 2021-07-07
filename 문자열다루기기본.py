import re

def solution(s):
    answer = False
    
    k = re.findall("\d+", s)
    k = "".join(k)

    if k == s:
        answer = True
    
    return answer


kkk = "12a3"
print(solution(kkk))
