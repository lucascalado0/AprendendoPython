#9.Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input("Informe o primeiro número: "))

num2 = float(input("Informe o segundo número: "))

num3 = float(input("Informe o terceiro número: "))

numeros = [num1, num2, num3]

numeros.sort(reverse = True) #a função .sort(reverse = True) faz com que os itens sejam impressos em ordem decrescente

print("A ordem decrescente dos números é: ", numeros)