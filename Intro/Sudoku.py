def check(m,i, j):
    a,c,flag = 0,[],True

    while a<3:
        b=0
        while b<3:
            if 0<m[a+i][b+j]<10:
                # print(a+i, b+j)
                if m[a+i][b+j] in c:
                    flag = False
                    return flag
                else:
                    c.append(m[a+i][b+j])
            else:
                flag = False
            b += 1
        a += 1
                
    return flag

def cr(m):
    
    flag = True
    for i in range(len(m)):
        a = []
        for j in range(len(m[0])):
            if 0<m[i][j]<10:
                if m[i][j] in a:
                    flag = False
                    return flag
                else:
                    a.append(m[i][j])
            else:
                flag = False
                return flag
        
        
    for i in range(len(m)):
        a = []
        for j in range(len(m[0])):
            if 0<m[j][i]<10:
                if m[j][i] in a:
                    flag = False
                    return flag
                else:
                    a.append(m[j][i])
            else:
                flag = False
                return flag
    return flag


def solution(d):
    flag = cr(d)
    if flag == False:
        return flag
        
    x = 0
    while x<7:
        y=0
        while y<7:
            flag = flag & check(d,x,y)
            y+=3
        x +=3

    return flag
