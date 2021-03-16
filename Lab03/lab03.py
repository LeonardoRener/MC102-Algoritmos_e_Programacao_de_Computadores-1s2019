d = float(input())
h = float(input())
a = float(input())
b = float(input())
c = float(input())
r = d / 2
v = 3.14 * (r * r) * h
v1 = v * 1000
if v1 >= a:
    print("posto A foi reabastecido")
    v2 = float(v1 - a)
else:
    print("posto A nao foi reabastecido")
    v2 = v1
if v2 >= b:
    print("posto B foi reabastecido")
    v3 = float(v2 - b)
else:
    print("posto B nao foi reabastecido")
    v3 = v2
if v3 >= c:
    print("posto C foi reabastecido")
else:
    print("posto C nao foi reabastecido")