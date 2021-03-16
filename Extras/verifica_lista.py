import copy
# Funcao 1:
# Descricao: verifica se ao trocar um numero da lista a mesma se torna ordenada.
def funcao1(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            lista2 = copy.deepcopy(lista)
            lista2.remove(i)
            for i in range(len(lista2) - 1):
                if lista2[i] > lista2[i + 1]:
                    return False
    return True

try:
    x = int(input())
    while x != 0:
        if x == 1:
            lista = []
            a = input("Digite sua lista: ").split(" ")
            for i in a:
                lista.append(int(i))
            if funcao1(lista) == True:
                print("Sim")
            else:
                print("Nao")


        x = int(input("Digite um numero de 1-4 para escolher uma funcao")
except:
    print("Voce nao digitou um numero valido!")