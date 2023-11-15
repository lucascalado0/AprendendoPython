#3.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input("Informe o seu sexo: "))

if sexo.upper() == 'M':
    print("M - Masculino")

elif sexo.upper() == 'F':
    print("F - Feminino")

else:
    print("Sexo Inválido")