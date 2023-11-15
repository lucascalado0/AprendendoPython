#7.Faça um Programa que leia três números e mostre o maior e o menor deles.

#neste exercicio utilizei as funções de listas min e max


num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

print("O maior número é:", (max(num1, num2, num3)))

print("O menor número é: ", (min(num1, num2, num3)))