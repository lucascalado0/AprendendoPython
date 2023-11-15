#7.Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float (input("Informe qual o lado do quadrado: "))

area = lado ** 2 #fórmula da área de um quadrado

dobro = area * 2 #dobro da area do quadrado

print("O dobro da área do quadrado é: {:.2f} m2".format(dobro))

