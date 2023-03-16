def solution(lottos, win_nums):
    answer = []
    extos = lottos.copy()
    cnt = 0
    dict = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    
    for i in range(len(lottos)) :
        if lottos[i] in win_nums:
            extos.remove(lottos[i])
            cnt+=1
    
    print(extos)
    answer.append(dict[cnt])
    answer.append(dict[cnt + extos.count(0)])
    answer.sort()
    
    return answer