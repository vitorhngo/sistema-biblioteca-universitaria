#XXX: Não deve ser chamado no Controller.
'''
menu.py: Contém a classe de Menus.
Esse arquivo é usado somente por sistema_view.py
'''
class Menu:
    def __init__(self, nome: str, opcoes: dict[int, str], msg_ultima_opcao = "Voltar") -> None:
        self.nome = nome
        self.opcoes = opcoes
        self.msg_ultima_opcao = msg_ultima_opcao

    def exibir_cabecalho(self):
        print(f'''
    Sistema de Biblioteca Universitária
    {self.nome}
        ''')

    def exibir_opcoes(self):
        for digito, nome in self.opcoes.items():
            print(f"[{digito}] - {nome}")
        ultimo_digito = len(self.opcoes) + 1
        print(f"[{ultimo_digito}] - {self.msg_ultima_opcao}")

    @staticmethod
    def capturar_digito(digito_min: int, digito_max: int) -> int:
        escolha = input("     Escolha: ")
        if not escolha.strip() or not escolha.isdigit():
            raise ValueError("Entrada inválida. Digite um número.")
        if not digito_min <= int(escolha) <= digito_max:
            raise ValueError(f"Entrada inválida. Digite um número entre {digito_min} e {digito_max}")
        return int(escolha)

    @staticmethod
    def cadastrar(campos: dict[str, type]):
        print('''
        Preencha as informações a seguir: 
        ''')
        respostas = []
        try:
            for campo, tipo in campos.items():
                campo_formatado = campo.capitalize().replace("_", " ")
                resposta = input(f"{campo_formatado}: ")

                if not resposta.strip():
                    raise ValueError(f"{campo} não pode ser vazio.")
                if resposta.isdigit():
                    resposta = int(resposta)
                if type(resposta) != tipo:
                    raise ValueError("Esse tipo de entrada não é válida. Tente novamente.")
                
                respostas.append(resposta)
            return respostas
        except Exception as e:
            print(f"\nERRO: {e}\n")

    @staticmethod
    def listar(campos: list[str], entidade: list[tuple]):
        if not entidade:
            print("\nNão há cadastros.\n")
        else:
            print("\n=== Resultads encontrados: ===\n")

            for tupla in entidade:
                linha = "| "
                for i, campo in enumerate(campos):
                    linha += f"{campo.capitalize()}: {tupla[i]} | "
                print(linha)

    @staticmethod
    def atualizar(campos: dict[str, type]):
        print('''
            Preencha as informações a seguir: 
            ''')
        respostas = []
        try:
            for campo, tipo in campos.items():
                campo_formatado = campo.capitalize().replace("_", " ")
                resposta = input(f"{campo_formatado}: ")

                if not resposta.strip():
                    raise ValueError(f"{campo} não pode ser vazio.")
                if resposta.isdigit():
                    resposta = int(resposta)
                if type(resposta) != tipo:
                    raise ValueError("Esse tipo de entrada não é válida. Tente novamente.")
                
                respostas.append(resposta)
            return respostas
        except Exception as e:
            print(f"\nERRO: {e}\n")

    @staticmethod
    def excluir():
        try:
            id = int(input("ID a excluir: "))
            return id
        except ValueError:
            print("\nEntrada inválida.\n")
            return None

    @staticmethod
    def mensagem(msg):
        print(msg)