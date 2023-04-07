def solution(N, stages):
    answer = []
    index = []
    bunmo = len(stages)
    for i in range(1,N+1):
        cnt = 0
        for j in range(len(stages)):
            if stages[j] == i :
                cnt+=1
        if cnt == 0 :
            answer.append(0)
        else :
            answer.append(cnt/bunmo)
            bunmo -=cnt
   
    real = sorted(answer,reverse = True)
    
    for i in real:
        if i in answer:
            index.append(answer.index(i)+1)
            answer[answer.index(i)] = 2
           
            
    
    return index