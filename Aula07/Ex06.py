salario = float(input('Digite seu salário '))

if salario >= 1500:
    salario = salario + (salario / 10)
    print(f'O seu salário é {salario}')
else:
    salario = salario + (salario / 15)
    print(f'O seu salário é {salario}')


