'''
menu_exemplo_uso.py: Não faz parte da estrutura principal do projeto.
Esse arquivo deve ser executado individualmente
'''
### TRECHO QUE IMPEDE ERROS DE IMPORTAÇÃO ###
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))
##############################################

from view.menu import Menu

def main():

    # CRIAÇÃO DOS MENUS:
    opcoes_CRUD = {
        1: "Cadastrar",
        2: "Listar",
        3: "Atualizar",
        4: "Excluir"
    }

    menu_principal = Menu("Menu principal", {
        1: "Gerenciar Autor",
        2: "Gerenciar Livro"
        },
        msg_ultima_opcao="Sair"
    )
    menu_gerenciar_autor = Menu("Menu principal / Gerenciar Autor", opcoes_CRUD)
    menu_gerenciar_livro = Menu("Menu principal / Gerenciar Livro", opcoes_CRUD)

    # EXEMPLO DE CADASTROS:
    print("CADASTROS")
    resultado = menu_gerenciar_autor.cadastrar({
        "nome": str,
        "nacionalidade": str
    })
    resultado = menu_gerenciar_livro.cadastrar({
        "id_autor": int,
        "titulo": str,
        "data_publicacao": int
    })

    # EXEMPLO DE ATUALIZAÇÕES:
    print("ATUALIZAÇÕES")
    novos_valores = menu_gerenciar_autor.cadastrar({
        "id_autor": int,
        "nome": str,
        "nacionalidade": str
    })
    resultado = menu_gerenciar_livro.cadastrar({
        "id_livro": int,
        "id_autor": int,
        "titulo": str,
        "data_publicacao": int
    })

    # EXEMPLO DE LISTAS:
    print("LISTAS")
    menu_gerenciar_autor.listar([
        "Nome",
        "Nacionalidade"
    ], [(1, "Brasilira"), (2, "Brasilira"), (3, "Alemã")])

    menu_gerenciar_livro.listar([
        "ID autor",
        "Titulo",
        "Data publicação"
    ], [(1, "Brasilira", 2000), (2, "Brasilira", 2000), (3, "Alemã", 2000)])

    # EXEMPLO EXCLUIR:
    print("EXCLUIR")
    resultado = menu_gerenciar_autor.excluir()
    resultado = menu_gerenciar_livro.excluir()

if __name__ == "__main__":
    main()