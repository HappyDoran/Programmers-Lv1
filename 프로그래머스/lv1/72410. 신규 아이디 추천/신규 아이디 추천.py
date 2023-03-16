def solution(new_id):
    answer = ''
    rem = ['-','_','.']
    
    for i in range(len(new_id)):
        if new_id[i] >= 'A' and new_id[i] <= 'Z':
            new_id = new_id.replace(new_id[i],new_id[i].lower()) 
    
    for i in range(len(new_id)):
        if new_id[i] in rem or (new_id[i] >= '0' and new_id[i] <= '9') or new_id[i] >= 'a' and new_id[i] <= 'z' :
            continue
        else :
            new_id = new_id.replace(new_id[i]," ") 
            
    new_id = new_id.replace(" ", "")
    
    while ".." in new_id :
        new_id = new_id.replace("..", ".")
    
    if new_id[0] == '.' :
        new_id = new_id[1:]
    
    if new_id == "" :
        new_id +='a'
        
    if len(new_id) >= 16 :
        new_id = new_id[0 : 15]
    
    if new_id[len(new_id) - 1] == '.':
        new_id = new_id[0 : len(new_id) - 1]
    
    while len(new_id) <= 2 :
        new_id+=new_id[len(new_id) - 1]
    
    print(new_id)
    return new_id