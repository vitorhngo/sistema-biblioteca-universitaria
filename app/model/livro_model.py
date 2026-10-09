# from dotenv import load_dotenv
# import os

# load_dotenv()  

# host = os.getenv("DB_HOST")
# port = os.getenv("DB_PORT")
# database = os.getenv("DB_NAME")
# user = os.getenv("DB_USER")
# password = os.getenv("DB_PASSWORD")

import psycopg2

class LivroModel:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname="biblioteca_universitaria",
                user="postgres",
                password="",
                host="localhost",
                port="5432"
            )

            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f"\nErro ao conectar ao banco de dados: {e}\n")

    def listar(self):
        try:
            self.cursor.execute("select * from livro order by id;")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"\nErro ao listar livros: {e}\n")
            return []
    
    def inserir(self, id_autor, titulo, data_publicacao):
        try:
            self.cursor.execute("insert into livro (id_autor, titulo, data_publicacao) values (%s,%s,%s);", (id_autor, titulo, data_publicacao))
            self.conn.commit()
        except Exception as e:
            print(f"\nErro ao inserir livro: {e}\n")
            self.conn.rollback()

    def existe_id(self, id_livro): #  Pode ser que aqui ao invés de 'id_livro', seja somente 'id'
        try:
            self.cursor.execute("select 1 from livro where id=%s;", (id_livro,))
            return self.cursor.fetchone is not None
        except Exception as e:
            print(f"\nErro ao verificar a existência do livro: {e}\n")
            return False
        
    def atualizar(self, id_livro, id_autor, titulo, data_publicacao): # Mesma lógica acima, aqui pode ser que 'id_livro' dê errado
        try:
            if not self.existe_id(id_livro):
                print("\nNenhum autor encontrado com esse ID.\n")
                return False
            self.cursor.execute("update livro set id_autor= %s, titulo= %s, data_publicacao= %s where id= %s;", (id_autor, titulo, data_publicacao))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"\nErro ao atualizar livro: {e}\n")
            self.conn.rollback()
            return False
    
    def excluir(self, id_livro):
        try:
            if not self.existe_id(id_livro):
                print("\nNenhum livro encontrado com esse ID.\n")
                return False
        
            self.cursor.execute("delete from livro where id= %s;", (id_livro,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"\nErro ao excluir livro: {e}\n")
            self.conn.rollback()
            return False
        
    def __del__(self):
        if hasattr(self, "cursor") and hasattr(self, "conn"):
            self.cursor.close()
            self.conn.close()
    
    