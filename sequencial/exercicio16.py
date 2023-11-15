"""
16.Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
 Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
 Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""


import math 

area = int(input("Informe a área a ser pintada em m2: "))

cobertura = area / 3

lata_tinta = 18

valor_lata = 80

latas_necessarias = math.ceil(cobertura / lata_tinta) #math.ceil tem como função arredondar a quantidade de latas, levando em consideração que a loja só pode vender as latas de 18l fechadas

preco_total = latas_necessarias * valor_lata


print("Quantidade de latas de tinta necessárias: ", latas_necessarias)
print("Preço total: R$ {:.2f}".format(preco_total))