class SubMenu:
    def __init__(self, nome: str, entidade) -> None:
        self.nome = nome
        self.entidade = entidade
        self.opcoes = {
            "1": ("Cadastrar", self.cadastrar),
            "2": ("Listar", self.listar),
            "3": ("Atualizar", self.atualizar),
            "4": ("Excluir", self.excluir),
        }
        self.max_opcoes = len(self.opcoes) + 1

    def cabecalho(self):
        '''Exibe as opções do submenu'''
        print(
        f'''
    Sistema de Biblioteca Universitária
    ───────────────────────────────────
    Menu principal / {self.nome}
        '''
        )
        for digito, (nome, _) in self.opcoes.items():
            print(f"[{digito}] - {nome}")

        print(f"[{self.max_opcoes}] - Voltar")


    def processar_digito(self, digito) -> bool:
        if int(digito) == self.max_opcoes:
            return False

        self.opcoes[digito][1]()
        return True

    def cadastrar(self):
        print(f'''
    Cadastrar {self.entidade}
    Preencha as informações a seguir:
        ''')
        try:
            ...
        except Exception as e:
            print(e)

    def listar(self):
        print(f'''
    Listar {self.entidade}
    Preencha as informações a seguir:
        ''')
        try:
            ...
        except Exception as e:
            print(e)

    def atualizar(self):
        print(f'''
    Atualizar {self.entidade}
    Preencha as informações a seguir:
        ''')
        try:
            ...
        except Exception as e:
            print(e)

    def excluir(self):
        print(f'''
    Excluir {self.entidade}
    Preencha as informações a seguir:
        ''')
        try:
            ...
        except Exception as e:
            print(e)