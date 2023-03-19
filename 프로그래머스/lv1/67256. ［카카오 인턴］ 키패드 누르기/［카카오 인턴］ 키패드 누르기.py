import math
def solution(number, hand):
    answer = ''
    current_left_position = [3,0]
    current_right_position = [3,2]
    user = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    for i in range(len(number)):
        if number[i] == 1 or number[i] == 4 or number[i] == 7 :
            answer+='L'
            current_left_position = (user[number[i]])
        elif number[i] == 3 or number[i] == 6 or number[i] == 9 :
            answer+='R'
            current_right_position = (user[number[i]])
        else :
            # print(user[number[i]][0],user[number[i]][1])
            
            # print(current_left_position)
            # print(current_right_position)
            left_direct = abs(user[number[i]][0] - current_left_position[0]) + abs(user[number[i]][1] - current_left_position[1])
            # print(left_direct)
            right_direct = abs(user[number[i]][0] - current_right_position[0]) + abs(user[number[i]][1] - current_right_position[1])
            # print(left_direct,right_direct)
            if left_direct < right_direct :
                answer+='L'
                current_left_position = (user[number[i]])
            elif left_direct > right_direct :
                answer+='R'
                current_right_position = (user[number[i]])
            else :
                if hand == 'right' :
                    answer+='R'
                    current_right_position = (user[number[i]])
                else :
                    answer+='L'
                    current_left_position = (user[number[i]])
                       
    # print(user)
    return answer