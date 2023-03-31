def solution(name, yearning, photo):
    answer = []
    dic = {}
    score = 0
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
        
    for i in range(len(photo)):
        score = 0
        for j in range(len(photo[i])):
            if photo[i][j] in dic.keys():
                score+= dic[photo[i][j]]
            else:
                continue;
        answer.append(score)
    return answer