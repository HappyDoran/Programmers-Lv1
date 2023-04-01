def solution(x):
    s = 0
    a = x
    answer = 0
    while a != 0 :
        s = s + a % 10
        a = a//10
    print(s)
    
    if x % s == 0 :
        answer = True
    else:
        answer = False
        
    return answer