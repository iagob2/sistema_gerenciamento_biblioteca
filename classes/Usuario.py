class Usuario:
    # Atributo de classe para controlar o id
    proximo_id = 1

    def __init__(self, nome):
        self.id = Usuario.proximo_id
        self.nome = nome

        # Incrementa o próximo id para o próximo usuário
        Usuario.proximo_id += 1

    # Getter para o id
    def get_id(self):
        return self.id

    # Getter e setter para o nome
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome
        
#teste para ver se estão funcionando corretamente

# Exemplo de uso da classe Usuario
# usuario1 = Usuario("Alice")
# usuario2 = Usuario("Bob")

# Obtendo o id e o nome dos usuários usando getter
#print(f"Usuário 1 - ID: {usuario1.get_id()}, Nome: {usuario1.get_nome()}")
#print(f"Usuário 2 - ID: {usuario2.get_id()}, Nome: {usuario2.get_nome()}")

# Alterando o nome do segundo usuário usando setter
#usuario2.set_nome("Charlie")

# Obtendo os valores atualizados usando getter
#print(f"Usuário 2 - ID: {usuario2.get_id()}, Nome: {usuario2.get_nome()}")
