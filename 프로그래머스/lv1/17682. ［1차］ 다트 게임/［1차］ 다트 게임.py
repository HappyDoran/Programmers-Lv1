def solution(dartResult):
    answer = 0
    cnt = 0
    keyword = []
    
    for i in range(1, len(dartResult)):
        if dartResult[i]>="0" and dartResult[i]<= "9" and i-cnt != 1 :
            keyword.append(dartResult[cnt:i])
            cnt = i
    keyword.append(dartResult[cnt:])
    print(keyword)
    
    starflag = 0
    achaflag = 0
    numbers = []
    for i in range(len(keyword)):
        number = 0
        for j in range(len(keyword[i])):
            if keyword[i][j] == "S" :
                number = int(keyword[i][:j])**1
            elif keyword[i][j] == "D" :
                number = int(keyword[i][:j])**2
            elif keyword[i][j] == "T" :
                number = int(keyword[i][:j])**3
            if keyword[i][j] == "*":
                if len(numbers) != 0 :
                    numbers[i-1] = numbers[i-1]*2
                number = number*2
            if keyword[i][j] == "#":
                number = -number
        numbers.append(number)
    print(numbers)
    return sum(numbers)