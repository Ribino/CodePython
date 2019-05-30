# CÓDIGO CRIADO POR LUCAS DA SILVA RIBINO 
# GITHUB ---> http://github.com/Ribino
import os
class sorteio(object):
    def sorteionome():
        import random
        qtde =  int(input("Quantas pessoas irão participar do sorteio?\n"))
        if(qtde < 2):
            print("Não há quantidade suficiente para o sorteio\n")
            return 0
        lista = []

        print("Insira o nome dos participantes\n")
        for i in range(qtde):
            lista.append(input("Participante {}: ".format(i+1)))

        random = random.randrange(qtde)

        print("\nSorteado/a foi o/a \"{}\"\n" .format(lista[random]))

print("***Código para sortear nomes***\n")
sorteio.sorteionome()
while(int(input("Sortear Novamente?\n 1 - SIM 0 - NÃO\n"))):   
    os.system('cls' if os.name == 'nt' else 'clear')
    sorteio.sorteionome()
    