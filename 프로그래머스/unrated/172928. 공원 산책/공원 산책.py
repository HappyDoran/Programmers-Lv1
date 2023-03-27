def solution(park, routes):
    t, r = 0,0
    move = {"E" : [0,1],"W" : [0,-1],"S" : [1,0],"N" : [-1,0]}
    max_t, max_r = len(park),len(park[0])
    
    for i in range(len(park)):
        if park[i].find("S") > -1 :
            t,r = i, park[i].find("S")
    
    for i in range(len(routes)):
        t_dr,t_c = routes[i].split(" ")
        print(t_dr,t_c)
        new_t,new_r = t,r
        for i in range(int(t_c)):
            if 0 <= new_t+move[t_dr][0] < max_t and 0 <= new_r+move[t_dr][1] < max_r and park[new_t+move[t_dr][0]][new_r+move[t_dr][1]] != "X":
                new_t,new_r = new_t+move[t_dr][0], new_r+move[t_dr][1]
                print(park[move[t_dr][0]][move[t_dr][1]])
                print(new_t,new_r)
            else: 
                new_t,new_r = t,r
                break
        t,r = new_t,new_r 
            
    return [t,r]