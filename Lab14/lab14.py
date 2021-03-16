# Leonardo Rener de Oliveira RA: 201270
# O programa recebera uma lista contendo os RAs iniciais da turma e recebera comando para fazer modificacoes ou imprimir os RAs
# enquanto nao receber como entrada "s". Para buscar a posicao de um RA na lista o programa utilizara um metodo de busca binaria.

def binario(seq, busca, ordem):
    ultimo = len(seq) - 1
    primeiro = 0
    indices = []
    while primeiro <= ultimo:
        centro = (primeiro+ultimo) // 2
        candidato = seq[centro]
        indices.append(centro)
        if busca == candidato:
            return indices, centro
        elif busca > candidato and ordem == "crescente":
            primeiro = centro+1
        elif busca < candidato and ordem == "decrescente":
            primeiro = centro+1
        else:
            ultimo = centro-1
    return indices, -1
# ===================================================================================================
# Entrada da lista de RAs:
lista = input().split()
lista = [int(i) for i in lista]
tarefa = input().split()
# ===================================================================================================
# Verifica a ordenacao da lista.
lista_crescente = lista[:]
lista_crescente.sort()
lista_decrescente = lista[:]
lista_decrescente.sort(reverse=True)
if lista == lista_crescente:
    ordenacao = "crescente"
elif lista == lista_decrescente:
    ordenacao = "decrescente"
else:
    ordenacao = "nao"
# ===================================================================================================
# Roda o programa ate receber a entrada "s".
while tarefa[0] != "s":
    # ===============================================================================================
    # Imprime a lista.
    if tarefa[0] == "p" and lista != []:
        for i in range(len(lista)):
            print(lista[i], end=" ")
        print()
    # ===============================================================================================
    # Ordena a lista.
    if tarefa[0] == "c":
        lista.sort()
        ordenacao = "crescente"

    if tarefa[0] == "d":
        lista.sort(reverse=True)
        ordenacao = "decrescente"
    # ===============================================================================================
    # Realiza a busca binaria na lista.
    if tarefa[0] == "b":
        if ordenacao != "nao":
            resultado = binario(lista, int(tarefa[1]), ordenacao)
            for i in resultado[0]:
                print(i, end=' ')
            print()
            if resultado[1] != -1:
                print("%d esta na posicao: %d" %(int(tarefa[1]), resultado[1]))
            else:
                print("%d nao esta na lista!" %(int(tarefa[1])))
        else:
            print("Vetor nao ordenado!")
    # ===============================================================================================
    # Inclui o item na lista, e o ordena caso a lista já esteja ordenada.
    if tarefa[0] == "i":
        if len(lista) >= 150:
            print("Limite de vagas excedido!")
        elif int(tarefa[1]) in lista:
            print("Aluno ja matriculado na turma!")
        else:
            if ordenacao == "crescente":
                lista.append(int(tarefa[1]))
                lista.sort()
            elif ordenacao == "decrescente":
                lista.append(int(tarefa[1]))
                lista.sort(reverse=True)
            else:
                lista.append(int(tarefa[1]))
    # ===============================================================================================
    # Remove o item da lista caso ele exista.
    if tarefa[0] == "r":
        if len(lista) == 0:
            print("Nao ha alunos cadastrados na turma!")
        elif int(tarefa[1]) in lista:
            lista.remove(int(tarefa[1]))
        else:
            print("Aluno nao matriculado na turma!")
    # ===================================================================================================
    # Recebe o proximo comando:
    tarefa = input().split()
# ==============================================<FIM>====================================================