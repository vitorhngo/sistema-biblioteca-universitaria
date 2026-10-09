from model.autor_model import AutorModel
from model.livro_model import LivroModel
from view.sistema_view import menu_principal, menu_gerenciar_autor, menu_gerenciar_livro

class AutorController:
    def __init__(self):
        self.model = AutorModel()
        self.model = LivroModel()
        self.view = menu_principal()
        self.view = menu_gerenciar_autor()
        self.view = menu_gerenciar_livro()

    def executar(self):
        while True:
            opcao = self.view.sistema_view.menu_principal()
            if opcao == 1:
                menu_gerenciar_autor()
                if opcao == 1:
                    # Antes tava 'produtos', agora está 'autor'
                    autor = self.model.listar()
                    self.view.listar(autor)
                
                elif opcao == 2:
                    nome, nacionalidade = self.view.cadastrar()
                    if nome and nacionalidade:
                        self.model.inserir(nome, nacionalidade)
                        self.view.menu.msg("\nAutor cadastrado com sucesso!\n")

                elif opcao == 3:
                    id_autor, nome, nacionalidade = self.view.atualizar()
                    if id_autor and nome and nacionalidade:
                        sucesso = self.model.atualizar(id_autor, nome, nacionalidade)
                        if sucesso:
                            self.view.menu.msg("\nAutor atualizado com sucesso!\n")
                        else:
                            self.view.menu.msg("\nFalha ao atualizar: ID não encontrado.\n")

                elif opcao == 4:
                    id_autor = self.view.excluir()
                    if id_autor:
                        sucesso = self.model.excluir(id_autor)
                        if sucesso:
                            self.view.menu.msg("\nAutor excluído com sucesso!\n")
                        else:
                            self.view.menu.msg("\nFalha ao excluir: ID não encontrado.\n")

                elif opcao == 0:
                    self.view.menu.msg("\nSaindo do sistema...\n")
                    break

                else:
                    self.view.menu.msg("\nOpção inválida!\n")

            if opcao == 2:
                menu_gerenciar_livro()
                if opcao == 1:
                    # Antes tava 'produtos', agora está 'autor'
                    livro = self.model.listar()
                    self.view.listar(livro)
                
                elif opcao == 2:
                    id_autor, titulo, data_publicacao = self.view.cadastrar()
                    if id_autor and titulo and data_publicacao: # Revisar isso
                        self.model.inserir(id_autor, titulo, data_publicacao)
                        self.view.menu.msg("\nLivro cadastrado com sucesso!\n")

                elif opcao == 3:
                    id_livro, id_autor, titulo, data_publicacao = self.view.atualizar()
                    if id_livro and id_autor and titulo and data_publicacao:
                        sucesso = self.model.atualizar(id_livro, id_autor, titulo, data_publicacao)
                        if sucesso:
                            self.view.menu.msg("\nLivro atualizado com sucesso!\n")
                        else:
                            self.view.menu.msg("\nFalha ao atualizar: ID não encontrado.\n")

                elif opcao == 4:
                    id_livro = self.view.excluir()
                    if id_livro:
                        sucesso = self.model.excluir(id_livro)
                        if sucesso:
                            self.view.menu.msg("\nLivro excluído com sucesso!\n")
                        else:
                            self.view.menu.msg("\nFalha ao excluir: ID não encontrado.\n")

                elif opcao == 0:
                    self.view.menu.msg("\nSaindo do sistema...\n")
                    break

                else:
                    self.view.menu.msg("\nOpção inválida!\n")