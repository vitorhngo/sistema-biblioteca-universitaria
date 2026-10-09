class AutorView:
    @staticmethod
    def menu():
        # Troquei aqui de 'MENU DE PRODUTOS' para 'GERENCIAR AUTOR'. Futuramente criar o 'GERENCIAR LIVRO'
        print("\n=====GERENCIAR AUTOR=====\n") 
        print("1 - Cadastrar autor")
        print("2 - Listar autores")
        print("3 - Atualizar autor")
        print("4 - Excluir autor")
        print("0 - Sair")
        
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("\nEntrada inválida. Digite um número.\n")
            return -1
        
    @staticmethod
    def listar(autor): # Troquei de 'produtos' para 'autor'
        if not autor:
            print("\nNenhum autor cadastrado.\n")
        else:
            print("\n=== Lista de Autores ===\n")
            for a in autor:
                print(f"ID: {a[0]} | Nome: {a[1]} | Nacionalidade: {a[2]}")

    
    @staticmethod
    def cadastrar():
        nome = input("Nome do Autor: ")
        try:
            nacionalidade = float(input("Nacionalidade: "))
            return nome, nacionalidade
        # Pensar direito sobre esse tratamento, porque ele era para o preço, 
        # não sei a gente vai precisar desse tratamento para nacionalidade
        except Exception as e:
            print("\nValor inválido para nacionalidade.\n")
            return None, None

    @staticmethod
    def atualizar():
        try:
            id_autor = int(input("ID do autor a atualizar: "))
            nome = input("Novo nome: ")
            nacionalidade = float(input("Nova nacionalidade: "))
            return id_autor, nome, nacionalidade
        except ValueError:
            print("\nEntrada inválida.\n")
            return None, None, None
        
    @staticmethod
    def excluir():
        try:
            id_autor = int(input("ID do autor a excluir: "))
            return id_autor
        except ValueError:
            print("\nEntrada inválida.\n")
            return None
    
    @staticmethod
    def mensagem(msg):
        print(msg)