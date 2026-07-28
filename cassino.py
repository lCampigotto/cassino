# cassino fornece: multiplicador/chance , cassino pede: Valor da aposta e numero (opcional)
#jogos: roleta, caca niquel, Penalti!

import random as rdm

saldo = 100000
multiplica = 0.0

def penalti(aposta, canto):
    global saldo, multiplica
    goleiro = rdm.randint(1, 6)
    try:
        canto = int(canto)
    except ValueError:
        canto = 0

    if goleiro == canto:
        print("\nDEFESAÇA! O GOLEIRO PULA E DEFENDE O PÊNALTI!")
        print("Você perdeu!")
        multiplica = 0.0
        print(f"Saldo atual: R$ {saldo:.2f}")
        return False
    else:
        print("\nGOOOOOL! A BOLA VAI NO FUNDO DA REDE!")
        print("Você Venceu!")
        multiplica += 0.1
        recompensa_penal = (aposta * multiplica) + aposta
        saldo += recompensa_penal
        print(f"Saldo atual: R$ {saldo:.2f}")
        return True

def playgame3():
    global saldo, multiplica
    print("\n----- BEM-VINDO AO PÊNALTI! -----")
    print("~ Escolha um canto para chutar (1 a 6)!")
    print("~ A cada chute certo seguido, a recompensa aumenta em +0.1x")
    print("~ Aposta Mínima: R$ 500 | Máxima: R$ 1.000")
    print(f"Saldo: R$ {saldo:.2f}\n")
    
    try:
        aposta = int(input("Digite o Valor da aposta: "))
    except ValueError:
        print("Valor inválido!")
        return

    if aposta < 500 or aposta > 1000:
        print("Valor de aposta fora do limite permitido (R$ 500 a R$ 1.000).")
        return

    if saldo < aposta:
        print("Saldo Insuficiente.")
        return

    multiplica = 0.0
    
    while True:
        print("\n ____________________\n |  1      2      3  |\n |  4      5      6  |\n")
        canto = input("Escolha um canto para chutar: ")
        confirma = input("Confirmar Chute? (s/n): ")
        
        if confirma.lower() == "s":
            saldo -= aposta
            acertou = penalti(aposta, canto)
            
            if not acertou:
                break
                
            continuar = input("\nDeseja chutar novamente mantendo a sequência? (s/n): ")
            if continuar.lower() != "s":
                break
        else:
            print("Aposta cancelada.")
            break

def cacar_niquel():
    global saldo
    print("\n----- BEM-VINDO AO CAÇA-NÍQUEL! -----")
    print("~ Números de 1 a 9")
    print("~ Trinca = (Aposta x 2 x número da trinca)")
    print("~ Custo por jogada: R$ 500")
    
    while True:
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        if saldo < 500:
            print("Você não possui saldo suficiente para jogar (Mínimo R$ 500).")
            break

        confirma = input("Puxar a Alavanca por R$ 500? (s/n): ")
        if confirma.lower() == "s":
            saldo -= 500
            n1 = rdm.randint(1, 9)
            n2 = rdm.randint(1, 9)
            n3 = rdm.randint(1, 9)
            
            print(f"\nResultados: | {n1} | {n2} | {n3} |")
            
            if n1 == n2 == n3:
                ganhos = 500 * 2 * n1
                print(f"🎉 TRINCA! Você ganhou R$ {ganhos:.2f}!")
                saldo += ganhos
            else:
                print("Sem trinca desta vez!")
                
            continuar = input("\nJogar novamente no Caça-Níquel? (s/n): ")
            if continuar.lower() != "s":
                break
        else:
            break

def girar_roleta(opcao, aposta):
    global saldo
    resultado = rdm.randint(0, 62)
    print(f"\nA roleta girou... E parou no número {resultado}!")

    venceu = False
    
    if opcao in ["1", "pretas", "impares"] and resultado % 2 != 0:
        venceu = True
        multiplicador = 2
    elif opcao in ["2", "brancas", "pares"] and resultado != 0 and resultado % 2 == 0:
        venceu = True
        multiplicador = 2
    elif opcao in ["3", "verde", "zero"] and resultado == 0:
        venceu = True
        multiplicador = 14

    if venceu:
        ganhos = aposta * multiplicador
        print(f"🎉 PARABÉNS! Você ganhou R$ {ganhos:.2f}!")
        saldo += ganhos
    else:
        print(f"Que pena, você perdeu R$ {aposta:.2f}.")

def playgame1():
    global saldo
    print("\n----- BEM-VINDO À ROLETA! -----")
    print("1> Pretas = Ímpares (2x)")
    print("2> Brancas = Pares (2x)")
    print("3> Verde = Zero (14x)")
    
    while True:
        print(f"\nSaldo: R$ {saldo:.2f}")
        try:
            aposta = int(input("Escolha o valor da aposta: "))
        except ValueError:
            print("Valor inválido!")
            continue

        if aposta > saldo:
            print("Saldo insuficiente para essa aposta!")
            continue
            
        numero = input("Escolha a opção (1, 2 ou 3): ").lower()
        confirma = input("Confirmar aposta? (s/n): ")

        if confirma.lower() == "s":
            saldo -= aposta
            girar_roleta(numero, aposta)
            
            continuar = input("\nDeseja fazer outra aposta na Roleta? (s/n): ")
            if continuar.lower() != "s":
                break
        else:
            print("Aposta cancelada.")
            break

def menuplay():
    while True:
        print("\n========== BEM VINDO AO CASSINO ==========")
        print(f"Seu Saldo Atual: R$ {saldo:.2f}")
        print("1> Roleta\n2> Caça-Níquel\n3> Pênalti\n4> Sair")
        
        escolha = input("Digite o número do jogo desejado: ")
        
        if escolha == "1":
            playgame1()
        elif escolha == "2":
            cacar_niquel()
        elif escolha == "3":
            playgame3()
        elif escolha == "4":
            print("\nObrigado por jogar no Cassino! Até mais.")
            break
        else:
            print("Opção inválida! Tente novamente.")

menuplay()