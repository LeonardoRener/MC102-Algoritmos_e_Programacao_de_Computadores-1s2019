#Leonardo Rener de Oliveira RA: 201270
#O programa ira receber os valores do tamanho da matriz e quantidade de dias, ultilizando do comando for ira receber os dados das linhas e colunas,
#depois a funcao "zumbis" ira checar as condicoes e fazer as modificoes ao depender dos resultado, depois um for imprimira cada elemento da matriz.

from copy import deepcopy  #usarei o comando deepcopy para clonar a matriz inicial.
def zumbis(matriz, linha, coluna):
    matrizatual = deepcopy(matriz)
    for l in range(1, linha+1):
        for c in range(1, coluna+1):
            humano = 0
            if matriz[l][c] == 0:             #Verifica quando o elemento é vazio
                if matriz[l-1][c-1] == 1:
                    humano += 1
                if matriz[l-1][c] == 1:
                    humano += 1
                if matriz[l-1][c+1] == 1:
                    humano += 1
                if matriz[l][c-1] == 1:
                    humano += 1
                if matriz[l][c+1] == 1:
                    humano += 1
                if matriz[l+1][c-1] == 1:
                    humano += 1
                if matriz[l+1][c] == 1:
                    humano += 1
                if matriz[l+1][c+1] == 1:
                    humano += 1
                if humano == 2:                #Se possuir exatamente 2 humanos como vizinhos, muda o elemento de 0 para 1
                    matrizatual[l][c] = 1
                    ####
            elif matriz[l][c] == 1:            #Verifica quando o elemento é humano
                if matriz[l-1][c-1] == 2:
                    matrizatual[l][c] = 2
                elif matriz[l-1][c] == 2:
                    matrizatual[l][c] = 2
                elif matriz[l-1][c+1] == 2:
                    matrizatual[l][c] = 2
                elif matriz[l][c-1] == 2:
                    matrizatual[l][c] = 2
                elif matriz[l][c+1] == 2:
                    matrizatual[l][c] = 2
                elif matriz[l+1][c-1] == 2:
                    matrizatual[l][c] = 2
                elif matriz[l+1][c] == 2:
                    matrizatual[l][c] = 2
                elif matriz[l+1][c+1] == 2:
                    matrizatual[l][c] = 2
                    ####
            elif matriz[l][c] == 2:           #Verifica quando o elemento é zumbi
                if matriz[l-1][c-1] == 1:
                    humano += 1
                if matriz[l-1][c] == 1:
                    humano += 1
                if matriz[l-1][c+1] == 1:
                    humano += 1
                if matriz[l][c-1] == 1:
                    humano += 1
                if matriz[l][c+1] == 1:
                    humano += 1
                if matriz[l+1][c-1] == 1:
                    humano += 1
                if matriz[l+1][c] == 1:
                    humano += 1
                if matriz[l+1][c+1] == 1:
                    humano += 1
                if humano != 1:              #Caso tenha dois ou mais humanos como vizinho muda o elemento de 2 para 0
                    matrizatual[l][c] = 0
    return(matrizatual)        #Transforma a copia da matriz na matriz atual

matriz = []
entrada = input().split(' ')
dias = int(input())
extra = [9 for i in range(int(entrada[1])+2)]
matriz.append(extra)

for i in range(int(entrada[0])):
    atual = input().split(' ')
    atual = [int(i) for i in atual]
    atual.insert(0, 9)
    atual.append(9)
    matriz.append(atual)

matriz.append(extra)

for d in range(dias+1):
    print("iteracao", d)
    for l in range(1, int(entrada[0])+1):
        for c in range(1, int(entrada[1])+1):
            print(matriz[l][c], end='')
        print()
    matriz = zumbis(matriz, int(entrada[0]), int(entrada[1]))