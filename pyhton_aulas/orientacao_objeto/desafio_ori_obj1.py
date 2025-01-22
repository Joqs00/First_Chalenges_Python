#Desafio 1 de Programação Orientada a Objeto(POO) em Python

#A aula foi sobre classes, atributos e instancias das classes e algumas funções especiais de classes

#as etapas eram:

#Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos definindo cada atributo:
# nome
# artista
# duracao

#Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
# Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
# Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
# Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
# Altere o valor do atributo nome para 'Bistrô'.
# Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
# Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
# Mude o estado da instância restaurante_pizza para ativo.
# Imprima no console o nome e a categoria da instância restaurante_praca.

#Novamente tive ajuda do chat GPT com algumas coisas, pois acabei esquecendo de algumas coisas da aula
#Mas com a ajuda do GPT acabei intendendo melhor algumas coisas


# Definindo a classe 'Musica' com os atributos solicitados.
class Musica():
    # Atributos da classe Musica: nome, artista, duracao.
    nome = ''
    artista = ''
    duracao = ''

# Criando 3 objetos da classe Musica, com valores definidos para cada atributo.
musica1 = Musica()
musica1.nome = "Shape of You"  # Definindo o nome da música.
musica1.artista = "Ed Sheeran"  # Definindo o artista da música.
musica1.duracao = "4:23"  # Definindo a duração da música.

musica2 = Musica()
musica2.nome = "Blinding Lights"  # Definindo o nome da música.
musica2.artista = "The Weeknd"  # Definindo o artista da música.
musica2.duracao = "3:20"  # Definindo a duração da música.

musica3 = Musica()
musica3.nome = "Levitating"  # Definindo o nome da música.
musica3.artista = "Dua Lipa"  # Definindo o artista da música.
musica3.duracao = "3:23"  # Definindo a duração da música.

# Definindo a classe 'Restaurante'.
class Restaurante():
    # Inicializando os atributos nome, categoria e ativo com valores padrão.
    def __init__(self, nome='', categoria='', ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

    # Método para exibir o status do restaurante (Ativo ou Inativo).
    def exibir_status(self):
        return "Ativo" if self.ativo else 'Inativo'

    # Método __str__ para retornar uma representação formatada do restaurante.
    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"Categoria: {self.categoria}\n"
                f"Status: {self.exibir_status()}")

    # Método para alterar o nome do restaurante.
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

# Criando a instância restaurante_praca da classe Restaurante com nome 'Praça', categoria 'Italiana' e ativo como True.
restaurante_praca = Restaurante(nome='Praça', categoria='Italiana', ativo=True)

# Imprimindo os detalhes do restaurante_praca usando o método __str__.
print(restaurante_praca)

# Acessando o valor do atributo categoria de restaurante_praca.
categoria = restaurante_praca.categoria

# Acessando o valor do atributo nome de restaurante_praca.
# Isso é útil caso você precise fazer alguma manipulação ou exibição do nome em outro ponto.
print(f'O nome do restaurante é: {restaurante_praca.nome}')

# Verificando o status do restaurante_praca com base no atributo 'ativo'.
print(f'O restaurante {restaurante_praca.nome} está {restaurante_praca.exibir_status()}.')

# Acessando diretamente o atributo de classe 'categoria' para armazená-lo em uma variável.
categoria = Restaurante.categoria  # Acessando a categoria diretamente da classe.

# Alterando o nome do restaurante_praca para 'Bistrô' usando o método alterar_nome.
restaurante_praca.alterar_nome('Bistrô')

# Imprimindo o novo nome do restaurante após a alteração.
print(f'Nome alterado: {restaurante_praca.nome}')

# Criando uma nova instância de restaurante com nome 'Pizza Place' e categoria 'Fast Food'.
pizza_place = Restaurante(nome='Pizza Place', categoria='Fast Food')

# Verificando se a categoria da instância pizza_place é 'Fast Food'.
print(f'A categoria do restaurante {pizza_place.nome} é {pizza_place.categoria}.')

# Alterando o estado da instância pizza_place para ativo.
pizza_place.ativo = True

# Imprimindo o status de pizza_place após alterá-lo para ativo.
print(f'O restaurante {pizza_place.nome} está {pizza_place.exibir_status()}.')

# Imprimindo nome e categoria do restaurante_praca após as modificações.
print(f'\nO restaurante {restaurante_praca.nome} tem a categoria {restaurante_praca.categoria}.')
