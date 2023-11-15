#6.Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

PI = 3.14 #Neste caso, a variável PI tem função de constante

raio = float(input("Informe o raio do círculo: "))

area = PI * (raio ** 2)

print("A área do circulo é: {:.2f} cm2".format(area))

