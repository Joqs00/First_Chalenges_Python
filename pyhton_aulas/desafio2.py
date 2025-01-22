#etapas do desafio 2 de python
#1 - Crie uma lista para cada informação a seguir:
# lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.



# Lista de números de 1 a 10
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lista com quatro nomes
nomes = ['Jorge', 'Carla', 'Alberto']

# Lista com o ano de nascimento e o ano atual
anos = [1998, 2025]

# Variáveis para armazenar somas
soma = 0  # Soma dos números ímpares
soma2 = 0  # Soma de todos os números

# Ordenando a lista de números em ordem decrescente
ordem_decrescente = sorted(numeros, reverse=True)

# 2 - Loop para percorrer e imprimir todos os números da lista
for numero in numeros:
    print(numero)

# 3 - Loop para calcular a soma dos números ímpares de 1 a 10
for numero in numeros:
    if numero % 2 != 0:  # Verifica se o número é ímpar
        soma += numero  # Soma os números ímpares

print(f'A soma dos números ímpares da lista é {soma}')

# 4 - Loop para imprimir os números de 1 a 10 em ordem decrescente
for numero in ordem_decrescente:
    print(numero)

# 5 - Solicita um número ao usuário e imprime sua tabuada de 1 a 10
tabuada = int(input('Digite um número para ver a tabuada deste número: \n'))

for numero in numeros:
    print(f'{tabuada} x {numero} = {tabuada * numero}')

# 6 - Loop para calcular a soma de todos os números da lista, com try-except
for numero in numeros:
    try:
        soma2 += numero  # Adiciona o número à soma
    except:  # Bloco except não será necessário aqui, pois a lista é válida
        pass
print(soma2)

# 7 - Calcula a média dos números da lista
try:
    media = sum(numero for numero in numeros) / len(numeros)  # Soma os números e divide pelo total
    print(f'A média dos números da lista é {media}')
except ZeroDivisionError:  # Trata o caso de a lista estar vazia
    print("Não é possível calcular a média de uma lista vazia.")
