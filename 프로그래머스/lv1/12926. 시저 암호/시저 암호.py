def solution(s, n):
    answer = ''
    print(ord('z'))
    print(ord('a'))
    print(ord("A"))
    print(ord("Z"))
    for i in s :
        if i == " " :
            answer += i
        else :
            if i >= "a" and i <= "z":
                a = ord(i) + n
                if a > 122 :
                    answer += chr(a-26)
                else :
                    answer += chr(a)
            elif i >= "A" and i <= "Z":
                a = ord(i) + n
                if a > 90 :
                    answer += chr(a-26)
                else :
                    answer += chr(a)
                
    return answer