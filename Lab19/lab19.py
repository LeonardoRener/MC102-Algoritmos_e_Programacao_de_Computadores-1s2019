# Laboratorio 18 - Convolução
# Nome: Leonardo Rener de Oliveira
# RA: 201270

#=======================================================================================#
def recursao(n, colunas, matriz):
    lista.append(n)
    for i in range(colunas):
        if matriz[n][i] == "1":
            recursao(i, colunas, matriz)
    return None
#=======================================================================================#
entrada = input().split()
matriz = []
lista = []
for i in range(int(entrada[0])):
    linha = input().split()
    matriz.append(linha)
#=======================================================================================#
recursao(int(entrada[1]), int(entrada[0]), matriz)
lista.remove(int(entrada[1]))
lista.sort()
print(int(entrada[1]), end="")
for i in lista:
    print("", i, end="")
print("")