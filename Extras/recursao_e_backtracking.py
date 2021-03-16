n = int(input("n = "))
c = int(input("c = "))
x = [0 for i in range(n)]

def solution(n, C, k, R, x):
    if(k == n-1):
        for i in range(0, n-1):
            print("%d + "%x[i], end="")
        print("%d = %d" %(R, C))

    else:
        for x[k] in range(0, R+1):
            solution(n, C, k+1, R-x[k], x)

solution(n, c, 0, c, x)