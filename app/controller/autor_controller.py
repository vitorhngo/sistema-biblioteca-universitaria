from model.autor_model import AutorModel
from model.livro_model import LivroModel
from view.sistema_view import menu_principal, menu_gerenciar_autor, menu_gerenciar_livro

class AutorController:
    def __init__(self):
        self.autor_model = AutorModel()
        self.livro_model = LivroModel()
        
    def executar(self):
        while True:
            menu_principal.exibir_cabecalho()
            menu_principal.exibir_opcoes()
            try:
                opcao = menu_principal.capturar_digito(1, 3)

                try:
                    if opcao == 1:
                        while True:
                            menu_gerenciar_autor.exibir_cabecalho()
                            menu_gerenciar_autor.exibir_opcoes()
                            opcao2 = menu_gerenciar_autor.capturar_digito(1, 5)

                            if opcao2 == 1:
                                #Cadastrar autor
                                resposta = menu_gerenciar_autor.cadastrar({
                                    'nome': str,
                                    'nacionalidade': str
                                })
                                if resposta is None:
                                    continue
                                self.autor_model.inserir(resposta)
                            if opcao2 == 2:
                                autores = self.autor_model.listar()
                                menu_gerenciar_autor.listar(
                                    ["id", "nome", "nacionalidade"],
                                    autores
                                )
                            if opcao2 == 3:
                                resposta = menu_gerenciar_autor.atualizar({
                                    'id_autor': int,
                                    'nome': str,
                                    'nacionalidade': str
                                })
                                if resposta is None: 
                                    continue
                                self.autor_model.atualizar(resposta)

                            if opcao2 == 4:
                                resposta = menu_gerenciar_autor.excluir()
                                self.autor_model.excluir(resposta)

                            if opcao2 == 5:
                                break

                except ValueError as e:
                    print("ERRO:", e)

                try:
                    if opcao == 2:
                        while True:
                            menu_gerenciar_livro.exibir_cabecalho()
                            menu_gerenciar_livro.exibir_opcoes()
                            opcao3 = menu_gerenciar_livro.capturar_digito(1, 5)

                            if opcao3 == 1:
                                resposta = menu_gerenciar_livro.cadastrar({
                                    'id_autor': int,
                                    'titulo': str,
                                    'data_publicacao': int
                                })
                                if resposta is None:
                                    continue
                                self.livro_model.inserir(resposta)
                            if opcao3 == 2:
                                livros = self.livro_model.listar()
                                menu_gerenciar_livro.listar(
                                    ["id_livro", "id_autor", "titulo", "data_publicacao"],
                                    livros
                                )
                            if opcao3 == 3:
                                resposta = menu_gerenciar_livro.atualizar({
                                    'id_livro': int,
                                    'id_autor': int,
                                    'titulo': str,
                                    'data_publicacao': int
                                })
                                if resposta is None:
                                    continue
                                self.livro_model.atualizar(resposta)

                            if opcao3 == 4:
                                resposta = menu_gerenciar_livro.excluir()
                                self.livro_model.excluir(resposta)

                            if opcao3 == 5:
                                break

                except ValueError as e:
                    print("ERRO:", e)

                if opcao == 3:
                    menu_principal.mensagem("Saindo do programa...")
                    break

            except ValueError as e:
                print("ERRO:", e)
            

    