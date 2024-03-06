def calculo_milha(km):
    return km / 1.609344
kilo = float(input("Quantas Kilometros você quer converter para milhas: "))
print("Resultado de converção: {:0.2f}".format(calculo_milha(kilo)))
