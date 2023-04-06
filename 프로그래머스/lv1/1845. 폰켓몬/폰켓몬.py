def solution(nums):
    answer = 0
    many = len(nums)
    
    nums = list(set(nums))
    if many/2 > len(nums) :
        return len(nums)
    else :
        return many/2
    return answer