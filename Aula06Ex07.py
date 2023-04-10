nome = ['Sauron','Darth Vader','Crow','Joker', 'Hannibal']
idade = [30,40,27,35,32]
email = ['sauron@gmail.com','darthvader@gmail.com','crow@gmail.com','joker@gmail.com','hannibal@gmail.com']

print('\n')
print('#'*15)
print('Cadastro de Usuário')
print('#'*15)
print('\n')


for indice in range(0,4,1):
   
    print(f'Nome:{nome[indice]}\nIdade:{idade[indice]}\nEmail: {email[indice]}\n')