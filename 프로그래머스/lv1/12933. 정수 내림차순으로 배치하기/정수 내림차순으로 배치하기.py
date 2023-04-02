def solution(n):
    answer = []
    a = 0
    while n != 0 :
        answer.append(n % 10)
        n = n // 10
    answer.sort()
    
    for i in range(len(answer)) :
        a = a + answer[i]*10**i
    
    
    return a