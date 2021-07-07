def solution(a, b):
    day_list = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    answer = ''
    num = 0
    
    if a > 1:
        for i in range(1,a):
            if i == 1:
                num += 31
                
            elif i == 2:
                num += 29
                
            elif i == 3:
                num += 31
                
            elif i == 4:
                num += 30
                
            elif i == 5:
                num += 31
                
            elif i == 6:
                num += 30
                
            elif i == 7:
                num += 31
                
            elif i == 8:
                num += 31
                
            elif i == 9:
                num += 30
                
            elif i == 10:
                num += 31
                
            elif i == 11:
                num += 30
            
    
    num += b
    num = num % 7 -1
    
    answer = day_list[num]
    
    
    return answer

print(solution(1,2))