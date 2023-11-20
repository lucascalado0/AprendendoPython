"""
15.Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

def condicao_triangulo(a, b, c):
    if a + b > c  and a + c > b and c + b > a:
        if a == b == c:
            return "Triângulo Equilátero"

        elif a + b > c and a + c > b and c + b > a:
            if a == b or c == b or a == c:
                return "Trinângulo Isósceles"
    
        else:
            return "Triângulo Escaleno"
    else:
        return "Triangulo inválido"
    
a = float(input("Digite o valor do primeiro lado: "))

b = float(input("Digite o valor do segundo lado: "))

c = float(input("Digite o valor do terceiro lado: "))

triangulo = condicao_triangulo(a, b, c)

print("O triângulo é: ", triangulo)