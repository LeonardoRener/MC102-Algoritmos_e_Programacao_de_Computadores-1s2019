#!/usr/bin/env python3
#========================================================================================================#
# Leonardo Rener de Oliveira RA: 201270                                                                  #
# O objetivo do programa é a criacao de uma biblioteca de funcoes para operacoes com conjuntos numericos.#
#========================================================================================================#
# Funcao: pertence
#
# Parametros:
#   conj: vetor contendo o conjunto de entrada
#    num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se num pertence a conj e False caso contrario
#
def pertence(conj, num):
    # Implementar a funcao e trocar o valor de retorno
    # Essa funcao simplesmente verifica se o numero esta no conjunto, se estiver retorna verdadeiro, do contrario retorna falso.
    if num in conj:
        return True
    return False

# Funcao: contido
#
# Parametros:
#   conj1: vetor contendo um conjunto de entrada
#   conj2: vetor contendo um conjunto de entrada
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#
def contido(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    for i in range(len(conj1)):
        if conj1[i] not in conj2:
            # Se ao menos um numero nao estiver no outro conjunto retorna falso.
            return False
    #Se nao retornou falso entao o conjunto esta contido, retornando verdadeiro:
    return True

# Funcoes: adicao e subtracao
#
# Parametros:
#   conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
def adicao(conj, num):
    # Implementar a funcao
    if num not in conj:
        conj.append(num)
    return

def subtracao(conj, num):
    # Implementar a funcao
    if num in conj:
        conj.remove(num)
    return

# Funcoes: uniao, intersecao e diferenca
#
# Parametros:
#     conj1: vetor contendo o conjunto de entrada do primeiro operando
#     conj2: vetor contendo o conjunto de entrada do segundo operando
#
# Retorno:
#   Vetor contendo o conjunto de saida/resultado da operacao
#
def uniao(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    conj3 = []
    for i in conj1:
        conj3.append(i)
    for i in range(len(conj2)):
        if conj2[i] not in conj1:
            conj3.append(conj2[i])
    return conj3

def intersecao(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    conj3 = []
    for i in range(len(conj2)):
        if conj2[i] in conj1:
            conj3.append(conj2[i])
    return conj3

def diferenca(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    conj3 = []
    for i in range(len(conj1)):
        if conj1[i] not in conj2:
            conj3.append(conj1[i])
    return conj3

def uniao_disjunta(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    conj3 = []
    for i in range(len(conj1)):
        if conj1[i] not in conj2:
            conj3.append(conj1[i])
    for i in range(len(conj2)):
        if conj2[i] not in conj1 and conj2[i] not in conj3:
            conj3.append(conj2[i])
    return conj3