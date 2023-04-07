def solution(n, lost, reserve):
    answer = 0
    
    lost_len = len(lost)
    
    cur_reserve = set(reserve)-set(lost) 
    cur_lost = set(lost)-set(reserve) 
    
    for i in cur_reserve :
        if (i-1) in cur_lost :
            cur_lost.remove(i-1)
            
        elif (i+1) in cur_lost :
            cur_lost.remove(i+1)
    
    answer = n - len(cur_lost)
            
    return answer