"""
11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: 
-O produto do dobro do primeiro com metade do segundo .
-A soma do triplo do primeiro com o terceiro.
-O terceiro elevado ao cubo.
"""


num1 = int(input("Informe um número inteiro: "))

num2 = int(input("Agora informe outro número inteiro: "))

num3 = float(input("Agora informe um número REAL: "))

primeiro = (2 * num1) * (num2 / 2)

segundo = (3 * num1) + num3

terceiro = num3 ** 3

print("O produto do dobro do primeiro com metade do segundo é: ", primeiro)
print("A soma do triplo do primeiro com o terceiro é: ", segundo)
print("O terceiro elevado ao cubo é: ", terceiro)