print("Digite o número correspondente ao menu: \n 1-> Soma \n 2-> Subtração \n 3-> Multiplicação \n 4-> Dividir ")
menu = int(input("Qual o valor do menu a selecionar: "))
valor_1= 0
valor_2= 0
resultado = 0
if menu == 1:
    print("Você escolheu a soma ")
    valor_1 = int(input("Digite seu primeiro numero: "))
    valor_2 = int(input("Digite seu segundo numero: "))
    resultado = valor_1 + valor_2
    print("O Resultado foi de {}".format(resultado))
elif menu == 2:
    print("Você escolheu a subtração ")
    valor_1 = int(input("Digite seu primeiro numero: "))
    valor_2 = int(input("Digite seu segundo numero: "))
    resultado = valor_1 - valor_2
    print("O Resultado foi de {}".format(resultado))
elif menu == 3:
    print("Você escolheu a multiplicação ")
    valor_1 = int(input("Digite seu primeiro numero: "))
    valor_2 = int(input("Digite seu segundo numero: "))
    resultado = valor_1 * valor_2
    print("O Resultado foi de {}".format(resultado))
elif menu == 4:
    print("Você escolheu a divisão ")
    valor_1 = int(input("Digite seu primeiro numero: "))
    valor_2 = int(input("Digite seu segundo numero: "))
    resultado = valor_1 / valor_2
    print("O Resultado foi de {}".format(resultado))
    
else: print("Resultado invalido")