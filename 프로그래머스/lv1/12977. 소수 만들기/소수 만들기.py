def solution(nums):
    answer = 0
    answer2 = 0
    a = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(0, len(nums)-2):
        for j in range(i + 1, len(nums)-1):
            for k in range(j + 1, len(nums)):
                a.append(nums[i]+nums[j]+nums[k])
    print(list(set(a)))
    
    for i in range(len(a)):
        answer = 0
        for j in range(1,a[i]+1):
            if a[i]%j == 0 :
                answer+=1
        if answer == 2 :
            answer2+=1

    return answer2