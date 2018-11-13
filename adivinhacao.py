import random

def jogar():
    print("*************************************")
    print("* Bem vindo ao jogo de adivinhação! * ")
    print("*************************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual a dificuldade?")
    print("(1) Fácil \t (2) Médio \t (3) Difícil")
    dificuldade = int(input("Escolha o nível de dificuldade: "))
    if (dificuldade == 1):
        total_de_tentativas = 20
    elif (dificuldade == 2):
        total_de_tentativas = 10
    elif (dificuldade == 3):
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número de 1 a 100: "))
        print("Você digitou: ", chute)

        if (chute < 1 or chute > 100):
            print("Número Inválido! Você deve digitar um número de 1 a 100: ")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!\n".format(pontos))
            break
        else:
            if (maior):
                print("Resposta Errada! :(")
                print("O número que você chutou é MAIOR que o número secreto.\n")
            elif (menor):
                print("Resposta Errada! :(")
                print("O número que você chutou é MENOR que o número secreto.\n")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos



    if (not acertou):
        print("O Número Secreto era: {} \n".format(numero_secreto))

    print("Fim do Jogo.")

if  (__name__ == "__main__"):
    jogar()