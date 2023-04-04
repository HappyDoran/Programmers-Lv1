def solution(n):
    answer = ''
    arr = ["수","박"]
    for i in range(n):
        if i % 2 == 0 :
            answer+= arr[0]
        else :
            answer+= arr[1]
    return answer