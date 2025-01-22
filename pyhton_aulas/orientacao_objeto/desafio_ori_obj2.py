#Segundo desafio de "POO" em Python

#Nesta aula foi revisado algumas coisas sobre classe da aula anterior
#E também foi explicado melhor sobre os métodos especiais das classes
#Também foi mostrado que é possivel criar os próprios métodos, porém nos desafios não foi pedido algo do tipo
#(A ultima parte do desafio foi uma brincadeira pra uns amigos)

#E dessa vez fiz completamente sozinho, apenas com os ensinamentos da aula e dos conhecimentos passado pelo GPT anteriormente

# Desafio 1: Implementar uma classe Carro com atributos básicos e criar uma instância.
class Carro():
    # O método __init__ é o construtor que inicializa os atributos modelo, cor e ano.
    def __init__(self, modelo='', cor='', ano=''):
        self.modelo = modelo  # Armazena o modelo do carro.
        self.cor = cor  # Armazena a cor do carro.
        self.ano = ano  # Armazena o ano de fabricação do carro.

# Desafio 2: Criar a classe Restaurante com os atributos nome, categoria, ativo e mais dois atributos extras.
class Restaurantes():
    # O método __init__ inicializa os atributos nome, categoria, ativo, delivery e desconto.
    def __init__(self, nome='', categoria='', ativo=False, delivery='', desconto='0'):
        self.nome = nome  # Nome do restaurante.
        self.categoria = categoria  # Categoria do restaurante, como "Pizza" ou "Fast Food".
        self.ativo = ativo  # Define se o restaurante está ativo ou inativo (False por padrão).
        self.delivery = delivery  # Indica se o restaurante oferece delivery.
        self.desconto = desconto  # Desconto oferecido pelo restaurante, representado como uma string.

    # Desafio 4: Adicionar um método especial __str__ para exibir nome e categoria ao imprimir uma instância.
    def __str__(self):
        return (f'{self.nome} | {self.categoria}')  # Retorna uma string formatada com nome e categoria.

# Criação de uma instância de Restaurante utilizando o construtor.
sonimod = Restaurantes('Sonimod Pizzas', 'Pizza')  # Instância criada com nome e categoria.
print(sonimod)  # Exibe o nome e a categoria usando o método __str__.

# Desafio 5: Criar a classe Cliente com 4 atributos e instanciar 3 objetos.
class Cliente():
    # O método __init__ inicializa os atributos nome, idade, adicionado e ban.
    def __init__(self, nome='', idade='', adicionado=False, ban=''):
        self.nome = nome  # Nome do cliente.
        self.idade = idade  # Idade do cliente.
        self.adicionado = adicionado  # Indica se o cliente foi adicionado ao sistema.
        self.ban = ban  # Indica se o cliente merece um "ban" (banimento).

    # Método especial __str__ para exibir os dados do cliente de forma formatada.
    def __str__(self):
        return (f'\n Nome: {self.nome}\n Idade: {self.idade}\n Merece Ban?: {self.ban}\n')

# Criação de instâncias da classe Cliente com diferentes atributos.
Shuu = Cliente('Shuu', '25?', True, 'Jamais')  # Instância do cliente Shuu.
Karla = Cliente('Karla', '27?', True, 'Nunca')  # Instância do cliente Karla.
Kura = Cliente('Kura', '23?', True, 'Também nunca')  # Instância do cliente Kura.

# Impressão dos dados de cada cliente utilizando o método __str__.
print(Shuu, Karla, Kura)
