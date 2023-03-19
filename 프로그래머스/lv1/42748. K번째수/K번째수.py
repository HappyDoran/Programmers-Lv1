def solution(array, commands):
    hello = []
    for i in range(len(commands)):
        answer = []
        for j in range(commands[i][0], commands[i][1]+1):
            answer.append(array[j-1])
        answer.sort()
        print(answer)
        hello.append(answer[commands[i][2]-1])
        print(hello)
    return hello