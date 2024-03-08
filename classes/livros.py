class Livro:
    disponibilidade = True
    def __init__(self, titulo, ano_publicacao, genero):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.genero = genero
        self.disponibilidade = Livro.disponibilidade

    # Getter e setter para o título
    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    # Getter e setter para o ano de publicação
    def get_ano_publicacao(self):
        return self.ano_publicacao

    def set_ano_publicacao(self, ano_publicacao):
        self.ano_publicacao = ano_publicacao

    # Getter e setter para o gênero
    def get_genero(self):
        return self.genero

    def set_genero(self, genero):
        self.genero = genero

    # Getter e setter para a disponibilidade
    def get_disponibilidade(self):
        return self.disponibilidade

    def set_disponibilidade(self, disponibilidade):
        self.disponibilidade = disponibilidade

#teste para ver se estão funcionando corretamente

# Exemplo de uso da classe Livro
#livro_exemplo = Livro("Aventuras em Python", 2020, "Aventura", True)

# Obtendo e definindo o título usando getter e setter
#print(livro_exemplo.get_titulo())  # Saída: Aventuras em Python
#livro_exemplo.set_titulo("Novas Aventuras em Python")

# Obtendo e definindo o ano de publicação usando getter e setter
#print(livro_exemplo.get_ano_publicacao())  # Saída: 2020
#livro_exemplo.set_ano_publicacao(2022)

# Obtendo e definindo o gênero usando getter e setter
#print(livro_exemplo.get_genero())  # Saída: Aventura
#livro_exemplo.set_genero("Fantasia")

# Obtendo e definindo a disponibilidade usando getter e setter
#print(livro_exemplo.get_disponibilidade())  # Saída: True
#livro_exemplo.set_disponibilidade(False)
