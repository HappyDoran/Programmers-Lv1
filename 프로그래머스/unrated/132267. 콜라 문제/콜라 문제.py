def solution(a, b, n):
    answer = 0
    x = int(n/a)*b + int(n%a)
    answer += int(n/a)*b
    #n은 빈병
    #a는 빈병 수
    #b는 빈병 주고 가져오는 콜라 수
    
    while x >= a :
        print(x)
        p = int(x/a)*b
        x = p + int(x%a)
        answer+= p
    
    print(x)
    x = int(x/a)*b + int(x%a)
    answer+= int(x/a)*b
    
#     x = int(n/a)*b + int(n%a)   #현재 있는 콜라수
#     print(x)
#     x = int(x/a)*b + int(x%a)
#     print(x)
#     x = int(x/a)*b + int(x%a)
#     print(x)
#     x = int(x/a)*b + int(x%a)
#     print(x)
#     x = int(x/a)*b + int(x%a)
#     print(x)
    
    
        
    return answer