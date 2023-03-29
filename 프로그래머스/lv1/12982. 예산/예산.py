def solution(d, budget):
    answer = 0
    s = 0
    d.sort()
    for i in d:
        s+=i
        answer+=1
        if s > budget:
            answer-=1
            break
            
    return answer