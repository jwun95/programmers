def daemunja(item, n):
    
    if item + n > 90:
                
        count = item + n - 90
        gap = chr(count + 64)
        return gap

    else:
        return chr(item+n)

def somunja(item,n):

    
    if item + n > 122:
        
        count = item + n - 122
        gap = chr(count + 96)
        return gap

    else:
        return chr(item+n)

def solution(s, n):
    answer = ''
    
    for item in s:
        if item == " ":
            answer += " "
            
        elif ord(item) >= 65 and ord(item) <= 90:
            answer += daemunja(ord(item), n)

        
        else:
            answer += somunja(ord(item), n)
            
    
    return answer


print(solution("a B z",4))