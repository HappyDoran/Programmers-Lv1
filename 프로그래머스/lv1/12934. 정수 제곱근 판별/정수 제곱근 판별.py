def solution(n):
    answer = 0
    if n**(1/2) == int(n**(1/2)) :
        return (n**(1/2)+1)**2
    else :
        return -1
    return answer