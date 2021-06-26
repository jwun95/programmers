def solution(s):
    
    tip = sorted(s, reverse = True)
    answer = "".join(tip)
    return answer