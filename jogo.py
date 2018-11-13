import adivinhacao
import forca

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca\t (2) Advinhação")

jogo = int(input("Qual o jogo?\n"))

if (jogo == 1):
    print("Jogando Forca\n")
    forca.jogar()
elif (jogo == 2):
    print("Jogando Adivinhação\n")
    adivinhacao.jogar()


