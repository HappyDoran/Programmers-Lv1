def solution(n):
    answer = ""
    num = 0
    while n > 2 :
        answer+=str(n%3)
        n = int(n / 3)
    answer+=str(n)
    

    
    for i in range(len(answer)):
        print(answer[i])
        num = num + int(answer[i])*3**(len(answer) - i-1)
    
    return num