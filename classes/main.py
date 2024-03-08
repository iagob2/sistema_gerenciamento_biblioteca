from biblioteca import Biblioteca


sistema = Biblioteca()

op = 0

while(True):
    op = int(input( "Digite o opção que deseja:\n1. Adicionar livro\n2. Adicionar usuário \n3. Emprestar livro\n4. Listar livros disponíveis\n5. Listar livros emprestados\n6. Listar usuários\n7. Sair\n:"))

    if op == 1:
        tit = input("digite o titulo do livro:")
        ano = int(input("digite o ano de publicaca do livro:"))
        gen = input("digite o genero do livro:")
        
        sistema.adicionar_livro(tit,tit,ano,gen )
        
    elif op == 2:
        nomeUsua = input("digite o nome do usuario:")
        sistema.adicionar_usuario(nomeUsua)
        
    elif op == 3:
        livro= input("digite o titulo do livro:")

        sistema.emprestar_livro(livro)
        
    elif op == 4:
        sistema.livros_disponiveis()
        
    elif op == 5:
        sistema.livros_emprestados()
        
    elif op == 6:
        sistema.listar_usuario()
        
    elif op == 7:
        print("Obrigado por utilizar nosso sistema, criado por Iago Correia de Lima. Até logo!")
        break
    else:
        print("Opção inválida, digite novamente.")