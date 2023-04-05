def solution(arr):
    answer = [-1]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    stack = 0
    for i in range(len(arr)):
        if answer[stack] != arr[i]:
            answer.append(arr[i])
            stack+=1
   
    return answer[1:]