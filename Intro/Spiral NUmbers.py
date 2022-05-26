def solution(n):
    t = n*n
    c, i = 0, 0
    matrix = [([0]*n) for i in range(n)]
    print(matrix)
    print("\n")
    while c<t:
        T, R, B, L = i, i, n-(i+2), n-(i+1)
        
#TOP
        while T < n-i:
            c += 1
            matrix[R][T] = c
            T+=1
#
        R += 1
        T -= 1
#RIGHT
        while R < n-i:
            c += 1
            matrix[R][T] = c
            R += 1
#BOTTOM
        while B >= i:
            c += 1
            matrix[L][B] = c
            B -= 1
#
        B += 1
        L -= 1
#LEFT
        while L > i:
            c += 1
            matrix[L][B] = c
            L -= 1
#
        L += 1
        i += 1
    return matrix
