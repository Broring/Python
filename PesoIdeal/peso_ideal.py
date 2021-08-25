import os

print('***Peso Ideal***')

altura = float(input('Digite sua Altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / altura**2

print('Seu IMC é: %.f2' % imc)

if imc < 16:
    print('Baixo Peso Muito Grave')
elif imc < 17:
    print('Baixo Peso Grave')
elif imc < 18:
    print('Baixo Peso')
elif imc < 25:
    print('Peso Normal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 35:
    print('Obesidade Grau I')
elif imc < 40:
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III')

os.system('pause')
