#Leonardo Rener de Oliveira RA: 201270
#O programa possui duas partes, uma para o raund 1 e outra para o raund 2, o programa calcula os danos e verifica se e uma sequencia
#com base no valor ser maior ou menor que zero, a funcao "maisdano" verifica se o numero é perfeito ou triangular e atribui adevida multiplicaçao.
def maisdano(n):     #funcao que ira verificar e aplicar as multiplicacoes
    f = 0
    if n < 0:
        n = n * -1
        f = 1
    lista = []
    for i in range(1,(n-1)):     #verifica se é perfeito
        divisores = n % i
        if divisores == 0:
            lista.append(i)
    soma = 0
    for i in range(len(lista)):
        b = lista[i]
        soma = b + soma
    if f == 1:
        soma = soma * -1
        n = n * -1
    if soma == n:
        m = n * 3
    else:                 #caso nao seja perfeito verifica se é triangular antes de sair da funçao
        if n < 0:
            n = n * -1
            f = 1
        soma = 0
        for i in range(1, n):    #verifica se é triangular
            if soma < n:
                soma += i
        if f == 1:
            soma = soma * -1
            n = n * -1
        if soma == n:
            m = n * 2
        else:
            m = n
    return(m)
vidaryu = 2000          #vida inicial do ryu
vidaken = 2000          #vida inicial do ken
dano1 = int(input())    #primeiro golpe
dano1 = maisdano(dano1) #verifica se o numero e perfeito ou triangular, caso seja aplica a multiplicacao de dano respectiva.

while vidaken > 0 and vidaryu > 0:     #enquanto a vida dos lutadores for maior que zero o loop continua

    if vidaken - dano1 <= 0:       #so entra nessa parte se for o ultimo golpe
        x2 = vidaken - dano1
        print("Ken:", vidaken, "-", dano1, "=", x2)
        vidaken = x2
        dano1 = 0

    if vidaryu + dano1 <= 0:       #so entra se for o ultimo golpe
        total = vidaryu + dano1
        print("Ryu:", vidaryu, "-", dano1 * -1, "=", total)
        vidaryu = total
        dano1 = 0

    while dano1 > 0 and vidaken > 0 and vidaryu > 0 and vidaken - dano1 > 0:   #calcula o dano e a sequencia (se houver) causada pelo ryu no ken
        dano2 = int(input())
        dano2 = maisdano(dano2)
        while dano2 > 0 and vidaken - dano1 > 0:     #o while continua ate a entrada de um numero negativo
            dano1 = dano1 + dano2
            if vidaken - dano1 > 0:
                dano2 = int(input())
                dano2 = maisdano(dano2)
        x2 = vidaken - dano1
        print("Ken:", vidaken, "-", dano1,"=", x2)             #imprime o dano sofrido e vida restante do ken
        vidaken = x2
        dano1 = dano2

    while dano1 < 0 and vidaken > 0 and vidaryu > 0 and vidaryu + dano1 > 0:   #calcula o dano e a sequencia (se houver) causada pelo ken no ryu
        dano2 = int(input())
        dano2 = maisdano(dano2)
        while dano2 < 0 and vidaryu + dano1 > 0:              #o while continua ate a entrada de um numero possitivo
            dano1 = dano1 + dano2
            if vidaryu + dano1 > 0:
                dano2 = int(input())
                dano2 = maisdano(dano2)
        total = vidaryu + dano1
        print("Ryu:", vidaryu, "-", dano1 * -1, "=", total)    #imprime o dano sofrido e vida restante do ryu
        vidaryu = total
        dano1 = dano2

if vidaken > 0:      #sistema para saber quem ganhou o a partida ou se empatou
    vitoria = 1      #se o ken tiver vida maior que zero ele ganhou esse round
else:
    vitoria = 2      #se o ken tiver vida menor que zero o ryu ganhou o round

vidaryu = 2000   #vida inicial do ryu
vidaken = 2000   #vida inicial do ken
dano1 = int(input())    #primeiro golpe
dano1 = maisdano(dano1)
while vidaken > 0 and vidaryu > 0:     #enquanto a vida dos lutadores for maior que zero o loop continua

    if vidaken - dano1 <= 0:       #so entra nessa parte se for o ultimo golpe
        x2 = vidaken - dano1
        print("Ken:", vidaken, "-", dano1, "=", x2)
        vidaken = x2
        dano1 = 0

    if vidaryu + dano1 <= 0:       #so entra se for o ultimo golpe
        total = vidaryu + dano1
        print("Ryu:", vidaryu, "-", dano1 * -1, "=", total)
        vidaryu = total
        dano1 = 0

    while dano1 > 0 and vidaken > 1 and vidaryu > 0 and vidaken - dano1 > 0:   #calcula o dano e a sequencia (se houver) causada pelo ryu no ken
        dano2 = int(input())
        dano2 = maisdano(dano2)
        while dano2 > 0 and vidaken - dano1 > 0:
            dano1 = dano1 + dano2
            if vidaken - dano1 > 0:
                dano2 = int(input())
                dano2 = maisdano(dano2)
        x2 = vidaken - dano1
        print("Ken:", vidaken, "-", dano1,"=", x2)             #imprime o dano sofrido e vida restante do ken
        vidaken = x2
        dano1 = dano2

    while dano1 < 0 and vidaken > 0 and vidaryu > 0 and vidaryu + dano1 > 0:   #calcula o dano e a sequencia (se houver) causada pelo ken no ryu
        dano2 = int(input())
        dano2 = maisdano(dano2)
        while dano2 < 0 and vidaryu + dano1 > 0:
            dano1 = dano1 + dano2
            if vidaryu + dano1 > 0:
                dano2 = int(input())
                dano2 = maisdano(dano2)
        total = vidaryu + dano1
        print("Ryu:", vidaryu, "-", dano1 * -1, "=", total)    #imprime o dano sofrido e vida restante do ryu
        vidaryu = total
        dano1 = dano2

if vidaken > 0:
    vitoria = vitoria + 1
else:
    vitoria = vitoria + 2

if vitoria == 2:               #se a variavel "vitoria" tiver valor 2 siginifica que o ken ganhou os dois rounds (1 + 1)
    print("Ken venceu")
elif vitoria == 4:             #se a variavel "vitoria" tiver valor 4 siginifica que o ryu ganhou os dois rounds (2 + 2)
    print("Ryu venceu")
else:                          #se der um valor diferente de 2 ou 4 (ou seja 3) a partida empatou
    print("empatou")