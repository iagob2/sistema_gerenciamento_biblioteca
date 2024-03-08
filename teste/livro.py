class Livro:
    def __init__(self, titulo, ano_publicacao, genero, disponibilidade):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.genero = genero
        self.disponibilidade = disponibilidade 
    
    def teste(self):
        print( self.ano_publicacao)
        print(self.genero)
        print(self.disponibilidade)
        print(self.titulo)
        
        
livro_exemplo = Livro("Aventuras em Python", 2020, "Aventura", True)
livro_exemplo.teste()


