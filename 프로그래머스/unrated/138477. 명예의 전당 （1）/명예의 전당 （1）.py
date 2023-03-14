def solution(k, score):
    answer = []
    m = []
    for i in range(len(score)):
        answer.append(score[i])
        answer.sort()
        answer.reverse()
        if len(answer) < k:
            m.append(answer[len(answer) - 1])
        else :
            m.append(answer[k-1])
    
    print(m)
    return m