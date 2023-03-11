def solution(t, p):
    answer = 0
    a = []
    plen = len(p)
    for i in range(len(t) - plen + 1):
        a.append(t[0+i:0+i+plen])
    
    for i in a :
        num = int(i)
        if num <= int(p):
            answer+=1
    return answer