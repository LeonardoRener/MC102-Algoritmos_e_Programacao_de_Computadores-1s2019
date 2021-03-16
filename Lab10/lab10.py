#Leonardo Rener de Oliveira RA: 201270
#O programa ira ler a quantidade "n" de linhas que seram inseridas, depois ira separar o ID, o PCa e o PCf em listas.
#Apos isso o programa ficaram em um loop verificando o ID e o PCa que forem digitados e retornando o PCf ate que sejam digitados 0 0 como entrada.
import math
import playsound
def funcao(ID, inicial):    #funcao que ira retornar o PCf com base no ID e do PCa
    a = 0
    lista = []
    media = 0
    for i in range(len(I)):    #Consulta em quais locais da lista "I" o ID aparece
        if I[i] == ID:
            lista.append(a)
        a += 1
    for i in lista:            #Faz a media entre os PCf e PCa onde o ID aparece em "I"
        media += PCf[i] / PCa[i]
    mediaf = media / len(lista)
    total = math.ceil(inicial * mediaf)
    return(total)
I = []
PCa = []
PCf = []
n = int(input())
#easter egg, favor desconsiderar:
if n == 1997:
    playsound.playsound('lab10.mp3')
#fim do easter egg.
for i in range(n):            #Separa a entrada em tres lista: "I" para o ID, e PCa e PCf
    linha = input()
    ints = [int(i) for i in linha.split()]
    I.append(ints[0])
    PCa.append(ints[1])
    PCf.append(ints[2])

consulta = input()
c = [int(i) for i in consulta.split()]   #separa a entrada nas variaveis ID e inicial
ID = c[0]
inicial = c[1]
while ID != 0 and inicial != 0:    #Enquanto o ID e o PCa que forem digitados forem diferentes de 0 o loop continua
    print(funcao(ID, inicial))
    consulta = input()
    c = [int(i) for i in consulta.split()]
    ID = c[0]
    inicial = c[1]