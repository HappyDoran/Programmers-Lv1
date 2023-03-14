def solution(id_list, report, k):
    answer = []
    call_cnt = {} #신고당한 횟수를 담는 dict
    black_list = {}
    report = list(set(report))
    
    for i in id_list:
        call_cnt[i] = 0
        black_list[i] = 0 
    
    # print(call_cnt)
    for i in report:
            A,B = i.split(" ") #분할
            # print(A,B)
            # for elem,index in call_cnt.items():
            #     if B == elem :  
            #         call_cnt[elem]+=1
            call_cnt[B]+=1
                
    print(call_cnt)
    
    for i in report:
            A,B = i.split(" ") #분할
            # print(A,B)
            for elem,index in black_list.items():
                if A == elem :
                    if call_cnt[B] >= k :
                        black_list[A]+=1
                        
    # print(black_list)
    
    for i in black_list.values():
        answer.append(i)
                    
    
            
    
    return answer