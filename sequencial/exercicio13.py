"""
13.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
-Para homens: (72.7*h) - 58
-Para mulheres: (62.1*h) - 44.7
"""

h = float(input("Informe a sua altura: "))

sexo = str(input("Você é homem ou mulher?(Responda 'm' ou 'M' se for mulher e 'H' ou 'h' se for homem)"))

if sexo.upper() == 'M':
    peso_idealM = (62.1 * h) - 44.7
    print("Seu peso ideal é: {:.2f}kg".format(peso_idealM))

elif sexo.upper() == 'H':
    peso_idealH = (72.7 * h) - 58
    print("Seu peso ideal é: {:.2f}kg".format(peso_idealH))

else:
    print("Sexo não reconhecido.")