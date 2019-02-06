import random
def jogar():
    print("**********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("**********************************")

    numero_secreto = random.randrange(1,101)
    pontos = 1000
    print("Qual nível de dificuldade?","(1) Fácil (2) Médio (3) Dificil", sep = '\n')
    nivel = 4
    while(nivel > 3 or nivel < 1):
        nivel = int(input("Defina o nível: "))
        if(nivel == 1):
            total_de_tentativa = 20
        elif(nivel == 2):
            total_de_tentativa = 10
        elif(nivel == 3):
            total_de_tentativa = 5
        else:
            print("Defina um nível valído")

    for rodada in range(0,total_de_tentativa): 
        print("Tentativa {} de {}".format(rodada+1, total_de_tentativa))
        chute = int(input("Digite o seu numero entre 1 e 100: "))
        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        if (acertou):
            print("Você acertou","O numero secreto é {}".format(numero_secreto), sep = '\n')
            print("Você fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(pontos-chute) / 3 
            pontos = pontos - round(pontos_perdidos)
        rodada = rodada + 1
    print("Fim do jogo")
if(__name__ == "__main__"):
    jogar()