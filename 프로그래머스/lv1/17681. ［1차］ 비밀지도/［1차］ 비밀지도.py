def binary(n,length):
    s = ""
    while n >= 1:
        s = str(n % 2) + s
        n = n // 2
    
    if len(s) < length :
        while len(s) != length:
            s = "0" + s
    
    return list(s)

def solution(n, arr1, arr2):
    
    answer = []
    arr_1 = []
    arr_2 = []
    s = ""
    
    for i in range(len(arr1)):
        arr_1.append(binary(arr1[i],n))
    
    for i in range(len(arr2)):
        arr_2.append(binary(arr2[i],n))
    
    for i in range(n):
        s = ""
        for j in range(n):
            if arr_1[i][j] == '1' or arr_2[i][j] == '1' :
                s += '#'
            else:
                s += ' '
        answer.append(s)
    print(answer)
    
    return answer