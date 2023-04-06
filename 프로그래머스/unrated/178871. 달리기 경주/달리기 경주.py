def solution(players, callings):
    rank = {}
    play = {}
#     for i in range(len(callings)):
#         index = players.index(callings[i])
#         tmp = players[index-1]
#         players[index-1] = players[index]
#         players[index] = tmp
    
#     print(players)
    
    for index,item in enumerate(players):
        rank[index+1] = item
        play[item] = index+1
    
    # print(play)
    # print(rank)
    
    for i in callings:
        cur_rank = play[i]
        pre_rank = cur_rank-1
        pre_play = rank[pre_rank]

        rank[cur_rank - 1], rank[cur_rank] = rank[cur_rank], rank[cur_rank - 1]
        play[pre_play], play[i] = play[i], play[pre_play]
    
    return (list(rank.values()))
    # return players