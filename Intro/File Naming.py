def solution(names):
    dup = []    
    for n in names:
        s = n
        i = 1
        while (s in dup):
            s = n + '(' + str(i) + ')'
            i += 1
        
        dup.append(s)
            
    return dup
