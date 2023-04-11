nome = input('Diga seu nome')
idade = int(input('Diga sua idade'))

if idade < 18:
    print(f'{nome} você tem {idade} anos, você não pode dirigir')
else:
    print(f'{nome} você tem {idade} anos, você pode dirigir')

