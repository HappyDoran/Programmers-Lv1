def solution(sizes):
    answer = 0
    width = []
    height = []
    for i in range(len(sizes)):
        width.append(max(sizes[i][0],sizes[i][1]))
        height.append(min(sizes[i][0],sizes[i][1]))
    
    
    return max(width)*max(height)