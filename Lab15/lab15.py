#!/usr/bin/env python3
#*******************************************************************************
# Funcao: atualizaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato
#   jogo: string contendo as informações de um jogo no formato especificado no lab.
#
# Descrição:
#   Deve inserir as informações do parametro 'jogo' na tabela.
#   OBSERVAÇÃO: nesse momento não é necessário ordenar a tabela, apenas inserir as informações.
def atualizaTabela(tabela, jogo):
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************
    jogo = jogo.split()
    saldo1 = int(jogo[1]) - int(jogo[3])
    saldo2 = int(jogo[3]) - int(jogo[1])
    if jogo[1] > jogo[3]:
        v1 = 1
        v2 = 0
        a = 3
        b = 0
    elif jogo[1] < jogo[3]:
        v1 = 0
        v2 = 1
        a = 0
        b = 3
    else:
        a = b = 1
        v1 = v2 = 0
    for i in range(len(tabela)):
        if tabela[i][0] == jogo[0]:
            tabela[i][1] = tabela[i][1] + a
            tabela[i][2] = tabela[i][2] + v1
            tabela[i][3] = tabela[i][3] + saldo1
            tabela[i][4] = tabela[i][4] + int(jogo[1])
        elif tabela[i][0] == jogo[4]:
            tabela[i][1] = tabela[i][1] + b
            tabela[i][2] = tabela[i][2] + v2
            tabela[i][3] = tabela[i][3] + saldo2
            tabela[i][4] = tabela[i][4] + int(jogo[3])
#*******************************************************************************
# Funcao: comparaTimes
#
# Parametros:
#   time1: informações de um time
#   time2: informações de um time
#
# Descricão:
#   retorna 1, se o time1>time2, retorna -1, se time1<time2, e retorna 0, se time1=time2
#   Observe que time1>time2=true significa que o time1 deve estar em uma posição melhor do que o time2 na tabela.
def comparaTimes(time1, time2):
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************
    for i in range(1, 5):
        if time1[i] > time2[i]:
            return 1
        elif time1[i] < time2[i]:
            return -1
    return 0
#*******************************************************************************
# Funcao: ordenaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descricão:
#   Deve ordenar a tabela com campeonato de acordo com as especificaçoes do lab.
#
def ordenaTabela(tabela):
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************
    for i in range(len(tabela) -1 ,0 , -1):
        for j in range(i):
            if comparaTimes(tabela[j], tabela[j+1]) == -1:
                tabela[j], tabela[j+1] = tabela[j+1], tabela[j]
#*******************************************************************************
# Funcao: imprimeTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descrição:
#   Deve imprimir a tabela do campeonato de acordo com as especificações do lab.
def imprimeTabela(tabela):
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************
    for i in range(len(tabela)):
        for j in range(4):
            print("{}, ".format(tabela[i][j]), end='')
        print(tabela[i][4])