def solution(cards1, cards2, goal):
    answer = ''
    
    while len(goal) > 0 :
        if len(cards1) > 0 and len(cards2) > 0 :
            if cards1[0] == goal[0]:
                cards1.pop(0)
                goal.pop(0)
            elif cards2[0] == goal[0]:
                cards2.pop(0)
                goal.pop(0)
            else :
                return "No"
        
        elif len(cards1) == 0 : 
            if cards2[0] == goal[0]:
                cards2.pop(0)
                goal.pop(0)
            else :
                return "No"
        
        elif len(cards2) == 0 : 
            if cards1[0] == goal[0]:
                cards1.pop(0)
                goal.pop(0)
            else :
                return "No"
        
        
    if len(goal) == 0 :
        return "Yes"
    return answer