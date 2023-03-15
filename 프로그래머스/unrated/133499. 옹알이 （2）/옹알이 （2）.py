def solution(babbling):
    answer = 0
    baby = ["aya", "ye", "woo", "ma"]
    rep = []
    for i in babbling:
        for j in baby:
            if j in i :
                if j*2 not in i :
                    i = i.replace(j,"*")
                    rep.append(i)
    
    for i in rep:
        i = set(i)
        if len(i)==1 and '*' in i:
            answer+=1
    return answer