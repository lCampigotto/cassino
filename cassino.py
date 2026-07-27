# cassino fornece: multiplicador/chance , cassino pede: Valor da aposta e numero (opcional)
#jogos: roleta, caca niquel, Sorte-Pura!

import random as rdm

def menuplay():


    print("---------- BEM VINDO AO CASSINO ----------")
    print(" ----- Escolha um de nossos jogos: -----   \n")
    print("1> Roleta\n2> Caça-Níquel\n3> Sorte-Pura!\n")

    global escolha
    global jogos
    escolha = int(input("Digite o número do jogo desejado : "))
    jogos = [1, 2, 3]

menuplay()

saldo = int(100000)

def init_game(par):
    if par == 1:
        playgame1()
    elif par == 2:
        playgame2()
    elif par == 3:
        playgame3()


def playgame1():
    global saldo
    print("\n----- BEM VINDO A ROLETA! -----\n\n1> Pretas = Impares (2x)\n2> Brancas = Pares (2x)\n3> Verde = Zero (14x)\n")
    print("Saldo : R$", saldo)
    print("")
    numero = input("Escolha uma cor para apostar : ")
    aposta = int(input("Escolha um valor para apostar : "))
    print("")
    confirma = input("Confirmar aposta? (s/n) : ")

    if saldo > aposta:
        if confirma.lower() == "s":
            saldo -= aposta
            girar_roleta(numero, aposta)
        else:
            print("Aposta cancelada. Reinicie o Sistema")
    else:
        print("Voce não possui saldo suficiente. Tente novamente")
        playgame1()


def girar_roleta(numero, aposta):
    global saldo
    resultado = rdm.randint(0, 62)
    print("A roleta parou no número", resultado)

    if numero.lower() in ["1", "pretas", "impares"] and resultado % 2 == 1:
        ganhos = aposta * 2
        print("Você ganhou R$", ganhos)
        saldo += ganhos
        print(saldo)
        continuar = input("Continuar? (s/n) : ")
        if continuar.lower() == "s":
            playgame1()
        else:
            voltar = print("Deseja voltar ao menu? (s/n) : ")
            if voltar.lower() == "s":
                menuplay()
            else:
                print("Programa encerrado : ")
    elif numero.lower() in ["2", "brancas", "pares"] and resultado != 0 and resultado % 2 == 0:
        ganhos = aposta * 2
        print("Você ganhou R$", ganhos)
        saldo += ganhos
        print(saldo)
        continuar = input("Continuar? (s/n) : ")
        if continuar.lower() == "s":
            playgame1()
        else:
            voltar = print("Deseja voltar ao menu? (s/n) : ")
            if voltar.lower() == "s":
                menuplay()
            else:
                print("Programa encerrado : ")
    elif numero.lower() in ["3", "verde", "zero"] and resultado == 0:
        ganhos = aposta * 14
        print("Você ganhou R$", ganhos)
        saldo += ganhos
        print(saldo)
        continuar = input("Continuar? (s/n) : ")
        if continuar.lower() == "s":
            playgame1()
        else:
            voltar = print("Deseja voltar ao menu? (s/n) : ")
            if voltar.lower() == "s":
                menuplay()
            else:
                print("Programa encerrado : ")
    else:
        print("Você perdeu R$", aposta)
        print(saldo)
        continuar = input("Continuar? (s/n) : ")
    if continuar.lower() == "s":
        playgame1()
    else:
        voltar = print("Deseja voltar ao menu? (s/n) : ")
        if voltar.lower() == "s":
            menuplay()
        else:
            print("Programa encerrado : ")
        

if escolha in jogos:
    init_game(escolha)


