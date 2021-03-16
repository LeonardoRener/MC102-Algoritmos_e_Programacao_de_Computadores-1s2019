#Leonardo Rener de Oliveira RA: 201270
#O programa utiliza a funcao "funcao" para analizar se i é divisor de j ou j é divisor de i, caso seja retorna "True"
#apos passar pela funcao os "if" iram imprimir "*" se o retorno for "True", alem disso atribuiram +1 a uma variavel
#"total" que sera a responsavel por dizer quantos "*" foram impressos, caso contrario e o retorno nao for "True" ira imprimir "-".

def funcao(i, j):    #funcao que define se i é divisor de j.
    resultado = 0
    resultado2 = 0
    n = 1
    while n <= j and resultado != j:
        resultado = i * n
        n = n + 1
    n = 1
    while n <= i and resultado2 != i:
        resultado2 = j * n
        n = n + 1
    if resultado == j or resultado2 == i:
        return(True)    #retorno da funcao

entrada = int(input())
total = 0    #total de "*" impressos
linha = 0    #variavel para pular de linha
for i in range(1, entrada+1):
    for j in range(1, entrada+1):
        if linha == entrada:    #se a quantidade de "*" ou "-" impressos for igual a "entrada" ira pular de linha
            print()
            linha = 0    #zera a variavel para contar a nova linha
        if funcao(i, j) == True:
            print("*",end='',sep='')   #se a funcao retornar True imprime "*"
            total += 1  #soma +1 cada vez que imprime "*"
        else:
            print("-",end='',sep='')   #se a funcao retornar True imprime "-"
        linha += 1      #soma +1 cada vez que imprime "*" ou "-"
print()
print(total)