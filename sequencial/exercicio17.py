"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
 Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
 que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
"""

#Para este exercicio, vou aproveitar parte do código da atividade 16

import math 

area = int(input("Informe a área a ser pintada em m2: "))

cobertura = area / 6
lata = 18
valor_lata = 80
galao = 3.6
valor_galao = 25


latas_necessarias = math.ceil(cobertura / lata) #math.ceil tem como função arredondar a quantidade de latas, levando em consideração que a loja só pode vender as latas de 18l fechadas

preco_total_lata = latas_necessarias * valor_lata

galoes_necessarios = math.ceil(cobertura / galao)

preco_total_galoes = galoes_necessarios * valor_galao


print("Quantidade de latas de tinta necessárias: ", latas_necessarias)
print("Preço total das latas: R$ {:.2f}\n".format(preco_total_lata))

print("Quantidade de galões de tinta necessários: ", galoes_necessarios)
print("Preço total dos galões: R$ {:.2f}". format(preco_total_galoes))