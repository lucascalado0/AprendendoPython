#8.Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Informe o preço do produto: "))

produto2 = float(input("Informe o preço do produto: "))

produto3 = float(input("Informe o preço do produto: "))

if produto1 < produto2 and produto1 < produto3:
    produto_mais_barato = 1

elif produto2 < produto1 and produto2 < produto3:
    produto_mais_barato = 2

else:
    produto_mais_barato = 3

print("Você deve comprar o produto ", produto_mais_barato)