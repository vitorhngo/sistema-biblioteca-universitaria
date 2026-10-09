from model.autor_model import AutorModel
from view.autor_view import AutorView

class AutorController:
    def __init__(self):
        self.model = AutorModel()
        self.view = AutorView()

    def executar(self):
        while True:
            opcao = self.view.menu()
            
            if opcao == 1:
                # Antes tava 'produtos', agora está 'autor'
                autor = self.model.listar()
                self.view.listar(autor)
            
            elif opcao == 2:
                nome, nacionalidade = self.view.cadastrar()
                if nome and nacionalidade:
                    self.model.inserir(nome, nacionalidade)
                    self.view.mensagem("\nAutor cadastrado com sucesso!\n")

            elif opcao == 3:
                id_autor, nome, nacionalidade = self.view.atualizar()
                if id_autor and nome and nacionalidade:
                    sucesso = self.model.atualizar(id_autor, nome, nacionalidade)
                    if sucesso:
                        self.view.mensagem("\nAutor atualizado com sucesso!\n")
                    else:
                        self.view.mensagem("\nFalha ao atualizar: ID não encontrado.\n")

            elif opcao == 4:
                id_autor = self.view.excluir()
                if id_autor:
                    sucesso = self.model.excluir(id_autor)
                    if sucesso:
                        self.view.mensagem("\nAutor excluído com sucesso!\n")
                    else:
                        self.view.mensagem("\nFalha ao excluir: ID não encontrado.\n")

            elif opcao == 0:
                self.view.mensagem("\nSaindo do sistema...\n")
                break

            else:
                self.view.mensagem("\nOpção inválida!\n")