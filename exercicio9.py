#9.Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9)

fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))

C = 5 * ((fahrenheit - 32) / 9)

print("A temperatura correspondente em celcius é: {:.2f} ºC".format(C))