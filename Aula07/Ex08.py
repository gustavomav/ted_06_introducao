palavra = str(input('Digite uma palavra '))

if palavra [::-1] == palavra:
    print(f'A palavra {palavra} é um Palíndromo')
else:
    print(f'A palavra {palavra} não é um palíndromo')