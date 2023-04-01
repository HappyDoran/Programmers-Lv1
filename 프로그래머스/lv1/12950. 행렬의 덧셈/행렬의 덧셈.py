#def matrix(x,y):
    
    
def solution(arr1, arr2):
    answer = []
    a = []
    for i in range(len(arr1)):
        # print(arr1[i])
        # print(arr2[i])
        a = []
        for j in range(len(arr1[i])):
            a.append(arr1[i][j]+arr2[i][j])
        answer.append(a)
    
    return answer