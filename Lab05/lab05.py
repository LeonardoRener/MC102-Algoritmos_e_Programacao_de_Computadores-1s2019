#Leonardo Rener de Oliveira RA: 201270
#O programa analiza os dados de entrada e se ouver combustivel suficiente imprime "sim" e o tempo em que conseguiu
#caso contrario imprime "nao" e o tempo em que o escudo acabou

t = int(input())         #tempo ate o escudo acabar
c = int(input())         #combustivel necessario para conseguir fugir
n = 0                    #variavel que dira o instante em que a nave conseguil fugir
lista = input().split(" ")        #lista que armazena as informacoes sobre o combustivel
a = 0                             #variavel que armazenara o total de combustivel
while n < t and a < c:      #loop que verifica se o combustivel e suficiente e em qual instante.
    b = int(lista[n])       #trasforma o valor na lista em inteiro
    a = b + a
    n = n + 1
if a >= c:             #Verifica se o combustivel total(a) e suficiente, ou seja maior/igual ao combustivel necessario(c).
    print("sim")       #A nave nao teve combustivel para se teleportar a tempo
    print(n)
else:
    print("nao")
    print(t+1)