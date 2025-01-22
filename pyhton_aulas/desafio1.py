#Etapas do primeiro desafio de python
# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.
# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.


#Cometi alguns erro, porém foram corrigidos pelo gpt, mas em resumo, foram erros de digitação e algumas melhorias




# Solicita ao usuário a idade
idade = int(input('Insira idade:\n'))

# Função para verificar se o nome começa com letra maiúscula
def name_checking(name):  # Corrigido para o nome correto
    if name[0].isupper():  # Verifica se a primeira letra é maiúscula
        print(f'O nome {name} é válido\n')
    else:
        print(f'O nome {name} é inválido, insira a primeira letra como maiúscula\n')

# Função para verificar a validade da senha (mínimo de 4 caracteres)
def pass_check(passw):
    if len(passw) >= 4:  # Verifica se a senha tem pelo menos 4 caracteres
        print('A senha é válida\n')
    else:
        print('A senha deve conter pelo menos 4 caracteres\n')

# Função para determinar se o número é par ou ímpar
def impar_par(num):
    if num % 2 == 0:
        print(f'O número {num} é par\n')  # Corrigido para usar "num" ao invés de "idade"
    else:
        print(f'O número {num} é ímpar\n')  # Corrigido para usar "num" ao invés de "idade"

# Função para classificar a idade
def idade_class(num):
    if num <= 0:  # Adicionada verificação para idades negativas ou zero
        print('Idade inválida, deve ser um número positivo.\n')
    elif num <= 12:  # Menores ou iguais a 12 anos são classificados como crianças
        print(f'{num} é criança\n')
    elif num <= 18:  # Idade entre 13 e 18 é classificada como adolescente
        print(f'{num} é adolescente\n')
    else:
        print(f'{num} é adulto\n')

# Chamando a função para verificar se o número é par ou ímpar
impar_par(idade)

# Chamando a função para classificar a idade
idade_class(idade)

# Solicita ao usuário o nome e verifica se começa com letra maiúscula
nome = input('Insira o nome:\n')
name_checking(nome)  # Corrigido para "name_checking"

# Solicita a senha e verifica se é válida
senha = input('Insira uma senha:\n')
pass_check(senha)
