def solution(s):
    answer = []
    s = list(s)
    for i in range(len(s)):
        result = -1
        for j in range(0,i):
            if s[i] == s[j]:
                result = i - j
        answer.append(result)
    return answer