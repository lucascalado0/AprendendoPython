#8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input("Quanto você ganha por hora?"))

hora_trabalhada = int(input("Quantas horas você trabalhou neste mês? "))

salario = ganho_hora * hora_trabalhada

print("Seu salário neste mês foi: R$", salario) 
