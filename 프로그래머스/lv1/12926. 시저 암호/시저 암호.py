def control(a, n):
    if a > n :
        return chr(a-26)
    else :
        return chr(a)
    
def solution(s, n):
    answer = ''
    for i in s :
        if i == " " :
            answer += i
        else :
            a = ord(i) + n
            if i >= "a" and i <= "z":
                answer += control(a, 122)
                
            elif i >= "A" and i <= "Z":
                answer += control(a, 90)
                
    return answer