"""
11.As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
-salários até R$ 280,00 (incluindo) : aumento de 20%
-salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
-salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
-salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
-o salário antes do reajuste;
-o percentual de aumento aplicado;
-o valor do aumento;
-o novo salário, após o aumento.
"""

salario = float(input("Informe o seu salário: "))

aumento20 = salario * (20 / 100)

aumento15 = salario * (15 / 100)

aumento10 = salario * (10 / 100)

aumento5 = salario * (5 / 100)

if salario == 280:
    print("Salário antes do reajuste: R$", salario)
    print("Percentual de aumento aplicado : 20%")
    print("Valor de aumento: R${:.2f}".formatformat(aumento20))
    print("Seu novo salario é: R$", salario + aumento20)

elif salario > 280 and salario <=700:
    print("Salário antes do reajuste: R$", salario)
    print("Percentual de aumento aplicado: 15%")
    print("Valor de aumento: R${:.2f}".format(aumento15))
    print("Seu novo salário é: R$", salario + aumento15 )

elif salario > 700 and salario <=1500:
    print("Salário antes do reajuste: R$", salario)
    print("Percentual de aumento: 10%")
    print("Valor de aumento: R${:.2f}".format(aumento10))
    print("Seu novo salário é: R$", salario + aumento10)

else:
    print("Salário antes do reajuste: R$", salario)
    print("Percentual de aumento aplicado: 5%")
    print("Valor de aumento: R${:.2f}".format(aumento5))
    print("Seu novo salário é: R$", salario + aumento5)


