#Quarto desafio de POO em python

#Nesta aula foi ensinado sobre importar classes para outros arquivos através do from e import
#Foi pedido no desafio, porém como este arquivo faz parte de um conjunto de arquivos para portifólio, resolvi não implentar aqui
#Porém vou treinar em outros arquivos que talvez postar em um novo repositório

#Etapas do desafio:

# Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

# Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

# Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

# Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

class Livro:
    # Atributo de classe para armazenar todas as instâncias criadas
    livros = []

    def __init__(self, titulo, autor, ano_publicado):
        """
        Construtor que inicializa os atributos título, autor, ano de publicação e disponibilidade.
        Adiciona automaticamente cada instância à lista de livros.
        """
        self._titulo = titulo  # Título do livro
        self._autor = autor  # Autor do livro
        self._ano_publicado = ano_publicado  # Ano de publicação do livro
        self.disponivel = True  # Atributo que indica se o livro está disponível (True por padrão)
        Livro.livros.append(self)  # Adiciona a instância atual à lista de livros (automatização acertada)

    def __str__(self):
        """
        Método especial __str__ que retorna uma mensagem formatada com as informações do livro.
        """
        return f'\nTitulo: {self._titulo.ljust(20)} | Autor: {self._autor.ljust(30)} | Ano: {self._ano_publicado}\n'

    def emprestar(self):
        """
        Método de instância que define o atributo 'disponivel' como False.
        Simula o empréstimo do livro.
        """
        self.disponivel = False

    def status(self):
        """
        Método de instância que retorna uma string indicando se o livro está 'Disponível' ou 'Indisponível'.
        """
        return 'Disponível' if self.disponivel else 'Indisponível'

    @staticmethod
    def verificar_disponibilidade(ano):
        """
        Método estático que recebe um ano como parâmetro e retorna os títulos dos livros disponíveis publicados naquele ano.
        """
        # Filtra os livros disponíveis com base no ano fornecido
        livros_encontrados = [livro for livro in Livro.livros if livro._ano_publicado == ano and livro.disponivel]
        if livros_encontrados:  # Se houver livros disponíveis
            return f'Livros disponíveis em {ano}:\n' + '\n'.join([livro._titulo for livro in livros_encontrados])
        else:  # Caso contrário
            return f'Nenhum livro disponível em {ano}.'

# Criando instâncias da classe Livro
demon_slayer = Livro('DemonSlayer', 'Japonesa que esqueci o nome', 2020)  # Instância 1
frieren = Livro('Frieren', 'Alemão?', 2024)  # Instância 2

# Desafio 1: Imprimir as instâncias
print(demon_slayer, frieren)  # Acertou ao chamar __str__ implicitamente com print

# Desafio 2: Verificar o status de um livro e emprestá-lo
print(f'{demon_slayer._titulo} está {demon_slayer.status()}')  # Livro disponível
frieren.emprestar()  # Empréstimo de um livro
print(f'{frieren._titulo} está {frieren.status()}')  # Livro agora indisponível

# Desafio 3: Verificar a disponibilidade de livros por ano
print(Livro.verificar_disponibilidade(2020))  # Livros disponíveis em 2020


#As partes sobre from e import eram essas: 

#Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

# No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

# No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

# Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.



#Não é nada muito diferente do que eu fiz no final do código, só pedia para importar de outro arquivo, nada muito dificil.