#Nome: Leonardo Rener de Oliveira, RA: 201270
#Esse programa lê um texto, torna todas suas letras minusculas e entao separa todas as palavras
#em uma lista, depois cada elemento dessa lista é checado e se for uma daz palavras-chave imprime na tela.

entrada = str(input()).lower() #recebe o texto e o transforma tudo em letra minuscula.
lista = entrada.split()    #separa as palavras do texto cada uma em um elemento da lista.
for i in range(len(lista)):    #verifica todos os elementos da lista.
    if lista[i] == "mercurio":
        print("N -", end="")
    if lista[i] == "venus":
        print("NE -", end="")
    if lista[i] == "terra":
        print("L -", end="")
    if lista[i] == "marte":
        print("SE -", end="")
    if lista[i] == "jupiter":
        print("S -", end="")
    if lista[i] == "saturno":
        print("SO -", end="")
    if lista[i] == "urano":
        print("O -", end="")
    if lista[i] == "netuno":
        print("NO -", end="")
    if lista[i] == "verde":
        print(" 30")
    if lista[i] == "amarelo":
        print(" 45")
    if lista[i] == "vermelho":
        print(" 60")