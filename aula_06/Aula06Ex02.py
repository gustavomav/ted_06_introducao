for i in range(1, 11):  # Range para os números de 1 a 10
    print(f'Tabuada do {i}:')
    for j in range(1, 11):  # Range para os múltiplos de cada número
        resultado = i * j
        print(f"{i} x {j} = {resultado}")