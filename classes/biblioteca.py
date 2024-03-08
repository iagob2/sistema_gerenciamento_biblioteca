from livros import Livro
from Usuario import Usuario  

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.listar_livros_disponiveis = []
        self.listar_livros_emprestados = []
    
    #livros
    
    #lista de livros disponiveis e emrestados 
    def atualizar_listas_livros(self):
        self.listar_livros_disponiveis = [livro for livro in self.livros if livro.get_disponibilidade()]
        self.listar_livros_emprestados = [livro for livro in self.livros if not livro.get_disponibilidade()]
    
    #metodo para adicionar livros 
    def adicionar_livro(self, livro,tit,ano,gen):
        print("Adicionando livro...")
        livro = Livro(tit,ano,gen)

        self.livros.append(livro)
        
        
    #metodo para mostrar as lista de livros 
    def listar_livros(self):
        for livro in self.livros:
            print("Título: {}, Ano: {}, Gênero: {}, Disponibilidade:{} ".format(livro.get_titulo(),livro.get_ano_publicacao(),livro.get_genero(),livro.get_disponibilidade()))
    
    #metodo para mostrar as lista de livros disponiveis
    def livros_disponiveis(self):
        self.atualizar_listas_livros()
        print("litras de livros disponiveis:")
        for livro in self.listar_livros_disponiveis:
            
            print("Título: {}, Ano: {}, Gênero: {}".format(
                livro.get_titulo(), livro.get_ano_publicacao(), livro.get_genero()
            ))
            
    def emprestar_livro(self,livro):
        # Lógica para emprestar livro
        self.atualizar_listas_livros()
        for livro in self.listar_livros_disponiveis:
            if livro.get_disponibilidade() == True and livro.get.titulo == livro:
                print("pode pegar o livro emprestando")
                livro.set_disponibilidade(False)
                print("Emprestando livro...")
            else:
                print("livro indisponivel")
            
            
        
    
    #metodo para mostrar as lista de livros emprestados   
    def livros_emprestados(self):
        self.atualizar_listas_livros()
        print("litras de livros emprestados:")
        for livro in self.listar_livros_emprestados:
            
            print("Título: {}, Ano: {}, Gênero: {}".format(
                livro.get_titulo(), livro.get_ano_publicacao(), livro.get_genero()
            ))
      
    #Usuarios 
    def adicionar_usuario(self,usuario):
        print("Adicionando usuário...")

        # Lógica para adicionar usuário
        usuario = Usuario(usuario)
        
        self.usuarios.append(usuario)
    
    def listar_usuario(self):
        for usuario in self.usuarios:
            print("Nome:{} - id: {}".format( usuario.get_nome(), usuario.get_id()))    

#teste para ver se estão funcionando corretamente

# Criando uma instância da classe Livro
#livro_exemplo = Livro("Aventuras em Python", 2020, "Aventura",True)
#livro_exemplo2 = Livro("Terro de java", 2024, "Terro",False)
#livro_exemplo3 = Livro("comedia em sql", 2010, "comedia",True)


# Criando uma instância da classe Biblioteca
#b = Biblioteca()

# Adicionando o livro à biblioteca
#b.adicionar_livro(livro_exemplo)
#b.adicionar_livro(livro_exemplo2)
#b.adicionar_livro(livro_exemplo3)

# Listando os livros na biblioteca
#b.listar_livros()

#teste de usuario 
#Usuario_exemplo1 = Usuario("iago")
#Usuario_exemplo2 = Usuario("thiago")
#Usuario_exemplo3 = Usuario("vitor")

#b.adicionar_usuario(Usuario_exemplo1)
#b.adicionar_usuario(Usuario_exemplo2)
#b.adicionar_usuario(Usuario_exemplo3)

#b.listar_usuario()

#b.livros_disponiveis()
#b.livros_emprestados()







