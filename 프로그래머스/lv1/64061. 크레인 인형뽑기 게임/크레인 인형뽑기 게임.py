def solution(board, moves):
    answer = 0
    cnt = 0
    bingo = []
    
    for i in range(len(moves)):
        cnt = 0
        while cnt < len(board):
            if board[cnt][moves[i]-1] == 0 :
                cnt+=1
            else :
                break
        if cnt != len(board):
            bingo.append(board[cnt][moves[i]-1])
            if len(bingo) >=2 :
                if bingo[len(bingo) - 1] ==  bingo[len(bingo) - 2]:
                    answer+=2
                    bingo.pop()
                    bingo.pop()
                    print(bingo)
            print(board[cnt][moves[i]-1])
            board[cnt][moves[i]-1] = 0
            
    return answer