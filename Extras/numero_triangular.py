def triangular(n):
    soma = 0
    for i in range(1, n):
        if soma < n:
            soma += i
    if soma == n:
        m = 1
    else:
        m = 0
    return(m)

a = int(input())

print(triangular(a))