def sosu_check(num):
    check = 0
    for n in range(2,num):
        if num % n == 0:
            check = 1
    
    return check


def solution(nums):
    answer = 0

    length = len(nums)
    
    for i in range(0,length-2):
        for j in range(i+1,length-1):
            for k in range(j+1, length):
                hap = nums[i] + nums[j] + nums[k]
                check = sosu_check(hap)
                if check == 0:
                    answer += 1

    return answer

my_list = [1,2,7,6,4]
print(solution(my_list))