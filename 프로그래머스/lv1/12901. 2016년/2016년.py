def solution(a, b):
    answer = ''
    date = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    day = ['0','FRI','SAT','SUN','MON','TUE','WED','THU']
    cnt = 0
    
    for i in range(1, a):
        cnt = cnt + date[i]
    cnt = (cnt + b) % 7
    if cnt == 0 :
        cnt = 7
    print(cnt)
    
    return day[cnt]