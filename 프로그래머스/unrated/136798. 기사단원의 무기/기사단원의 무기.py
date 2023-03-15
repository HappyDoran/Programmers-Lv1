def solution(number, limit, power):

    cnt = 0
    attack = []
    for i in range(1, number+1) :
        for j in range(1,int((i+1)**(1/2))+1):
            # print(i, j)
            if i%j == 0 :
                cnt+=1
                if j**2 != i :
                    cnt+=1
                
        attack.append(cnt)
        cnt = 0
        
    # print(attack)
        
    for i in range(len(attack)) :
        if attack[i] > limit :
            attack[i] = power
    
    return sum(attack)
