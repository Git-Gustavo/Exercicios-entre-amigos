def celsius_fire(celsius):
    return celsius * 9/5 + 32
celsius = float(input("Digite de forma correta a temperatura para ser convertita usando Celsius: "))
fire = celsius_fire(celsius)
print(fire)