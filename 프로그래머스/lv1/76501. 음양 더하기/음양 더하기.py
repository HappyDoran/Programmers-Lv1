def solution(absolutes, signs):
    answer = 0
    print(signs)
    for i in range(len(signs)):
        if signs[i] == True:
            answer+= absolutes[i]
        else :
            answer-= absolutes[i]
            
    return answer