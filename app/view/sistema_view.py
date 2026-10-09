#TODO: Chamar esse módulo no Controller.
'''
sistema_view.py: Cria os menus e suas respectivas opções.
'''
from view.menu import Menu

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