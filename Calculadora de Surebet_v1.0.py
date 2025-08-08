import time

print("Calculador de SureBet")
time.sleep(1)

def calcular_odd2():
    odd_casa1 = float(input("Digite a odd da primeira casa: "))
    odd_casa2 = float(input("Digite a odd da segunda casa: "))

    #calculo se existe surebet
    numero1 = 1 / odd_casa1
    numero2 = 1 / odd_casa2
    surebet = numero1 + numero2

    if surebet < 1:
        print("Aposte, tem surebet.")
        time.sleep(1)
        valor_disponivel = float(input("Quanto tem para apostar? "))

        #calculo de quanto deve apostar em cada casa
        apostar1 = (numero1 / surebet) * valor_disponivel
        apostar2 = (numero2 / surebet) * valor_disponivel

        #calculo lucro (o lucro é o mesmo, independente dos valores)
        lucro = apostar1 * odd_casa1 - valor_disponivel

        print(f"Aposte {apostar1:.2f} na primeira casa, e aposte {apostar2:.2f} na segunda casa.")
        print(f"Seu lucro {lucro:.2f}, independente do resultado.")

    else:
        print("Não aposte, não tem surebet")

def calcular_odd3():
    odd_casa1 = float(input("Digite a odd da primeira casa: "))
    odd_casa2 = float(input("Digite a odd da segunda casa: "))
    odd_casa3 = float(input("Digite a odd da terceira casa: "))
                      
    numero1 = 1 / odd_casa1
    numero2 = 1 / odd_casa2
    numero3 = 1 / odd_casa3
    surebet = numero1 + numero2 + numero3
    if surebet < 1:
        print("Aposte, tem surebet.")
        time.sleep(1)
        valor_disponivel = float(input("Quanto tem para apostar? "))

        #calculo de aposta
        apostar1 = (numero1 / surebet) * valor_disponivel
        apostar2 = (numero2 / surebet) * valor_disponivel
        apostar3 = (numero3 / surebet) * valor_disponivel

        #calculo lucro
        lucro = apostar1 * odd_casa1 - valor_disponivel

        print(f"Aposte {apostar1:.2f} na primeira casa, {apostar2:.2f} na segunda, e {apostar3:.2f} na terceira.")
        print(f"Seu lucro {lucro:.2f}, independente do resultado.")

    else:
        print("Não aposte, não tem surebet")

while True:
    print("Calcular com 2 odd (2)")
    print("Calcular com 3 odd (3)")

    escolha = int(input("Digite uma das opções: "))

    if escolha == 2:
        calcular_odd2()

    elif escolha == 3:
        calcular_odd3()

    else:
        print("Opção Errada!")
