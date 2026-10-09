# #TODO: Importar a view e chamá-la na função main.

# def main():
#     ...

# if __name__ == "__main__":
#     main()

from controller.autor_controller import AutorController

if __name__ == "__main__":
    app = AutorController()
    app.executar()