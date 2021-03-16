#Leonardo Rener de Oliveira RA: 201270
#O programa possui duas partes, uma para o raund 1 e outra para o raund 2, o programa calcula os danos e verifica se e uma sequencia
#com base no valor ser maior ou menor que zero.
vidaryu = 50   #vida inicial do ryu
vidaken = 50   #vida inicial do ken
dano1 = int(input())    #primeiro golpe
while vidaken > 0 and vidaryu > 0:     #enquanto a vida dos lutadores for maior que zero o loop continua no raund 1

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
        while dano2 > 0 and vidaken - dano1 > 0:
            dano1 = dano1 + dano2
            if vidaken - dano1 > 0:
                 dano2 = int(input())
        x2 = vidaken - dano1
        print("Ken:", vidaken, "-", dano1,"=", x2)             #imprime o dano sofrido e vida restante do ken
        vidaken = x2
        dano1 = dano2

    while dano1 < 0 and vidaken > 0 and vidaryu > 0 and vidaryu + dano1 > 0:   #calcula o dano e a sequencia (se houver) causada pelo ken no ryu
        dano2 = int(input())
        while dano2 < 0 and vidaryu + dano1 > 0:
            dano1 = dano1 + dano2
            if vidaryu + dano1 > 0:
                 dano2 = int(input())
        total = vidaryu + dano1
        print("Ryu:", vidaryu, "-", dano1 * -1, "=", total)    #imprime o dano sofrido e vida restante do ryu
        vidaryu = total
        dano1 = dano2

if vidaken > 0:      #sistema para saber quem ganhou o a partida ou se empatou
    vitoria = 1      #se o ken tiver vida maior que zero ele ganhou esse round
else:
    vitoria = 2      #se o ken tiver vida menor que zero o ryu ganhou o round

vidaryu = 50   #vida inicial do ryu
vidaken = 50   #vida inicial do ken
dano1 = int(input())    #primeiro golpe
while vidaken > 0 and vidaryu > 0:     #enquanto a vida dos lutadores for maior que zero o loop continua no raund 1

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
        while dano2 > 0 and vidaken - dano1 > 0:
            dano1 = dano1 + dano2
            if vidaken - dano1 > 0:
                 dano2 = int(input())
        x2 = vidaken - dano1
        print("Ken:", vidaken, "-", dano1,"=", x2)             #imprime o dano sofrido e vida restante do ken
        vidaken = x2
        dano1 = dano2

    while dano1 < 0 and vidaken > 0 and vidaryu > 0 and vidaryu + dano1 > 0:   #calcula o dano e a sequencia (se houver) causada pelo ken no ryu
        dano2 = int(input())
        while dano2 < 0 and vidaryu + dano1 > 0:
            dano1 = dano1 + dano2
            if vidaryu + dano1 > 0:
                 dano2 = int(input())
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