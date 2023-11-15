"""10.Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

turno = str(input("Em que turno você estuda? Digite M-matutino, V-verspertino ou N-noturno)? "))

if turno.upper() == 'M':
    print("Bom dia!")

elif turno.upper() == 'V':
    print("Boa tarde!")

elif turno.upper() == 'Ng':
    print("Boa noite!")

else:
    print("Informe um período válido!")