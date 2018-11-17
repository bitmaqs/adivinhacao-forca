def jogar():
    print("*****************************************")
    print("****** Bem-vindo ao jogo da Forca *******")
    print("*****************************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    #enforcou = False
    #acertou = False
    erros = 0

    print(letras_acertadas)

    while (True):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("OOPS! A palavra não possui a letra {}\n{} Tentativas Restantes\n".format(chute, 6-erros))

        if ("_" not in letras_acertadas):
            print("\n**** {} ****\n".format(palavra_secreta))
            print("Você ganhou!! :)\n")
            break
        elif (erros == 6):
            print("Você perdeu!! :(\n")
            break


        #enforcou = erros == 6
        #acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        letras_faltando = str(letras_acertadas.count("_"))
        print("Faltam {} letras".format(letras_faltando))

        print("\nJogando...")

    '''if(acertou):
        print("Você ganhou!! :)")
    else:
        print("Você perdeu!! :(")'''
    print("Fim do jogo")


if ( __name__ == '__main__' ):
    jogar()
