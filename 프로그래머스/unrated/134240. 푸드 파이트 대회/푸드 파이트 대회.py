def solution(food):
    answer = ''
    rewsna = ''
    f = []
    f.append(0)
    cnt = 1
    
    for i in range(1,len(food)):
        f.append(food[i]//2)
    
    for i in range(1,len(f)):
        answer+=str(i)*f[i]
    
    rewsna = list(answer)
    rewsna.reverse()
    rewsna = "".join(rewsna)
    
    answer+='0'
    
    answer+=rewsna
    
    
        
    return answer