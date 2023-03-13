def solution(today, terms, privacies):
    answer = []
    T = {}
    year,month,day = today.split(".")
    year = int(year)
    month = int(month)
    day = int(day)
    
    deadline = {}
    
    # print(year,month,day)
    
    for i in terms:
        Y,period = i.split(" ")
        T[Y] = int(period)
        
    
    cnt = 1
    
    for i in privacies: 
        when,whatY = i.split(" ")
        when_year,when_month,when_day = when.split(".")
        
        when_year = int(when_year)
        when_month = int(when_month)
        when_day = int(when_day)-1
        
        if when_day == 0 :
            when_month = when_month - 1
            if when_month == 0 :
                when_year = when_year - 1
                when_month = 12
            when_day = 28
            
        # print(T[whatY])
        
        dd_year = when_year
        dd_month = when_month + T[whatY]
        dd_day = when_day
        
        print("만료일자", dd_year, dd_month, dd_day)
        
        if dd_month > 12 :
            dd_year = dd_year + int(dd_month / 12)
            dd_month = dd_month % 12
        if dd_month == 0 :
            dd_month = 12
            dd_year = dd_year-1
        print("만료일자", dd_year, dd_month, dd_day)
        print("오늘일자",year,month,day)
        
        if year > dd_year : 
            answer.append(cnt)
            
        elif year == dd_year :
            if month > dd_month:
                answer.append(cnt)
                
            elif month == dd_month:
                if day > dd_day:
                    answer.append(cnt)
                    
        cnt+=1
                
            
        
    
    return answer