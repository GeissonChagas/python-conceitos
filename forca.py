def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while (not enforcou and not acertou):

        chute = input ("Qual a letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):

                print ("Encontrei a letra {} na posição {}".format (letra, index + 1))
                index = index + 1



    Print ("Jogando...")



    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
