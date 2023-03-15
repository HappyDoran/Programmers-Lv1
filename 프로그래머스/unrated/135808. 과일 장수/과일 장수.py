def solution(k, m, score):
    answer = 0

    score.sort()
    score.reverse()
    # print(score)
    
    for i in range(m-1,len(score),m):
        answer += score[i]*m
    
    # if i < len(score)-1:
    #     answer+= score[len(score)-1]*m
            
    
    return answer