def solution(s):
    num_str = ['zero','one','two','three','four','five','six','seven','eight','nine']
    answer = 0
    for i in num_str:
        if s.find(i) >= 0 :
            s = s.replace(s[s.find(i) : s.find(i) + len(i)], str(num_str.index(i)))

    return int(s)