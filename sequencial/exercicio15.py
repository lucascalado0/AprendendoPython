"""
5.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
#para este exercício aproveitei o código do exercício 8

ganho_hora = float(input("Quanto você ganha por hora?"))

hora_trabalhada = int(input("Quantas horas você trabalhou neste mês? "))

salario = ganho_hora * hora_trabalhada

IR = salario * 0.11

INSS = salario * 0.08

Sindicato = salario * 0.05

salarioLiquido = salario - IR - INSS - Sindicato

print("Seu salário bruto neste mês foi: R$", salario) 

print("-IR (11%): R${:.2f}".format(IR))

print("-INSS(8%): R${:.2f}".format(INSS))

print("-Sindicato (5%): R${:.2f}".format(Sindicato))

print("Salário liquido: R${:.2f}".format(salarioLiquido))

