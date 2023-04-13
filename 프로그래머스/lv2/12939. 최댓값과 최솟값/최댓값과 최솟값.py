def solution(s):
    answer = 0
    array = s.split(" ")
    
    for i in range(len(array)):
        array[i] = int(array[i])
    answer = str(min(array)) + " " + str(max(array))
    return answer