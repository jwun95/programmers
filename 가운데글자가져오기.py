def solution(s):
    
    length = len(s)
    devide = int(length / 2)
    answer = ''
    
    if length % 2 == 0:
        answer += s[devide-1] + s[devide]
        
    else:
        answer += s[devide]
    
    return answer