import random
print('Vamos jogar Pedra Papel Tesoura\nEscolha entre:\nPedra\nPapel\nTesoura ')
robo_vitoria = 0
barra_separar= "-" * 50
aste = "*" * 50
vitorias = 0
while True:
    options = ["pedra","papel","tesoura","x"]
    selecao = input("\nEscolha entre Pedra, Papel, Tesoura e [X] para fechar: ").strip().lower()
    if selecao not in options:
        print("\n{}   Pare de ser jumento e digita certo   {}\n\n\n".format(aste,aste))
        continue
    elif selecao == "x":
        break

    randomizador = random.randint(0,2)
    computador = options[randomizador]
    print("\nO computador escolheu {}".format(computador))

    if selecao == computador:
        print("Empate!")
    elif selecao == "pedra" and computador == "tesoura":
        vitorias +=1
        print("\nVocê venceu esta rodada ! Você esta com {} vitórias \n{}".format(vitorias,barra_separar))
        
    elif selecao == "tesoura" and computador == "papel":
        vitorias +=1
        print("\nVocê venceu esta rodada ! Você esta com {} vitórias \n{}".format(vitorias,barra_separar))
        
    elif selecao == "papel" and computador == "pedra":
        vitorias +=1
        print("\nVocê venceu esta rodada ! Você esta com {} vitórias \n{}".format(vitorias,barra_separar))
    else:
        robo_vitoria +=1
        print("\nVocê perdeu ! a maquinha esta com {} vitorias \n{}".format(robo_vitoria,barra_separar))
        
    if robo_vitoria == 3:
        print("\nVocê perdeu para uma maquina, que patético ")
        break
    elif vitorias == 3: 
        print("\nParabêns você venceu de uma simples maquina ")
        break
        

        

    









