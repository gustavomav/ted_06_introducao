num = int(input('Digite um número '))

print(f'Tabuada do {num}')
for j in range(1,11):
        resultado = num * j
        print(f'{num} x {j} = {resultado}')