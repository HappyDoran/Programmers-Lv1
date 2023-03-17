def solution(m, n, startX, startY, balls):
    answer = []
    reflect = []
    # -3 7
    reflect.append([-startX, startY])
    # 17 7
    reflect.append([2*m - startX, startY])
    # 3 13
    reflect.append([startX, 2*n - startY])
    # 3 -7
    reflect.append([startX, -startY])
    # -3 -7
    reflect.append([-startX, -startY])
    # -3 13
    reflect.append([-startX, 2*n - startY])
    # 17 13
    reflect.append([2*m - startX, 2*n- startY])
    # 17 -7
    reflect.append([2*m - startX, -startY])
    
    for i in range(len(balls)):
        distance = []
        if startX == balls[i][0]:
            if startY >= balls[i][1]:
                distance.append((reflect[2][0] - balls[i][0])**2 + (reflect[2][1] - balls[i][1])**2)
            
            elif startY <= balls[i][1]:
                distance.append((reflect[3][0] - balls[i][0])**2 + (reflect[3][1] - balls[i][1])**2)
            
            for j in range(0, 2):
                distance.append((reflect[j][0] - balls[i][0])**2 + (reflect[j][1] - balls[i][1])**2)
                
            for j in range(4, len(reflect)):
                distance.append((reflect[j][0] - balls[i][0])**2 + (reflect[j][1] - balls[i][1])**2)
                
        elif startY == balls[i][1]:
            if startX <= balls[i][0]:
                distance.append((reflect[0][0] - balls[i][0])**2 + (reflect[0][1] - balls[i][1])**2)
            
            elif startX >= balls[i][0]:
                distance.append((reflect[1][0] - balls[i][0])**2 + (reflect[1][1] - balls[i][1])**2)
            
            for j in range(2, len(reflect)):
                distance.append((reflect[j][0] - balls[i][0])**2 + (reflect[j][1] - balls[i][1])**2)
        
        else :
            for j in range(len(reflect)):
                distance.append((reflect[j][0] - balls[i][0])**2 + (reflect[j][1] - balls[i][1])**2)
                
        answer.append(min(distance))
        
            
            
    return answer