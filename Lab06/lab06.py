#Leonardo Rener de Oliveira RA: 201270
#O programa ira primeiramente ler a capacidade do estacionamento e guardar em uma variavel
#depois o comando while vai verificar se a vaga para os carros que chegarem ou se abriu vaga devido aos carros que sairam
#mudando sempre a capacidade atual, o programa e finalizado ao digitar 0.
capacidade = int(input())
a = int(input())
while a !=0:   #loop que verifica se o carro esta sainda, entrando e se tem vagas suficientes
    if capacidade - a < 0:      #verifica se cabe o veiculo no estacionamento
        print("Veiculo muito grande! Capacidade restante:",capacidade)
        a = int(input())
    else:
        if a > 0:    #se o numero e maior que zero o veiculo esta entrando
            capacidade = capacidade - a
            print("Seja bem-vindo! Capacidade restante:",capacidade)
            a = int(input())
        if a < 0:    #se o numero e menor que zero o veiculo esta saindo do estacionamento
            a = a * -1
            capacidade = capacidade + a
            print("Volte sempre! Capacidade restante:",capacidade)
            a = int(input())