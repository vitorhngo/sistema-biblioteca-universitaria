from model.autor_model import AutorModel
from model.livro_model import LivroModel
from view.sistema_view import menu_principal, menu_gerenciar_autor, menu_gerenciar_livro

class AutorController:
    def __init__(self):
        self.autor_model = AutorModel()
        self.livro_model = LivroModel()
        self.menu_principal_opcoes = {
            1: self.tela_menu_gerenciar_autor,
            2: self.tela_menu_gerenciar_livro
        }
        self.menu_gerenciar_autor_opcoes = {
            1: self.tela_cadastrar_autor,
            2: self.tela_listar_autor,
            3: self.tela_atualizar_autor,
            4: self.tela_excluir_autor
        }
        self.menu_gerenciar_livro_opcoes = {
            1: self.tela_cadastrar_livro,
            2: self.tela_listar_livro,
            3: self.tela_atualizar_livro,
            4: self.tela_excluir_livro
        }
        
    def executar(self):
        self.tela_menu_principal()


    # ── Menu principal ────────────────────────────────────────────────
    def tela_menu_principal(self):
        while True:
            menu_principal.exibir_cabecalho()
            menu_principal.exibir_opcoes()
            try:
                opcao = menu_principal.capturar_digito(1, 3)
                if opcao == 3:
                    menu_principal.mensagem("Saindo do programa...")
                    break
                self.menu_principal_opcoes[opcao]()
            except ValueError as e:
                menu_gerenciar_autor.mensagem(f"ERRO: {e}")



    # ── Autor ────────────────────────────────────────────────
    def tela_menu_gerenciar_autor(self):
        while True:
            menu_gerenciar_autor.exibir_cabecalho()
            menu_gerenciar_autor.exibir_opcoes()
            try:
                opcao = menu_gerenciar_autor.capturar_digito(1, 5)
                if opcao == 5:
                    break
                self.menu_gerenciar_autor_opcoes[opcao]()
            except ValueError as e:
                menu_gerenciar_autor.mensagem(f"ERRO: {e}")

    def tela_cadastrar_autor(self):
        resposta = menu_gerenciar_autor.formulario({
            'nome': str,
            'nacionalidade': str
        })
        if resposta is None:
            return
        resultado = self.autor_model.inserir(resposta)
        if resultado['sucesso']:
            menu_gerenciar_autor.mensagem("Autor cadastrado com sucesso!")
        else:
            menu_gerenciar_autor.mensagem(f"ERRO: {resultado['erro']}")

    def tela_listar_autor(self):
        autores = self.autor_model.listar()
        menu_gerenciar_autor.listar(
            ["id", "nome", "nacionalidade"],
            1,
            autores
        )

    def tela_atualizar_autor(self):
        self.autor_model.listar()
        resposta = menu_gerenciar_autor.formulario({
            'id autor': int,
            'nome': str,
            'nacionalidade': str
        })
        if resposta is None: 
            return
        resultado = self.autor_model.atualizar(resposta)
        if resultado['sucesso']:
            menu_gerenciar_autor.mensagem("Autor atualizado com sucesso!")
        else:
            menu_gerenciar_autor.mensagem(f"ERRO: {resultado['erro']}")


    def tela_excluir_autor(self):
        self.autor_model.listar()
        resposta = menu_gerenciar_autor.excluir()
        if resposta is None:
            return
        resultado = self.autor_model.excluir(resposta)
        if resultado['sucesso']:
            menu_gerenciar_autor.mensagem("Autor excluido com sucesso!")
        else:
            menu_gerenciar_livro.mensagem(f"ERRO: {resultado['erro']}")



    # ── Livro ────────────────────────────────────────────────
    def tela_menu_gerenciar_livro(self):
        while True:
            menu_gerenciar_livro.exibir_cabecalho()
            menu_gerenciar_livro.exibir_opcoes()
            try:
                opcao = menu_gerenciar_livro.capturar_digito(1, 5)
                if opcao == 5:
                    break
                self.menu_gerenciar_livro_opcoes[opcao]()
            except ValueError as e:
                menu_gerenciar_autor.mensagem(f"ERRO: {e}")

    def tela_cadastrar_livro(self):
        resposta = menu_gerenciar_livro.formulario({
            'id autor': int,
            'título': str,
            'data publicacão': int
        })
        if resposta is None:
            return
        resultado = self.livro_model.inserir(resposta)
        if resultado['sucesso']:
            menu_gerenciar_livro.mensagem("Livro cadastrado com sucesso!")
        else:
            menu_gerenciar_livro.mensagem(f"ERRO: {resultado['erro']}")

    def tela_listar_livro(self):
        autores = self.livro_model.listar()
        menu_gerenciar_livro.listar(
            ["id livro", "id autor", "título", "data publicacão"],
            2,
            autores
        )

    def tela_atualizar_livro(self):
        self.livro_model.listar()
        resposta = menu_gerenciar_livro.formulario({
            'id livro': int,
            'id autor': int,
            'título': str,
            'data publicacão': int
        })
        if resposta is None: 
            return
        resultado = self.livro_model.atualizar(resposta)
        if resultado['sucesso']:
            menu_gerenciar_livro.mensagem("Livro atualizado com sucesso!")
        else:
            menu_gerenciar_livro.mensagem(f"ERRO: {resultado['erro']}")

    def tela_excluir_livro(self):
        self.livro_model.listar()
        resposta = menu_gerenciar_livro.excluir()
        if resposta is None:
            return
        resultado = self.livro_model.excluir(resposta)
        if resultado['sucesso']:
            menu_gerenciar_livro.mensagem("Livro excluído com sucesso!")
        else:
            menu_gerenciar_livro.mensagem(f"ERRO: {resultado['erro']}")
