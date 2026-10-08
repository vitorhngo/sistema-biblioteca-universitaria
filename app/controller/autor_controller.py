from model.autor_model import AutorModel
# from model.livro_model import LivroModel
from view.menu import Menu

class AutorController:

    def __init__(self):
        self.model = AutorModel()
        self.menu = Menu()

    def listar_controller(self): # Eu mudei o nome do método listar dessa classe AutorController, porque estava com o mesmo nome do método da classe Submenu, estava 'listar' nos dois
        try:
            autores = self.model.listar_autores() # Antes aqui estava usuarios, então eu troquei para autores, mas eu não sei se deveria ser somente 'autor'
            self.listar(autores) # Utilizando o listar da classe Submenu
        except Exception as e:
            self.menu.mensagem(f"Erro ao listar usuários: {e}") 
            # No código do controller original do professor ele usou a função 'mensagem' que vinha do programa usuario_view, 
            # mas aqui, mesmo eu importando tudo da classe submenu, o método 'mensagem' ficou sublinhado como se não tivesse definido.
            # Por isso eu optei por usar o print mesmo.

    def cadastrar_controller(self): # Não sei se eu deveria passar o cadastrar como parâmetro aqui
        try:
            nome, nacionalidade = self.cadastrar() # Acredito que pode dar erro aqui, porque a lógica da função 'solicitar_dados_usuario' é diferente do método 'cadastrar'
            if not nome or not nacionalidade:
                print("Nome e nacionalidade são obrigatórios!") # Pelo mesmo motivo no método 'listar_controller' eu vou trocar esse 'mensagem' e os próximos por print
                return
            self.model.inserir_autor(nome, nacionalidade)
            print("Autor cadastrado com sucesso!") # Antes de print era 'mensagem'
        except Exception as e:
            print(f"Erro ao cadastrar autor: {e}") # Antes de print era 'mensagem'

    def atualizar_controller(self):
        try:
            id_autor = self.cadastrar() # Eu não sei qual método usar das classes Menu ou Submenu, mas na dúvida eu coloquei 'cadastrar' também
            if id_autor is None:
                return
            nome, nacionalidade = self.cadastrar() # Antes estava 'solicitar_dados_usuario' e eu troquei por 'cadastrar'
            self.model.atualizar_autor(id_autor, nome, nacionalidade)
            print("✏️ Autor atualizado com sucesso!") # Antes de print era 'mensagem'
        except Exception as e:
            print(f"Erro ao atualizar autor: {e}") # Antes de print era 'mensagem'

    def excluir_controller(self):
        try:
            id_autor = self.cadastrar()
            if id_autor is None:
                return
            self.model.excluir_autor(id_autor)
            print("Autor excluído com sucesso!") # Antes de print era 'mensagem'
        except Exception as e:
            print(f"Erro ao excluir autor: {e}") # Antes de print era 'mensagem'