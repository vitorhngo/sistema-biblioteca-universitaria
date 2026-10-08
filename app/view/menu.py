import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from view.submenu import SubMenu

class Menu:
    def __init__(self, autor, livro) -> None:
        self.submenus = {
            "1": SubMenu("Gerenciar autor", autor),
            "2": SubMenu("Gerenciar livro", livro)
        }
        self.max_opcoes = len(self.submenus) + 1 # Adiciona 1 em max para cobrir a opção de sair/voltar

    def cabecalho(self):
        '''Exibe as opções do menu'''
        print(
        f'''
    Sistema de Biblioteca Universitária
    ───────────────────────────────────
    Menu principal
        '''
        )
        for digito, submenu in self.submenus.items():
            print(f"[{digito}] - {submenu.nome}")

        # Calcula dinamicamente qual é a última opção e exibe a mensagem de sair/voltar
        print(f"[{self.max_opcoes}] - Sair")

    def capturar_digito(self, max) -> str:
        '''Pergunta ao usuário um dígito dentro do intervalo de opções'''
        min = 1
        resposta = input("Escolha: ")
        if not resposta.isdigit():
            raise ValueError("ERRO: Somente dígitos são aceitos. Tente novamente.")
        if not min <= int(resposta) <= max:
            raise ValueError(f"ERRO: Escolha um dígito entre {min} a {max}")
        return resposta

    def processar_digito(self, digito):
        if int(digito) == len(self.submenus) + 1:
            print("Saindo do sistema...")
            return False

        submenu = self.submenus[digito]
        while True:
            submenu.cabecalho()

            try:
                resposta = self.capturar_digito(submenu.max_opcoes)
            except Exception as e:
                print(e)
                continue

            resultado = submenu.processar_digito(resposta)
            if resultado == False: # Se o método retornar False, significa que o usuário escolheu a opção de Voltar.
                break
            
    @staticmethod
    def mensagem(texto):
        print(texto)