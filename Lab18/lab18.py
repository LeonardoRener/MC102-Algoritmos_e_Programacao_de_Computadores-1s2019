# Laboratorio 18 - Convolução
# Nome: Leonardo Rener de Oliveira
# RA: 201270

import sys
#================================================================================================#
# Funcao: Obtem o novo valor p'(x,y) do pixel da imagem resultante da convolução.

def funcao(x, y, m, D, img):
    a = (m[0][0] * img[x - 1][y - 1]) + (m[0][1] * img[x - 1][y]) + (m[0][2] * img[x - 1][y + 1])
    b = (m[1][0] * img[x][y - 1]) + (m[1][1] * img[x][y]) + (m[1][2] * img[x][y + 1])
    c = (m[2][0] * img[x + 1][y - 1]) + (m[2][1] * img[x + 1][y]) + (m[2][2] * img[x + 1][y + 1])
    r = (a + b + c) // D
    if r < 0:
        return 0
    if r > 255:
        return 255
    return r
#================================================================================================#
# Realizando a atribuicao da matriz e da imagem a variaveis, em sequida tranformando estas em matrizes.
imagem = open(sys.argv[1], "r")
p2 = imagem.readline()
k = imagem.readline().split(" ")
colunas = int(k[0])
linhas = int(k[1])
pixel = imagem.readline()
img = []
a = []
for c in range(linhas):
    l = imagem.readline().split(" ")
    for i in range(colunas):
        a.append(int(l[i]))
    img.append(a)
    a = []
#------------------------------------------------------------------------------------------------#
matriz = open(sys.argv[2], "r")
m = []
D = int(matriz.readline())
for c in range(3):
    b = matriz.readline().split()
    for i in range(3):
        a.append(int(b[i]))
    m.append(a)
    a = []
#================================================================================================#
print("P2")
print(colunas, linhas)
print("255")
#================================================================================================#
for i in img[0]:
    print(i, end=" ")
print(" ")
#====================================================================================#
for x in range(1, linhas - 1):
    print(img[x][0], end=" ")
    for y in range(1, colunas - 1):
        print(funcao(x, y, m, D, img), end=" ")
    print(img[x][y+1], end=" ")
    print(" ")
#====================================================================================#
for i in img[linhas-1]:
    print(i, end=" ")
print(" ")
#====================================================================================#