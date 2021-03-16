def dias(emp, d):
    dia = []
    a = 0
    b = 1
    while b <= (d-1):
        valor1 = emp[a]
        valor2 = emp[b]
        dia.append(valor2 - valor1)
        a += 1
        b += 1
    return(dia)

def funcao(a, atual):
    b = False
    for i in atual:
        print(atual)
        if a >= dia1[i] and a >= dia2[i] and a >= dia3[i] and a >= dia4[i] and a >= 0:
            b = True
    return(b)

def total(dia, e):
    atual = []
    lucro = 0
    valor = 0
    for i in range(len(dia)):
        if dia[i] > 0:
            valor += dia[i]
            atual.append(i)
        if dia[i] <= 0 or i+1 == len(dia):
            if valor > lucro and funcao(valor, atual) == True:
                lucro = valor
                valor = 0
                dias = atual[:]
            else:
                atual.clear()
                valor = 0
    if lucro > 0:
        print("acao %d: compra %d, venda %d, lucro %.2f" % (e, min(dias)+1, max(dias)+2, lucro))
        lucro_total.append(lucro)
    return(None)

emp1 = []
emp2 = []
emp3 = []
emp4 = []
d = int(input())
for i in range(d):
    emp1.append(float(input())) #empresa 1
for i in range(d):
    emp2.append(float(input())) #empresa 2
for i in range(d):
    emp3.append(float(input())) #empresa 3
for i in range(d):
    emp4.append(float(input())) #empresa 4

dia1 = dias(emp1, d)
dia2 = dias(emp2, d)
dia3 = dias(emp3, d)
dia4 = dias(emp4, d)
lucro_total = []

x = total(dia1, 1)
x1 = total(dia2, 2)
x2 = total(dia3, 3)
x3 = total(dia4, 4)

print("Lucro: %.2f" % (sum(lucro_total)))