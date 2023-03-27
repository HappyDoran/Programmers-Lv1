from collections import Counter

def solution(participant, completion):
    answer = ''
    p_dict = Counter(participant)
    c_dict = Counter(completion)

    # print(p_dict)
    # print(c_dict)
    
    # print((p_dict-c_dict).keys())
    
    for p_name in p_dict:
        if p_dict[p_name] != c_dict[p_name]:
            answer = p_name

    return answer