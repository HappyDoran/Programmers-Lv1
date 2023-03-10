def solution(keymap, targets):
    answer = []
    key = []
    for i in range(len(targets)):
        key = [] 
        for j in range(len(targets[i])):
            min_key = []
            for key_list in keymap:
                if targets[i][j] in key_list:
                    # print(targets[i][j])
                    min_key.append(key_list.index(targets[i][j]))
            # print(min_key)
            if min_key == []:
                key.append(-1)
            else :
                key.append(min(min_key)+1)
                # print(key)
        if -1 in key:
            answer.append(-1)
        else:
            answer.append(sum(key))
    return answer