def solution(strings, n):
    base_list = {}
    base = []
    answer = []

    strings.sort()

    for item in strings:
        base_list[item] = item[n]

    base = sorted(base_list.items(), key = lambda x : x[1])

    for i in base:
        answer.append(i[0])

    return answer

k = ["sun", "bed", "car"]
s = ["abce", "abcd", "cdx"]
print(solution(s, 2))
print(solution(k, 1))