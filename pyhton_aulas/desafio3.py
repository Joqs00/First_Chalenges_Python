#Etapas do desafio 3 de python


# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.


# 3 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário




# 1 - Criando uma lista de dicionários representando informações sobre pessoas
informacoes = [{'Nome': 'Jorge', 'Idade': '25', 'Cidade': 'SP'},
               {'Nome': 'Carla', 'Idade': '35', 'Cidade': 'RJ'},
               {'Nome': 'Abigail', 'Idade': '19', 'Cidade': 'Curitiba'}]

# 2 - Modificando o valor de um item, adicionando um novo campo e removendo um item do dicionário
for nome in informacoes:
    # Modificando o valor de 'Idade' para Jorge
    if nome['Nome'] == 'Jorge':
        nome['Idade'] = 26  # Atualizando a idade de Jorge
        print(f'Idade de {nome["Nome"]} alterada para: {nome["Idade"]}\n')
        
        # Adicionando a profissão 'Dev' para Jorge
        nome['Profissao'] = 'Dev'
        print(f'Foi adicionada a profissão {nome["Profissao"]} para {nome["Nome"]}\n')

# 2 - Removendo a chave 'Idade' de todos os dicionários na lista
for nome in informacoes:
    if 'Idade' in nome:
        del nome['Idade']  # Removendo a chave 'Idade'

# Exibindo as informações após as alterações
print(f'{informacoes}\n')

# 3 - Verificando se uma chave específica ('Cidade') e seu valor existem em algum dicionário
for nome in informacoes:
    # Verificando se a cidade é Curitiba
    if 'Curitiba' in nome['Cidade']:
        print(f'Quem mora em Curitiba é {nome["Nome"]}\n')  # Exibindo nome da pessoa que mora em Curitiba
