#!/usr/bin/env python3

import math

# Laboratorio 17 - Banco de Dados Geografico
# Nome: Leonardo Rener de Oliveira
# RA: 201270

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cidade:
    def __init__(self, coordenadas, inicioCEP, fimCEP, numHabitantes):
        self.coordenadas = coordenadas
        self.inicioCEP = inicioCEP
        self.fimCEP = fimCEP
        self.numHabitantes = numHabitantes

#
# Funcao: distancia
#
# Parametros:
#   a, b: pontos
#
# Retorno:
#   A distancia euclidiana entre a e b.
#
def distancia(c1, c2):
    return int(100 * math.sqrt((c1.x - c2.x)**2 + (c1.y - c2.y)**2)) / 100.0

# Funcao: consulta_cidade_por_cep
#
# Parametros:
#   cidades: lista de cidades (base de dados)
#       cep: CEP desejado
#
# Retorno:
#   O indice da cidade que contem o CEP desejado ou None caso não haja tal cidade.
#
def consulta_cidade_por_cep(cidades, cep):
    # Implementar a funcao e trocar o valor de retorno
    for i in range(len(cidades)):
        if cep >= cidades[i].inicioCEP and cep <= cidades[i].fimCEP:
            return i
    return None

# Funcao: consulta_cidades_por_raio
#
# Parametros:
#            cidades: lista de cidades (base de dados)
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   Lista dos indices das cidades que estao contidas no raio de busca (incluindo
#   a cidade referencia) *ordenados pelas respectivas distancias da cidade referencia*.
#
def consulta_cidades_por_raio(cidades, cidadeReferencia, raio):
    # Implementar a funcao e trocar o valor de retorno
    lista = []
    for i in range(len(cidades)):
        dist = distancia(cidades[cidadeReferencia].coordenadas, cidades[i].coordenadas)
        if dist <= raio:
            a = [i, dist]
            lista.append(a)
#-----------------------------------------------------------------------#
    #   Ordena a lista
    for i in range(len(lista) - 1, 0, -1):
        for j in range(i):
            if lista[j][1] > lista[j + 1][1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    final = []
    for w in range(len(lista)):
        final.append(lista[w][0])
#-----------------------------------------------------------------------#
    return final

# Funcao: populacao_total
#
# Parametros:
#            cidades: lista de cidades (base de dados)
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   O numero de habitantes das cidades que estao contidas no raio de busca
#
def populacao_total(cidades, cidadeReferencia, raio):
    # Implementar a funcao e trocar o valor de retorno
    total = []
    lista = consulta_cidades_por_raio(cidades, cidadeReferencia, raio)
    for i in lista:
        total.append(cidades[i].numHabitantes)
    return sum(total)

# Funcao: mediana_da_populacao
#
# Parametros:
#            cidades: lista de cidades (base de dados)
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   Mediana do numero de habitantes das cidades que estao contidas no raio de busca
#
def mediana_da_populacao(cidades, cidadeReferencia, raio):
    # Implementar a funcao e trocar o valor de retorno
    total = []
    lista = consulta_cidades_por_raio(cidades, cidadeReferencia, raio)
    for i in lista:
        total.append(cidades[i].numHabitantes)
    total.sort()
    if len(total) % 2 == 0:
        n = len(total) // 2 - 1
        return(total[n] + total[n + 1]) / 2
    return total[len(total) // 2]