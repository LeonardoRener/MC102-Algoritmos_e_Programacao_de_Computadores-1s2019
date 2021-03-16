#!/usr/bin/env python3

# Laboratorio 20 - Sudoku
# Nome: Leonardo Rener de Oliveira
# RA: 201270

from lab20_main import print_sudoku

# Funcao: print_sudoku
# Essa funcao ja esta implementada no arquivo lab20_main.py
# A funcao imprime o tabuleiro atual do sudoku de forma animada, isto e,
# imprime o tabuleiro e espera 0.1s antes de fazer outra modificacao.
# Voce deve chamar essa funcao a cada modificacao na matriz resposta, assim
# voce tera uma animacao similar a apresentada no enunciado.
# Essa funcao nao tem efeito na execucao no Susy, logo nao ha necessidade de
# remover as chamadas para submissao.

# O aluno pode criar outras funcoes que ache necessario

#=======================================================================================#

# Funcao: resolve
# Resolve o Sudoku da matriz resposta.
# Retorna True se encontrar uma resposta, False caso contrario



def resolve(resposta):
    # Implementar a funcao e trocar o valor de retorno
    encontrar = achar_vazio(resposta)
    if not encontrar:
        return True
    else:
        linha, coluna = encontrar

    print_sudoku(resposta)

    for i in range(1, 10):
        if verifica(resposta, i, (linha, coluna)):
            resposta[linha][coluna] = i
            if resolve(resposta):
                return True

            resposta[linha][coluna] = 0

    return False

#=======================================================================================#

# Funcao: achar_vazio
# Acha as posicoes vazias
# Entrada: matriz "M"
# Retorno: linha e coluna
def achar_vazio(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 0:
                return (i, j)

#=======================================================================================#

# Funcao: verifica
# verifica se o numero esta correto, para isso verifica as linhas, colunas e o bloco
# Entrada: matriz "M", numero "num" e posicao "pos"
# Retorno: True ou False
def verifica(M, num, pos):
    # Verifica a coluna:
    for i in range(len(M)):
        if M[i][pos[1]] == num and pos[0] != i:
            return False

    #Verifica a linha:
    for i in range(len(M[0])):
        if M[pos[0]][i] == num and pos[1] != i:
            return False

    # Verifica o bloco:
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if M[i][j] == num and (i,j) != pos:
                return False

    return True