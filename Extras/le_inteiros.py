def verifica_int(msg):
    while True:
        val = input(msg)
        try:
            val = int(val)
            break
        except ValueError:
            print("Formato de entrada invalido")
    return val

def verifica_tipo(msg, vType):
    while True:
        val = input(msg)
        try:
            val = vType(val)
            break
        except ValueError:
            print("Formato de entrada invalido")
    return val

def main():
    x = verifica_int("DIgite um inteiro: ")
    tipo = input("Digite o tipo do seu proximo numero: ")
    if tipo == "float":
        a = verifica_tipo("Digite o numero: ", float)
    elif tipo == "int":
        a = verifica_tipo("Digite o numero: ", int)
    print(x)
    print("Voce digitou um numero do tipo", tipo, "e ele é", a)
main()