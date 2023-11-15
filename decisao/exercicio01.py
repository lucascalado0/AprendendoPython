#1.Faça um Programa que peça dois números e imprima o maior deles.

num1 = input("Informe um número: ")

num2 = input("Informe outro número: ")

if num1 > num2:
    print("O número maior é: ", num1)

elif num2 > num1:
    print("O número maior é: ", num2)

else:
    print("Os números são iguais!")