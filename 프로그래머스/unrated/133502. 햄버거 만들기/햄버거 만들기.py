def solution(ing):
    answer = 0
    s = []
    HAMBERGER = [1,2,3,1]
    for i in ing :
        s.append(i)
        if s[-4:] == HAMBERGER:
            answer+=1
            for i in range(4):
                s.pop()
            
    return answer