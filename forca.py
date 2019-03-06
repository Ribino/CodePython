import random

def jogar():
    print("*********************************")
    print("***Bem vindo no jogo da Forca***!")
    print("*********************************")


    i = 0
    acabou = False
    vidas = 6
    palavra = randomstring()
    tamanho = len(palavra) - 1
    print("\nA palavra tem {} letras" .format(tamanho))
    forca = list(range(tamanho))

    for x in range(tamanho):
        forca[x] = " "

    while(True):
        chute_letra = (input("\nEscolha uma letra: ")).lower()
        nao_existe = True
        for x in palavra:
            if(chute_letra == x):
                if(chute_letra == forca[i]):
                    print("\nVocê ja escolheu essa letra, ela está na {}º posição".format(i + 1))    
                else:
                    print("\nEssa letra existe, esta na {}º posição".format(i + 1))
                    forca[i] = chute_letra
                    print(forca)
                nao_existe = False
            i += 1        
        if(" " not in forca):
            print("Voce descobriu que a palavra é " + palavra + "Parabêns!!")
            break
        if(nao_existe):
            print("\nNão existe essa letra, tente novamente\n")
            vidas -= 1
            print("Você tem {} vidas\n".format(vidas))
            acabou = desenha(vidas)
        if(acabou):
            print("A palavra era " + palavra + "Você nao descobriu, que pena =(")
            break
        i = 0
        

    novamente = int(input("Você quer jogar novamente?\n 1 - Sim\n 2 - Não\n"))        
    if(novamente == 1):
        jogar()
    elif(novamente == 2):
        print("Fim do Jogo")

def randomstring():
    Arquivo = open('palavras.txt')
    palavra = Arquivo.readlines()
    tamanho = len(palavra)
    aleatorio = random.randrange(0,tamanho)
    return palavra[aleatorio]

def desenha(vida):
    if(vida == 5):
        print("O")
    if(vida == 4):
        print("O\n|")
    if(vida == 3):
        print(" O\n/|")
    if(vida == 2):
        print(" O\n/|\\")
    if(vida == 1):
        print(" O\n/|\\\n/")
    if(vida == 0):
        print(" O\n/|\\\n/ \\ \nGame Over")
        return True

    
if(__name__ == "__main__"):
    jogar()