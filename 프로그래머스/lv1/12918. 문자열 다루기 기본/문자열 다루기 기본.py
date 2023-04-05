def solution(s):
    answer = True
    cnt = 0
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                cnt+=1
        if cnt == len(s) :
            return True
        else :
            return False
    else :
        return False
    return answer